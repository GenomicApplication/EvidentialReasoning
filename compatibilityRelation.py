
class CompatibilityRelations:

    dir_path = ''

    def __init__(self):
        pass

    #Opens up a new file in the same location as the Input.txt file and prints the
    #relations in there.
    def get_relations(self, crossProductFrame, input_dir_path):

        fileName = input("What did you want to name the output text file? :")
        outputText = open(input_dir_path.strip('Input.txt') + fileName, 'w')

        splitter = crossProductFrame[0].split(':')

        length_ofCPF = len(splitter) - 1
        relations = splitter[length_ofCPF].split(',')
        length_of_CR = len(relations)

        outputText.write("Please make your connect you relations. You have : " + str(length_of_CR)   + " relations to make. \n")
        outputText.write("Replace the # with the answer number.")
        outputText.write("The compatibility relations are: \n")

        count = 1

        for elements in relations:
            outputText.write('CR' + str(count) + ': Q# :' + elements + '\n')
            count = count + 1

        outputText.close()

        self.dir_path = input_dir_path + fileName

        print("Open the file at :   " + self.dir_path  + " and make the proper relations to the question frame." )

        return self.dir_path





