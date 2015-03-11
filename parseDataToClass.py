# Author Tami Hong Le
# 3/7/2015

class ParseDataToClass:

    frames = []
    CR = []
    relations = []
    questionFrame = []

    def __init__(self):
        pass

    def openInputFile(self):

        #open file, if path does not exist, print error message
        try:
            dir_path = raw_input("Enter the path to the Input.txt file:   ")
            inFile = open(dir_path, 'r')

            #parse the file by keywords: Question = Q, frame = B, and compatibility relations = CR
            for line in inFile:

                #send strings to methods by keywords
                if line.startswith('Q'):
                    self.parseDataToQuestionFrame(line)

                elif line.startswith('F'):
                    self.parseDataToFrame(line)

                elif line.startswith("R"):
                    self.parseDataToRelations(line)

                elif line.startswith("CR"):
                    self.parseDataToCR(line)
                else:
                    print ("Recheck your Input.txt file for consistency.\n")
                    print ("Question should use the abbreviation 'Q:' ")
                    print ("Frames should use the abbreviation 'B#:' where # is the sequential number starting from 1")
                    print ("Compatibility relations should use the abbreviation 'CR#:' where # is the sequential number starting from 1\n")
                    print ("The error exist in line --->     " + line)
                    inFile.close()
                    break

            inFile.close()
            return self.frames, self.CR, self.questionFrame, self.relations

        #throw an exception and reopen the openInputFile method again
        except IOError:
            print("The directory path to Input.txt file is invalid.\n")
            self.openInputFile()

    # packages two arrays into a dictionary
    def parseDataToQuestionFrame(self, str):

        splitter = str.split(':',3)
        question = [splitter[1], splitter[2]]
        answers = [splitter[3:len(splitter)]]
        self.questionFrame = {splitter[0]:[question,answers]}

        return self.questionFrame

    # an array of frames
    def parseDataToFrame(self, str):
        self.frames.append(str.rstrip('\n'))

        return self.frames

    #an array of frame relationship
    def parseDataToRelations(self, str):
        self.relations.append(str.rstrip('\n'))

        return self.CR

    #an array of compatibility relations (CR)
    def parseDataToCR(self, str):
        self.CR.append(str.rstrip('\n'))


    if __name__ == "__main__":
        openInputFile()



