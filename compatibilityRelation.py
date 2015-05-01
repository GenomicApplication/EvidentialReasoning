'''
This class takes in the parsed compatibility relations from parsedDataToClass.py
and organizes it into a dictionary with the keys as the cross product frames and
the values are its propositions.
'''

class CompatibilityRelations:

    crossed_frame = {}

    def __init__(self):
        pass

    #arranging the compatibility relations into a dictionary
    def get_relations(self,parsedCR):

        for elements in parsedCR:
            crossedPropositions = []
            x = 2

            splitter = elements.split(':')
            length_of_splitter = len(splitter)
            crossedFrameName = splitter[1]

            while x < length_of_splitter:
                propositions = splitter[x]
                crossedPropositions.append(propositions)
                self.crossed_frame[crossedFrameName] = crossedPropositions
                x = x + 1

        print("Printing compatibility relations dictionary")
        print(self.crossed_frame)
        print("\n")

        return self.crossed_frame






