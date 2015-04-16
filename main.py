
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

    while countFOD != 0:
        try:
            frames.get_crossProductFrames(parse.FOD[0], parse.FOD[1])
            parse.FOD.remove(parse.FOD[0])
            parse.FOD.remove(parse.FOD[0])
            parse.FOD.insert(0, frames.insertFrame)
        except IndexError:
            break

    print("printing from main")
    print(parse.FOD)

    outputTextFile = CompatibilityRelations()
    outputTextFile.get_relations(parse.FOD, parse.dir_path)
    print(parse.dir_path)
    parse.openInputFile()

if __name__ == "__main__":
    main()