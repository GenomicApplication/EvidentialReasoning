

import itertools
import re
from parseDataToClass import *
from main import *
from collections import Counter


class Analysis:
    translatedFrame1 = {}
    translatedFrame2 = {}
    newFrame = ''
    b = []

    def __init__(self):
        pass


    def discount(self, alpha, mass):
        try:
            # print("Entered discount operation")
            alpha = float(alpha)
            mass = float(mass)

            if alpha >= 1 or alpha <= 0:
                print("The number must be between 0 and 1.")
                self.discount(alpha, mass)
            else:
                self.discounted = float(alpha) * float(mass)
                return self.discounted

        except (TypeError, ValueError):
            print("Must be a numeric value and not a string value.\n")
            print("Please recheck the input text file and make sure all values are correct.")


    def translate(self, frame1, relations1, frame2, relations2):
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

        # iterate through an unknown length of the Frame 1, and collect all the belief values
        # record the translated frame in a dictionary
        while x < length_ofFrame1:
            try:
                for j in relations2:
                    proposition = frame1[x + 1]
                    key = proposition + ' v ' + str(j)
                    value = float(frame1[x])
                    mass = float(mass) + value
                    self.translatedFrame1[key] = float(frame1[x])
                    theta = float(1 - mass)
                    self.translatedFrame1["theta"] = theta
                    string1 = string1 + ':' + str(frame1[x]) + ':' + key
                    x = x + 2
            except:
                break

        #iterate through an unknown length of the Frame 2, and collect all the belief values
        #record the translated frame in a dictionary
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
                    y = y + 2
            except:
                break

        print(self.translatedFrame1)
        print(self.translatedFrame2)

        self.fuse(self.translatedFrame1, self.translatedFrame2)

        self.newFrame = "FOD:" + frame1[0] + 'x' + frame2[0] + ': NO:' + '0' + string1 + string2

        return self.translatedFrame1, self.translatedFrame2, self.newFrame


    # Dempster's combination rule
    def fuse(self, massA, massB):
        i = 0
        a = 0
        sum1 = []
        sumk = []
        for key, value in massB.items():
            for keys, values in massA.items():
                print(((keys)), ((key)))
                if keys == 'theta' or key == 'theta':
                    print(values)
                    print(value)
                    result = (value * values)
                    print(result)
                    sum1.append(result)
                    if key == "theta" and keys == "theta":
                        x = ("theta"), (result)
                        self.b.append(x)
                    elif key == "theta" and keys != "theta":
                        x = keys, result
                        self.b.append(x)
                    elif key != "theta" and keys == "theta":
                        x = key, result
                        self.b.append(x)
                elif keys != "theta" and key != "theta":
                    count = 0
                    count1 = 0
                    print ("here")
                    s1 = set(key.split(' '))
                    s2 = set(keys.split(' '))
                    if any(s1.intersection(s2)):
                        print("found a match!")
                        print(values)
                        print(value)
                        result1 = (value * values)
                        print(result1)
                        sum1.append(result1)
                        x = (key, result1)
                        self.b.append(x)
                        break
                    else:
                        print("No Match")
                        print(value)
                        print(values)
                        result2 = (1 - (value * values))
                        print(result2)
                        sumk.append(result2)
                        x = (key, result2)
                        self.b.append(x)

            i = i + 1
            a = a + 1
        print(self.b)
        print(sum1)
        sum1 = sum(sum1)
        print(sum1)
        print(sumk)
        sumk = sum(sumk)
        print(sumk)
        if sumk != 0:
            K = 1 / sumk
            print("K = ", K)
            m1x2 = K * sum1
            print("The mass of 1 and 2 is : ", (m1x2))
        else:
            m1x2 = sum1
            print("The mass of 1 and 2 is : ", (m1x2))



    def interpret(self, b, newDirectory ):
        output_dir =open(newDirectory + "Output.txt", 'w')
        print (b)
        support = 0
        val = []
        for keys,values in b:
            print (keys)
            print (values)
            val.append(values)
            print (val)
        val = sum(val)
        print (val)
        for keys, values in b:
            counter = (Counter(keys) in b)
            print (keys)
            print (values)
            if counter == True:
                print ('sum all')
                support = sum(values)
                print (("Support : "), support)
                plausibility = abs((1-((val)-values)))
                print (("Plausibility: "),plausibility)
                EI = [support, plausibility]
                print ("EI:", EI)
            else:
                support = values
                print (("Support : "), support)
                plausibility = abs((1-((val)-values)))
                print (("Plausibility: "),plausibility)
                EI = [support, plausibility]
                print ("EI:", EI)





