

class Analysis:

    translatedFrame1 = {}
    translatedFrame2 = {}
    newFrame = ''
    beliefValuesDictionary = {}

    def __init__(self):
        pass


    def discount(self, alpha, mass):
        try:
            #print("Entered discount operation")
            alpha = float(alpha)
            mass = float(mass)

            if alpha >= 1 or alpha <= 0:
                print("The number must be between 0 and 1.")
                self.discount(alpha, mass)
            else:
                self.discounted = float(alpha) * float(mass)
                return self.discounted

        except (TypeError,ValueError):
            print("Must be a numeric value and not a string value.\n")
            print("Please recheck the input text file and make sure all values are correct.")



    def translate(self,frame1, relations1, frame2, relations2, count_dictionary_occurrence):
        print("Entered Translating Operation\n")

        x = 3
        y = 3

        mass = 0
        mass2 = 0

        theta = 0
        theta2 = 0

        string1 = ''
        string2 = ''

        length_ofFrame1 = len(frame1)
        length_ofFrame2 = len(frame2)

        self.translatedFrame1.clear()
        self.translatedFrame2.clear()

        while x < length_ofFrame1:
            try:
                for j in relations2:
                    proposition = frame1[x+1]
                    key = proposition + ' v ' + str(j)
                    value = float(frame1[x])
                    mass = float(mass) + value
                    self.translatedFrame1[key] = float(frame1[x])
                    theta = float(1 - mass)
                    self.translatedFrame1["theta"] = theta
                    string1 = string1 + ':' + str(frame1[x]) + ':' + key

                    if count_dictionary_occurrence == 0:
                        self.set_beliefValuesDictionary(proposition,value)
                        print(self.beliefValuesDictionary)

                    x = x + 2
            except:
                break

        while y < length_ofFrame2:
            try:
                for i in relations1:
                    proposition = frame2[y + 1]
                    key2 = proposition + ' v ' + str(i)
                    value = float(frame2[y])
                    mass2 = float(mass2) + value
                    self.translatedFrame2[key2] = float(frame2[y])
                    theta2 = float(1 - mass2)
                    self.translatedFrame2["theta"] = theta2
                    string2 = string2 + ':' + str(frame2[y]) + ':' + key2

                    if count_dictionary_occurrence == 0:
                        self.set_beliefValuesDictionary(proposition,value)
                        print(self.beliefValuesDictionary)

                    y = y + 2
            except:
                break

        print(self.translatedFrame1)
        print(self.translatedFrame2)
        print(self.beliefValuesDictionary)

        self.newFrame = "FOD:" + frame1[0] + 'x' + frame2[0] + ': NO:' + '0' + string1 + string2

        return self.translatedFrame1, self.translatedFrame2, self.newFrame, self.beliefValuesDictionary

    def set_beliefValuesDictionary(self, key, value):
        print("print in function")
        self.beliefValuesDictionary[key] = value

    # Dempster's combination rule
    def fuse(self,translatedFrame1, translatedFrame2):

        pass

    def interpret(self):
        pass
