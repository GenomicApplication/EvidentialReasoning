
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
    def translate(self, frame1, frame2, compatibilityRelations):
        print("Entered Translate Operation\n")

        x = 3
        y = 3

        mass = 0
        mass2 = 0

        theta = 0
        theta2 = 0

        length_ofFrame1 = len(frame1)
        length_ofFrame2 = len(frame2)

        strToMatch1x2 =   frame1[0] + ' X ' + frame2[0]
        strToMatch2x1 =   frame2[0] + ' X ' + frame1[0]

        self.translatedFrame1.clear()
        self.translatedFrame2.clear()

        #Iterate through an unknown length of the Frame 1, and collect all the belief values
        #Finally, record the translated frame in a dictionary
        while x < length_ofFrame1:
            try:
                proposition = frame1[x+1]
                value = float(frame1[x])
                mass = float(mass) + value
                theta = float(1 - mass)

                for key1,value1 in compatibilityRelations.items():
                    if key1 == strToMatch1x2:
                        splitter = proposition.split('U')
                        length_of_splitter = len(splitter)
                        i = 0
                        temp_array= []
                        temp_dic = {}
                        comboString = ''

                        while i < length_of_splitter:
                            string = splitter[i].strip()

                            for elements in value1:
                                if elements.find(string) != -1:
                                    temp = elements.split('/')

                                    if elements.find('v') != -1:
                                        prop = temp[1]
                                        temp_dic[prop] = 1
                                    else:
                                        prop =  temp[1].split(',')
                                        for each in prop:
                                            temp_dic[each] = 1
                            i = i + 1

                        for k,v in temp_dic.items():
                            temp_array.append(k)
                            temp_array.sort()

                        for item in temp_array:
                            if comboString == '':
                                comboString = item
                            else:
                                comboString = comboString + ',' + item
                        finalString =  proposition.strip() + ' v ' + comboString
                        self.translatedFrame1[finalString] = value
                        self.translatedFrame1["theta"] = theta
                x = x + 2

            except:
                break


        #Iterate through an unknown length of Frame 2 and collect all the belief values.
        #Then, record the translated frame in a dictionary
        while y < length_ofFrame2:
            try:
                proposition2 = frame2[y + 1]
                value2 = float(frame2[y])
                mass2 = float(mass2) + value2
                theta2 = float(1 - mass2)

                for key2,value3 in compatibilityRelations.items():
                    if key2 == strToMatch2x1:
                        splitter2 = proposition2.split('U')
                        length_of_splitter2 = len(splitter2)
                        l = 0
                        temp_array2= []
                        temp_dic2 = {}
                        comboString2 = ''

                        while l < length_of_splitter2:
                            string2 = splitter2[l].strip()

                            for elements2 in value3:
                                if elements2.find(string2) != -1:
                                    temp2 = elements2.split('/')

                                    if elements2.find('v') != -1:
                                        prop2 = temp2[1]
                                        temp_dic2[prop2] = 1
                                    else:
                                        prop2 =  temp2[1].split(',')
                                        for each2 in prop2:
                                            temp_dic2[each2] = 1
                            l = l + 1

                        for k2,v2 in temp_dic2.items():
                            temp_array2.append(k2)
                            temp_array2.sort()

                        for item2 in temp_array2:
                            if comboString2 == '':
                                comboString2 = item2
                            else:
                                comboString2 = comboString2 + ',' + item2
                        finalString2 =  proposition2.strip() + ' v ' + comboString2
                        self.translatedFrame2[finalString2] = value2
                        self.translatedFrame2["theta"] = theta2
                y = y + 2

            except:
                break

        propForNewFrame1 = ''
        propForNewFrame2 = ''

        for key4,value4 in self.translatedFrame1.items():
            if key4 != 'theta':
                if propForNewFrame1 == '':
                    propForNewFrame1 = str(value4) + ':' + key4
                else:
                    propForNewFrame1 = str(value4) + ':' + key4 + ':' + propForNewFrame1

        for key5,value5 in self.translatedFrame2.items():
            if key5 != 'theta':
                if propForNewFrame2 == '':
                    propForNewFrame2 = str(value5) + ':' + key5
                else:
                    propForNewFrame2 = str(value5) + ':' + key5 + ':' + propForNewFrame2

        self.newFrame = 'FOD:' + strToMatch1x2 + ':NO: 0:' + propForNewFrame1 + ':' + propForNewFrame2

        print("Translated frames are: ")
        print(self.translatedFrame1)
        print(self.translatedFrame2)

        self.fuse(self.translatedFrame1, self.translatedFrame2)

        return self.translatedFrame1, self.translatedFrame2, self.newFrame



    # Dempster's combination rule
    def fuse(self, massA, massB):
        print("Entered fuse operation")
        i = 0
        a = 0
        sum1 = []
        sumk = []

        for key, value in massB.items():
            for keys, values in massA.items():
                print(((keys)), ((key)))
                if keys == 'theta' or key == 'theta':
                    result = (value * values)
                    print("%.4f" % result)
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
                        result1 = (value * values)
                        print("%.4f" % result1)
                        sum1.append(result1)
                        x = (key, result1)
                        self.b.append(x)
                        break
                    else:
                        print("No Match")
                        result2 = (1 - (value * values))
                        print("%.4f" % result2)
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
            print("The mass of 1 and 2 is : %.4f" % (m1x2))
        else:
            m1x2 = sum1
            print("The mass of 1 and 2 is : %.4f" % (m1x2))



    def interpret(self, b, crossed_frame):
        #for line in crossed_frame:
            #if 'Q' in line:
        val = []
        for keys,values in b:
            val.append(values)
        val = sum(val)
        for key, value in crossed_frame.items():
            if 'Q' in key:
                value1 = (value[0])
                s1 = set(value1.split(' '))
                for keys, values in b:
                    if 'PR' in keys:
                        print (keys)
                        s2 = set(keys.split(' '))
                        counter = (Counter(keys) in b)
                        print (keys)
                        print (values)
                        if counter == True:
                            print ('sum all')
                            support = sum(values)
                            print ("Support : %.4f" % support)
                            plausibility = abs((1-((val)-values)))
                            print ("Plausibility: %.4f" % plausibility)
                            EI = ["%.4f" % support, "%.4f" % plausibility]
                            print ("EI:", EI)
                        else:
                            support = values
                            print ("Support : %.4f" % support)
                            plausibility = abs((1-((val)-values)))
                            print ("Plausibility: %.4f" % plausibility)
                            EI = ["%.4f" % support, "%.4f" % plausibility]
                            print ("EI:", EI)
                        if any(s1.intersection(s2)):
                            value = value1[:value1.find('/')]
                            print (value)
                        elif any(s1.difference(s2)):
                            for key, value in crossed_frame.items():
                                if 'Q' in key:
                                    value1 = (value[1])
                                    s1 = set(value1.split(' '))
                                    for keys, values in b:
                                        if 'PR' in keys:
                                            print (keys)
                                            s2 = set(keys.split(' '))
                                            counter = (Counter(keys) in b)
                                            print (keys)
                                            print (values)
                                            if counter == True:
                                                print ('sum all')
                                                support = sum(values)
                                                print ("Support : %.4f" % support)
                                                plausibility = abs((1-((val)-values)))
                                                print ("Plausibility: %.4f" % plausibility)
                                                EI = ["%.4f" % support, "%.4f" % plausibility]
                                                print ("EI:", EI)
                                            else:
                                                support = values
                                                print ("Support : %.4f" % support)
                                                plausibility = abs((1-((val)-values)))
                                                print ("Plausibility: %.4f" % plausibility)
                                                EI = ["%.4f" % support, "%.4f" % plausibility]
                                                print ("EI:", EI)
                                            if any(s1.intersection(s2)):
                                                value = value1[:value1.find('/')]
                                                print (value)
                                            elif any(s1.intersection.s2):
                                                for key, value in crossed_frame.items():
                                                    if 'Q' in key:
                                                        value1 = (value[2])
                                                        s1 = set(value1.split(' '))
                                                        for keys, values in b:
                                                            if 'PR' in keys:
                                                                print (keys)
                                                                s2 = set(keys.split(' '))
                                                                counter = (Counter(keys) in b)
                                                                print (keys)
                                                                print (values)
                                                                if counter == True:
                                                                    print ('sum all')
                                                                    support = sum(values)
                                                                    print ("Support : %.4f" % support)
                                                                    plausibility = abs((1-((val)-values)))
                                                                    print ("Plausibility: %.4f" % plausibility)
                                                                    EI = ["%.4f" % support, "%.4f" % plausibility]
                                                                    print ("EI:", EI)
                                                                else:
                                                                    support = values
                                                                    print ("Support : %.4f" % support)
                                                                    plausibility = abs((1-((val)-values)))
                                                                    print ("Plausibility: %.4f" % plausibility)
                                                                    EI = ["%.4f" % support, "%.4f" % plausibility]
                                                                    print ("EI:", EI)
                                                                if any(s1.intersection(s2)):
                                                                    value = value1[:value1.find('/')]
                                                                    print (value)



