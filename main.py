
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

    #printing the information to an Output.txt file
    out_dir_path = parse.dir_path.strip("Input.txt")
    output = open(out_dir_path + "Output.txt", 'w')
    output.write("The Question is : \n\n")

    for k,v in parse.questionFrame.items():
        output.write(v[0] + '\n\n')
        output.write("The answers to the question is : \n\n")

        for i in v[1]:
            answers = i.split(',')
            for j in answers:
                output.write('{:10}{:10}\n'.format(j))

    #for k,v in




if __name__ == "__main__":
    main()
