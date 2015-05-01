
from collections import Counter

''' This class serves as the four major operations of discount, translate, fuse, and interpret

def discount needs an alpha and mass parameter to adjust the impact

def translate takes in 4 parameters, two frames at a time, with its relations = propositions

def fuse uses the Dempster's combination rule to perform orthogonal sum to derive a new mass density
across intersections and normalizes evidence that does not intersect

def interpret uses the combined translated frame along with the mass densities derived from fuse
to interpret the evidence pertaining to answers of the question frame
'''

class Analysis:

    translatedFrame1 = {}
    translatedFrame2 = {}
    newFrame = ''
    b = []


    def __init__(self):
        pass

    #adjust the impact based on new evidence
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


    # combines the two frames to arrive at a new cross product frame
    def translate(self,frame1,frame2,compatibilityRelations):
        print("Entered Translate Operation\n")

        x = 3
        y = 3

        mass = 0
        mass2 = 0

        theta = 0
        theta2 = 0

        length_ofFrame1 = len(frame1)
        length_ofFrame2 = len(frame2)

        print("PRINTING FRAMES ")
        print(frame1)
        print(frame2)

        strToMatch1x2 =   frame1[0] + ' X ' + frame2[0]
        strToMatch2x1 =   frame2[0] + ' X ' + frame1[0]

        print("PRINTING FRAMES TO MATCH")
        print(strToMatch1x2)
        print(strToMatch2x1)

        self.translatedFrame1.clear()
        self.translatedFrame2.clear()


        #iterate through an unknown length of the Frame 1, and collect all the belief values
        #Finally, record the translated frame in a dictionary
        while x < length_ofFrame1:
            try:
                proposition = frame1[x+1]
                print("PRINTING PRPOSITIONS 1")
                print(proposition)
                value = float(frame1[x])
                mass = float(mass) + value
                theta = float(1 - mass)

                for key1,value1 in compatibilityRelations.items():
                    print("PRINTING KEY 1")
                    print(key1)
                    print("PRINTING strToMatch1x2")
                    print(strToMatch1x2)

                    if key1 == strToMatch1x2:
                        print("MATCH FOR 1X2 IS FOUND")
                        print(key1)
                        splitter = proposition.split('U')
                        length_of_splitter = len(splitter)
                        i = 0
                        dic = {}
                        print("PRINTING PROPOSITION")
                        print(proposition)
                        print("PRINTING SPLITTER")
                        print(splitter)

                        while i < length_of_splitter:
                            string = splitter[i].strip()
                            print("PRINTING THE PROPOSITION FOUND IN FRAME 1")
                            print(string)

                            for elements in value1:
                                print("PRINTING ELEMENTS for value 1")
                                print(elements)
                                if elements.find(string) != -1:
                                    print(string + " Exists")
                                    newString = elements.strip(string + '/')
                                    print("STRIPPED STRING")
                                    print(newString)
                                    print("PRINTING NEW STRING")
                                    print(newString)

                                    if elements.find('v') != -1:
                                        h = newString
                                        dic[h] = 1
                                    else:
                                        h = newString.split(',')

                                        for each in h:
                                            print(each)
                                            dic[each] = 1
                            i = i + 1

                            print("printing dictionary at the end of 1st while")
                            print(dic)

                        temp_array = []

                        for key3,value3 in dic.items():
                            temp_array.append(key3)
                            print("PRINTING TEMP ARRAY")
                            print(temp_array)
                        temp_array.sort()
                        print("SORTED ARRAY")
                        print(temp_array)

                        len_of_temp_array = len(temp_array)
                        w = 0
                        string6 = ''

                        while w < len_of_temp_array:
                            if string6 == '':
                                string6 = temp_array[w]
                                w = w + 1
                            else:
                                string6 = string6 + ',' + temp_array[w]
                                w = w +1

                        print("ORGANIZED STRING")
                        print(string6)

                        key4 = proposition + ' v (' + string6 + ')'
                        self.translatedFrame1[key4] = value
                        self.translatedFrame1["theta"] = theta

                x = x + 2

            except:
                break


        #iterate through an unknown length of the Frame 2, and collect all the belief values
        #record the translated frame in a dictionary
        while y < length_ofFrame2:
            print("ENTERED 2ND WHILE LOOP")
            try:
                proposition2 = frame2[y+1]
                value2 = float(frame2[y])
                mass2 = float(mass2) + value2
                theta2 = float(1 - mass2)

                for key3,value3 in compatibilityRelations.items():
                    if key3 == strToMatch2x1:
                        print("PRINTING KEY IN SECOND WHILE LOOP")
                        print(key3)
                        print('PRINTING VALUE IN SECOND WHILE LOOP')
                        print(value3)
                        splitter2 = proposition2.split('U')
                        length_of_splitter2 = len(splitter2)
                        m = 0
                        dic2 = {}

                        while m < length_of_splitter2:
                            string2 = splitter2[m].strip()
                            print("PRINTING THE STRING FOUND IN FRAME 2")
                            print(string2)

                            for elements2 in value3:
                                print("printing elements 2")
                                print (elements2)

                                if elements2.find(string2) != -1:
                                    print("A MATCH IS FOUND IN 2")
                                    newString2 = elements2.strip(string2 + '/')
                                    print("Printing STRIPPE STRING IN 2")
                                    print(newString2)

                                    if elements2.find('v') != -1:
                                        f = newString2
                                        dic2[f] = 1
                                    else:
                                        f = newString2.split(',')
                                        print("printing f in loop2")
                                        print(f)

                                        for each2 in f:
                                            print('each2 in while loop 2')
                                            print(each2)
                                            dic2[each2] = 1
                            m = m + 1

                            print("PRINTING DICTIONARY 2")
                            print(dic2)

                        temp_array2 = []

                        for key4,value4 in dic2.items():
                            print("PRINTING KEY IN 2")
                            print(key4)
                            temp_array2.append(key4)
                            print("PRINTING TEMP ARRAY 2")
                            print(temp_array2)
                        temp_array2.sort()
                        print('SORTED ARRAY 2')
                        print(temp_array2)

                        len_of_temp_array2 = len(temp_array2)
                        p = 0
                        string7 = ''

                        while p < len_of_temp_array2:
                            if string7 == '':
                                string7 = temp_array2[p]
                                p = p + 1
                            else:
                                string7 = string7 + ',' + temp_array2[p]
                                p = p + 1
                        print("ORGANIZED STRING IN 2")
                        print(string7)

                        key5 = proposition2 + ' v (' + string7 + ')'
                        self.translatedFrame2[key5] = value2
                        self.translatedFrame2["theta"] = theta2
                y = y + 2
            except:
                print("Breaking out of the 2nd while loop")
                break
        print("broke out of the 2nd while loop")
        comboString1 = ''

        for key6,value6 in self.translatedFrame1.items():
            if key6 != 'theta':
                print("PRINTING KEY 6")
                print(key6)
                if comboString1 == '':
                    comboString1 = ':' + str(value6) + ':' + key6
                else:
                    comboString1 = comboString1 + ':' + str(value6) + ':' + key6
        print("PRINTING COMBO STRING 1")
        print(comboString1)
        comboString2 = ''

        for key8,value8 in self.translatedFrame2.items():
            if key8 != 'theta':
                print("PRINTING KEY 8")
                print(key8)
                if comboString2 == '':
                    comboString2 = ':' + str(value8) + ':' + key8
                else:
                    comboString2 = comboString2 + ':' + str(value8) + ':' + key8

        print("PRINTING COMBO STRING 2")
        print(comboString2)

        self.newFrame = 'FOD:' +  frame1[0] + ' X ' + frame2[0] + ': NO : 0' + comboString1 + comboString2
        print("PRINTING NEW FRAME")
        print(self.newFrame)

        print("Translated Frame 1 is : ")
        print(self.translatedFrame1)
        print("Translated Frame 2 is : " )
        print(self.translatedFrame2)
        print("Exiting translate operation \n")

        self.fuse(self.translatedFrame1, self.translatedFrame2)

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



    def interpret(self, b, newDirectory):

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