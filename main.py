
from parseDataToClass import *
from compatibilityRelation import *
from frame import *
from analysis import *

def main():

    parse = ParseDataToClass()
    parse.openInputFile()

    print("Information from the Input.txt are parsed :\n")
    print(parse.questionFrame)
    print (parse.frames)
    print(parse.CR)
    print(parse.FOD)
    print('\n')

    countFOD = len(parse.FOD)
    frames = Frames()
    frames.organize_frames(parse.frames)
    print(frames.mainFrame)
    print(frames.mainPropositions)

    CR = CompatibilityRelations()
    CR.get_relations(parse.CR)

    #printing the information to an Output.txt file
    out_dir_path = parse.dir_path.strip("Input.txt")
    output = open(out_dir_path + "Output.txt", 'w')
    output.write("The Question is : \n\n")

    for k,v in parse.questionFrame.items():
        output.write("\t" + v[0] + '\n\n')
        output.write("The answers to the question is : \n\n")

        for i in v[1]:
            answers = i.split(',')
            for j in answers:
                output.write("\t" + j + '\n')

    output.write("The frames are : \n\n")

    for i in parse.frames:
        frame = i.split(':')
        output.write('\t' + frame[1] + ' = ' + frame[2] + '\n')

    output.write('\n')

    for i in parse.frames:
        frame = i.split(':')
        output.write("The propositions for " + '"' + frame[1] + '"' + " frame is: \n\n")
        props = frame[3].split('/')
        number = 1

        for prop in props:
            output.write('\t{0}{1:7}{2} \n'.format(frame[1], str(number), prop.strip()))
            number = number + 1

        output.write('\n')

    output.write("The initial mass density assigned to the propositions are : \n\n")
    output.write('\t\t{0:30}{1}'.format("Proposition","Mass\n"))
    output.write('\t\t{0}'.format("___________________________________\n\n"))

    for FOD in parse.FOD:
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

    #crosses the frames and finds the new cross product frame
    while countFOD != 0:
        try:
            frames.get_crossProductFrames(parse.FOD[0], parse.FOD[1], CR.crossed_frame)
            parse.FOD.remove(parse.FOD[0])
            parse.FOD.remove(parse.FOD[0])
            parse.FOD.insert(0, frames.insertFrame)

        except IndexError:
            break

    print(parse.FOD)

    interpret = Analysis()
    #newDirectory = parse.dir_path.strip("Input.txt")
    #interpret.interpret(interpret.b, newDirectory)

if __name__ == "__main__":
    main()
