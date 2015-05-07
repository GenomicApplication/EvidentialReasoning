from analysis import *
from output import *

'''
# Author Tami Hong Le

def organize_frames organizes frames into a list with frame information and a list with all the propositions

'''


class Frames:

    mainPropositions = []
    mainFrame = []
    insertFrame = ''

    def __init__(self):
        pass


    #orgaizes the frames into lists
    def organize_frames(self,frames,FODs):
        file_write("The frames are : \n\n")

        for i in frames:
            frame = i.split(':')
            file_write('\t' + frame[1] + ' = ' + frame[2] + '\n')

        file_write('\n')

        for i in frames:
            frame = i.split(":")
            file_write("The propositions for " + '"' + frame[1] + '"' + " frame is: \n\n")
            props = frame[3].split('/')
            #self.mainFrame.append(frame[1:3])
            #self.mainPropositions.append(props)
            number = 1
            
            for prop in props:
                file_write('\t{0}{1:7}{2} \n'.format(frame[1], str(number), prop.strip()))
                number = number + 1
                
            file_write('\n')

        file_write("The initial mass density for each input node's proposition are: \n\n")
        file_write('\t\t{0:30}{1}'.format("Proposition","Mass\n"))
        file_write('\t\t{0}'.format("___________________________________\n\n"))

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
                file_write('\t\t{0:30}{1}\n'.format(k.strip(),v))
    
            file_write('\t\t{0}'.format("___________________________________\n"))
            file_write('\t\t{0:30}{1}'.format("Total of mass is :            ", str(total) + "\n\n\n"))

        print(self.mainFrame)
        print(self.mainPropositions)
            
        return self.mainFrame, self.mainPropositions


    #to get the cross product frames after discount and translating operations
    def get_crossProductFrames(self, FOD1, FOD2, compatibilityRelationsDictionary,count):
        print("ENTERED get_crossProductFrames from analysis.py")
        cross = Analysis()
        relations1 = []
        relations2 = []

        splitter1 = FOD1.split(':')
        splitter2 = FOD2.split(':')

        alpha1 = float(splitter1[3])
        alpha2 = float(splitter2[3].strip())

        discountOption1 = splitter1[2].upper().strip()
        discountOption2 = splitter2[2].upper().strip()

        length_ofFOD1 = len(splitter1) - 2
        length_ofFOD2 = len(splitter2) - 2

        x = 4
        y = 4


        #iterates through the FOD list and check for discounting operation
        while  x < length_ofFOD1:
            #accounts for the discount operation before crossing the frames
            if discountOption1 == 'YES':
                mass1 = float(splitter1[x].strip())
                discounts1 = Analysis()
                splitter1[x] = discounts1.discount(alpha1, mass1)
                splitter1[3] = 0
                splitter1[2] = "NO"
                file_write('\t\t{0:20}{1}\n'.format("Frame:",splitter1[1].strip()))
                file_write('\t\t{0:20}{1}\n'.format("Proposition:",splitter1[x+1].strip()))
                file_write('\t\t{0:20}{1:1.5f}\n'.format("alpha #:",alpha1))
                file_write('\t\t{0:20}{1:1.4f}\n'.format("Begin mass:",mass1))
                file_write('\t\t{0:20}{1:1.4f}\n\n\n'.format("End mass:",splitter1[x]))
                x = x + 2
            else:
                file_write('\tDiscount Operation\n')
                file_write('\t___________________________________\n\n')
                file_write('\t\t{0:20}{1}\n'.format("Frame :   ", splitter1[1]))
                file_write('\t\t{0}\n\n\n'.format("Discount was detected"))
                x = length_ofFOD1

        while y < length_ofFOD2:
            if discountOption2 == 'YES':
                mass2 = float(splitter2[y].strip())
                discounts2 = Analysis()
                splitter2[y] = discounts2.discount(alpha2, mass2)
                splitter2[3] = 0
                splitter2[2] = "NO"
                file_write('\t\t{0:20}{1}\n'.format("Frame:",splitter1[1].strip()))
                file_write('\t\t{0:20}{1}\n'.format("Proposition:",splitter1[y+1].strip()))
                file_write('\t\t{0:20}{1:1.5f}\n'.format("alpha #:",alpha2))
                file_write('\t\t{0:20}{1:}\n'.format("Begin mass:",mass2))
                file_write('\t\t{0:20}{1}\n\n\n'.format("End mass:",splitter2[y]))
                y = y + 2

            else:
                file_write('\tDiscount Operation\n')
                file_write('\t___________________________________\n\n')
                file_write('\t\t{0:20}{1}\n'.format("Frame :   ", splitter2[1]))
                file_write('\t\t{0}\n\n\n'.format("Discount was not detected"))
                y = length_ofFOD2


        length_ofFrameInfo1 = len(splitter1) - 1
        length_ofFrameInfo2 = len(splitter2) - 1

        frameInfo1 = splitter1[1: length_ofFrameInfo1]
        relations1.append(splitter1[length_ofFrameInfo1].split(','))
        relation1 = splitter1[length_ofFrameInfo1].split(',')


        frameInfo2 = splitter2[1: length_ofFrameInfo2]
        relations2.append(splitter2[length_ofFrameInfo2].split(','))
        relation2 = splitter2[length_ofFrameInfo2].split(',')

        cross.translate(frameInfo1,frameInfo2, compatibilityRelationsDictionary,count)

        string = ''

        count = 1

        #appends the cross product propositions to a new FOD frame
        for i in relation1:
            for j in relation2:
                if count < 2:
                    string = i + j
                    count = count + 1
                else:
                    string = string + ',' + i + j
                    count = count + 1

        self.insertFrame = cross.newFrame + ':' + frameInfo1[0] + ' X ' + frameInfo2[0] + ':' + string

        return cross.translate, self.insertFrame

