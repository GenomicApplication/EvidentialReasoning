from frame import *
from compatibilityRelation import *
from analysis import *

def output(questionFrame,frames,FODs,parsedCR):

    output_text_name = str(input("What would you like to name your output txt file? note you must end it with .txt:   "))
    output = open(output_text_name, 'w')

    output.write("The Question is : \n\n")

    for k,v in questionFrame.items():
        output.write("\t" + v[0] + '\n\n')
        output.write("The answers to the question is : \n\n")

        for i in v[1]:
            answers = i.split(',')
            for j in answers:
                output.write("\t" + j + '\n')

    output.write("The frames are : \n\n")

    for i in frames:
        frame = i.split(':')
        output.write('\t' + frame[1] + ' = ' + frame[2] + '\n')

    output.write('\n')

    for i in frames:
        frame = i.split(':')
        output.write("The propositions for " + '"' + frame[1] + '"' + " frame is: \n\n")
        props = frame[3].split('/')
        number = 1

        for prop in props:
            output.write('\t{0}{1:7}{2} \n'.format(frame[1], str(number), prop.strip()))
            number = number + 1

        output.write('\n')

    output.write("The initial mass density for each input node's proposition are: \n\n")
    output.write('\t\t{0:30}{1}'.format("Proposition","Mass\n"))
    output.write('\t\t{0}'.format("___________________________________\n\n"))

    for FOD in FODs:
        f = FOD.split(':')
        len_of_f = len(f) - 2
        x = 4
        sum = 0
        temp_dic = {}
        total = 0

        while x < len_of_f:
            sum = sum + float(f[x])
            key = f[x+1].strip()
            temp_dic[key] = f[x].strip()
            x = x + 2

        theta = 1 - sum
        total = format(sum + theta,'1.2f')
        temp_dic['theta for ' + f[1] + ' frame'] = format(theta,'1.2f')


        for k,v in temp_dic.items():
            output.write('\t\t{0:30}{1}\n'.format(k.strip(),v))

        output.write('\t\t{0}'.format("___________________________________\n"))
        output.write('\t\t{0:30}{1}'.format("Total of mass is :            ", str(total) + "\n\n\n"))


    output.write("ENTERING ANALYSIS\n\n\n")

    for FOD in FODs:
        y = 4
        f = FOD.split(':')
        len_of_f = len(f) - 2
        discounts = Analysis()
        alpha = float(f[3])

        while y < len_of_f:
            if f[2].upper().strip() == "YES":
                mass = format(float(f[y].strip()),'1.5f')
                output.write('\tDiscount operation : \n')
                output.write('\t___________________________________\n\n')
                output.write('\t\t{0:20}{1}\n'.format("Frame:",f[1].strip()))
                output.write('\t\t{0:20}{1}\n'.format("Proposition:",f[y+1].strip()))
                output.write('\t\t{0:20}{1:1.5f}\n'.format("alpha #:",alpha))
                output.write('\t\t{0:20}{1:}\n'.format("Begin mass:",str(mass)))
                newMass = format(discounts.discount(alpha,mass),'1.5f')
                output.write('\t\t{0:20}{1}\n\n'.format("End mass:",newMass))
                y = y + 2
            else:
                output.write('\t{0}{1}\n'.format("Discount was not detected for frame :   ", f[1]))
                y = len_of_f

    countFOD = len(FODs)
    frame = Frames()
    frame.organize_frames(frames)
    CR = CompatibilityRelations()
    CR.get_relations(parsedCR)

    while countFOD != 0:
        try:
            frame_zero = FODs[0].split(':')
            frame_one = FODs[1].split(':')
            print("PRINTING FOR FRAME_ZERO AND FRAME_ONE")
            print(frame_zero)
            print(frame_one)
            x = 4
            y = 4

            output.write('\n\n\n')
            output.write('\tTranslate operation: \n')
            output.write('\t_____________________________________________________________\n\n')
            output.write('\t{0:10}{1}\n\n'.format("Frame:", frame_zero[1] + ' X ' + frame_one[1]))
            output.write('\t{0:50}{1}\n'.format("Proposition","Begin Mass"))

            len_of_frame_zero = len(frame_zero) - 2
            len_of_frame_one = len(frame_one) - 2

            while x < len_of_frame_zero:
                output.write('\t{0:50}{1}\n'.format(frame_zero[x+1].strip(),frame_zero[x].strip()))
                x = x +2

            while y < len_of_frame_one:
                output.write('\t{0:50}{1}\n'.format(frame_one[y+1].strip(),frame_one[y].strip()))
                y = y +2

            frame.get_crossProductFrames(FODs[0], FODs[1], CR.crossed_frame)

            FODs.remove(FODs[0])
            FODs.remove(FODs[0])
            FODs.insert(0, frame.insertFrame)
        except IndexError:
            break




