
class CompatibilityRelations:

    answerDictionary = {}

    def __init__(self):
        pass

    #Opens up a new file in the same location as the Input.txt file and prints the
    #relations in there.
    def get_relations(self,parsedCR):

        for elements in parsedCR:

            splitter = elements.split(':')
            key = splitter[1]
            value = splitter[2].split(',')
            print(splitter)
            print(key)
            print(value)
            self.answerDictionary[key] = value

        return self.answerDictionary





