
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

    #printing the file to an Output.txt file
    out_dir_path = parse.dir_path.strip("Input.txt")
    output = open(out_dir_path + "Output.txt", 'w')





if __name__ == "__main__":
    main()
