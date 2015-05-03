# Author Tami Hong Le
# 3/7/2015
from utils import *

class ParseDataToClass:

    frames = []
    CR = []
    questionFrame = []
    FOD = []
    dir_path = ''

    def __init__(self):
        pass

    def openInputFile(self):
        #open file, if path does not exist, print error message
        try:
            if DEBUG:
                self.dir_path = "test.txt"
            else:
                self.dir_path = input("Enter the path to the text file:   ")

            inFile = open(self.dir_path, 'r')

            #parse the file by keywords: Question, frame, and compatibility relations = CR
            for line in inFile:

                #send strings to methods by keywords
                if line.startswith('Question'):
                    self.parseDataToQuestionFrame(line)

                elif line.startswith('Frame'):
                    self.parseDataToFrame(line)

                elif line.startswith("CR"):
                    self.parseDataToCR(line)

                elif line.startswith("FOD"):
                    self.parseDataToFOD(line)

                else:
                    print("Recheck your Input.txt file for consistency.\n")
                    print("Question should use the abbreviation 'Question:' ")
                    print("Frames should be named ""Frames"":")
                    print("Compatibility relations should use the abbreviation 'CR:' \n")
                    print("The error exist in line --->     " + line)
                    inFile.close()
                    break

            inFile.close()
            return self.frames, self.CR, self.questionFrame, self.dir_path

        #throw an exception and reopen the openInputFile method again
        except IOError:
            print("The directory path to Input.txt file is invalid.\n")
            self.openInputFile()

    # packages two arrays into a dictionary
    def parseDataToQuestionFrame(self, str):
        splitter = str.split(':')
        key = splitter[0]
        question = splitter[1]
        answers = splitter[2:len(splitter)]
        self.questionFrame = {key:[question,answers]}

        return self.questionFrame

    # an array of frames
    def parseDataToFrame(self, str):
        self.frames.append(str.rstrip('\n').strip())

        return self.frames

    #an array of compatibility relations (CR)
    def parseDataToCR(self, str):
        self.CR.append(str.rstrip('\n').strip())

        return self.CR

    def parseDataToFOD(self,str):
        self.FOD.append(str.rstrip('\n').strip())
        return self.FOD






