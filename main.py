
from parseDataToClass import *
from compatibilityRelation import *
from frame import *
from analysis import *


def main():

    parse = ParseDataToClass()
    parse.openInputFile()

    print("Parsed Information for frames, CR, Question, AND FOD \n")
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

    count_dictionary_occurrence = 0

    while countFOD != 0:
        try:
            frames.get_crossProductFrames(parse.FOD[0], parse.FOD[1],count_dictionary_occurrence)
            parse.FOD.remove(parse.FOD[0])
            parse.FOD.remove(parse.FOD[0])
            parse.FOD.insert(0, frames.insertFrame)
            count_dictionary_occurrence = count_dictionary_occurrence + 1

        except IndexError:
            break

    print("printing from main")
    print(parse.FOD)

    CR = CompatibilityRelations()
    CR.get_relations(parse.CR)
    print(CR.answerDictionary)





if __name__ == "__main__":
    main()