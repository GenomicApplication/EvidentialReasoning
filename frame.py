from analysis import *

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
    def organize_frames(self,frames):
        for elements in frames:
            splitter = elements.split(":")
            self.mainFrame.append(splitter[1:3])
            self.mainPropositions.append(splitter[3].split('/'))
        return self.mainFrame, self.mainPropositions


    #to get the cross product frames after discount and translating operations
    def get_crossProductFrames(self, FOD1, FOD2, compatibilityRelationsDictionary):

        cross = Analysis()
        relations1 = []
        relations2 = []

        splitter1 = FOD1.split(':')
        splitter2 = FOD2.split(':')

        alpha1 = splitter1[3]
        alpha2 = splitter2[3].strip()

        discountOption1 = splitter1[2].upper().strip()
        discountOption2 = splitter2[2].upper().strip()

        length_ofFOD1 = len(splitter1) - 2
        length_ofFOD2 = len(splitter2) - 2

        x = 4
        y = 4

        #iterates through the FOD list and check for discounting operation
        while y < length_ofFOD2 or x < length_ofFOD1:

            #accounts for the discount operation before crossing the frames
            if discountOption1 == 'YES' and x < length_ofFOD1:
                mass1 = splitter1[x].strip()
                discounts1 = Analysis()
                splitter1[x] = discounts1.discount(alpha1, mass1)
                splitter1[3] = 0
                splitter1[2] = "NO"
                x = x + 2


            elif discountOption2 == 'YES' and y < length_ofFOD2:
                mass2 = splitter2[y].strip()
                discounts2 = Analysis()
                splitter2[y] = discounts2.discount(alpha2, mass2)
                splitter2[3] = 0
                splitter2[2] = "NO"
                y = y + 2

            else:
                x = x + 2
                y = y + 2


        length_ofFrameInfo1 = len(splitter1) - 1
        length_ofFrameInfo2 = len(splitter2) - 1

        frameInfo1 = splitter1[1: length_ofFrameInfo1]
        relations1.append(splitter1[length_ofFrameInfo1].split(','))
        relation1 = splitter1[length_ofFrameInfo1].split(',')


        frameInfo2 = splitter2[1: length_ofFrameInfo2]
        relations2.append(splitter2[length_ofFrameInfo2].split(','))
        relation2 = splitter2[length_ofFrameInfo2].split(',')

        cross.translate(frameInfo1,frameInfo2, compatibilityRelationsDictionary)

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

