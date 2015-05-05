import re
from collections import Counter
from utils import dprint
from output import *

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
            print("Entered discount operation")
            file_write('\tDiscount Operation\n')
            file_write('\t___________________________________\n\n')
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
        dprint("PRINTING FRAMES 1 AND 2")
        dprint(frame1)
        dprint(frame2)

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
                    dprint("Printing key 1")
                    dprint(key1)
                    dprint("Value :")
                    dprint(value1)

                    if key1 == strToMatch1x2:
                        dprint("Found a match in strToMatch1x2 " + strToMatch1x2 + ' and ' + "key : " + key1)
                        splitter = proposition.split('U')
                        length_of_splitter = len(splitter)
                        i = 0
                        temp_array= []
                        temp_dic = {}
                        comboString = ''

                        dprint("Splitter length: " + str(length_of_splitter))
                        while i < length_of_splitter:
                            string = splitter[i].strip()
                            string = string.split('v')
                            string = string[0].strip()

                            dprint("string is :" + string)

                            for elements in value1:
                                dprint("PRINTING ELEMENTS IN 1")
                                dprint(elements)

                                if elements.find(string) != -1:
                                    dprint("FOUND  a matching proposition")
                                    temp = elements.split('/')
                                    dprint("printing temp")
                                    dprint(temp)

                                    if elements.find('v') != -1:
                                        dprint("Found the v in the string so do not split")

                                        for j in temp[1].split(','):
                                            temp_dic[j.strip()] = 1
                                            dprint("Temp_dic is:")
                                            dprint(temp_dic)
                                    else:
                                        dprint("Did not find 'v'")
                                        dprint("temp[1]:" + temp[1])
                                        prop =  temp[1].split(',')
                                        dprint("PROP is : ")
                                        dprint(prop)

                                        for each in prop:
                                            dprint("Printing each prop in the list")
                                            dprint(each)
                                            temp_dic[each.strip()] = 1
                                            dprint("Temp_dic is:")
                                            dprint(temp_dic)
                            i = i + 1
                            dprint("i: " + str(i))

                        for k,v in temp_dic.items():
                            dprint("PRINTING TEMP DIC 1")
                            dprint(k)
                            temp_array.append(k)
                            dprint("Temp_array is :")
                            dprint(temp_array)

                        temp_array.sort()

                        for item in temp_array:
                            dprint("Item is :")
                            dprint(item)
                            if comboString == '':
                                comboString = item
                                dprint("comboString is empty so comboString is item :" + item)
                            else:
                                comboString = comboString + ',' + item
                                dprint(" comboString isn't empty, here's the new string :")
                                dprint(comboString)
                        finalString =  proposition.strip() + ' v ' + comboString
                        dprint("Final string: " + finalString)
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
                                        prop2 = temp2[1].strip()
                                        temp_dic2[prop2] = 1
                                    else:
                                        prop2 =  temp2[1].split(',')
                                        for each2 in prop2:
                                            temp_dic2[each2.strip()] = 1
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
                        dprint("Final string2: " + finalString2)
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

        file_write('\n\n\n')

        print("Translated frames are: ")
        print(self.translatedFrame1)
        print(self.translatedFrame2)
        print('\n')


        #self.fuse(self.translatedFrame1, self.translatedFrame2)

        return self.translatedFrame1, self.translatedFrame2, self.newFrame



     # Dempster's combination rule
    def fuse(self, massA, massB):
        print("Entered fuse operation")
        sum1 = []
        sumk = []
        print ("\nFrames")
        print ('massA Frame: ', massA)
        print ('massB Frame: ', massB)

        print ('\nOrthogonal Sum begins here for massA and massB:')
        for key, value in massB.items():
            for keys, values in massA.items():
                print(((keys)), ((key)))
                if keys == 'theta' or key == 'theta':
                    result = (value * values)
                    x = (key, result)
                    print ((key, keys), ": %.4f" % result)
                    sum1.append(result)
                    self.b.append(x)
                elif key == "theta" and keys == "theta":
                    result = (value * values)
                    print ((key, keys), ": %.4f" % result)
                    sum1.append(result)
                    x = (key, result)
                    self.b.append(x)
                    self.final_dic.append(x)
                elif key == "theta" and keys != "theta":
                    result = (value * values)
                    print ((key, keys), ": %.4f" % result)
                    sum1.append(result)
                    x = (key, result)
                    self.b.append(x)
                elif key != "theta" and keys == "theta":
                    result = (value * values)
                    print ((key, keys), ": %.4f" % result)
                    sum1.append(result)
                    x = (key, result)
                    self.b.append(x)
                elif keys != "theta" and key != "theta":
                    s1 = (re.split('[,vU\s]+', key))
                    s2 = (re.split('[,vU\s]+', keys))
                    if any(set(s1).intersection(s2)):
                        intersect = (set(s1).intersection(s2))
                        result1 = (value * values)
                        print(intersect, ': %.4f' % result1)
                        sum1.append(result1)
                        x = (key, result1)
                        self.b.append(x)
                    elif set(s1).difference(s2):
                        diff = (set(s1).difference(s2))
                        result2 = (value * values)
                        print(diff, ": %.4f" % result2)
                        sumk.append(result2)
                        x = (key, result2)
                        self.b.append(x)
        print('Dictionary after orthogonal sum: ', self.b)
        count = 0
        for keys, values in self.b:
            if "PR" in keys:
                x = (keys, values)
                self.final_dic.append(x)
        print ("Final frame dictionary: ", self.final_dic)
        sum1 = sum(sum1)
        sum2 = 1
        for i in sumk:
            sum2 *= i
            return sum2
        if sum2 != 0:
            sum3 = (float(1)-(float(sum2)))
            print (sum3)
            if sum3 == 0:
                K = 1
                print ('K = ', K)
                massAxB = K * sum1
                print("The mass of 1 and 2 is : ", (massAxB))
            if sum3 != 0:
                K = float(1)/float(sum3)
                print("K = ", K)
                massAxB = K * sum1
                print("The mass of 1 and 2 is : ", (massAxB))


    def interpret(self, b, crossed_frame, final_dic):
        val = []
        for key, value in crossed_frame.items():
            if 'Q' in key:
                value0 = (value[0])
                print (value0)
                print ('here')
                result0 = value0[:value0.find('/')]
                print ('The experimental data is: ', result0)
                props0 = value0[value0.find('/'):]
                s0 = (re.split('[,/vU\s]+', props0))
                print (s0)
                value1 = (value[1])
                print (value1)
                result1 = value1[:value1.find('/')]
                print ('The experimental data is: ', result1)
                props1 = value1[value1.find('/'):]
                s1 = (re.split('[,/vU\s]+', props1))
                print (s1)
                value2 = (value[2])
                print (value2)
                result2 = value2[:value2.find('/')]
                print ('The experimental data is: ', result2)
                props2 = value2[value2.find('/'):]
                s2 = (re.split('[,/vU\s]+', props2))
        for keys, values in final_dic:
            val.append(values)
        val1 = sum(val)
        for keys, values in final_dic:
            print ('check')
            s3 = (re.split('[,vU\s]+', keys))
            print (s3)
            s3s0 = set()
            s3s1 = set()
            s3s2 = set()
            s3s0len = 1
            s3s1len = 1
            s3s2len = 1
            support = 0
            plausibility = 0
            if set(s3).intersection(s0):
                print ('s3s0')
                print (set(s3).intersection(s0))
                s3s0.update(set(s3).intersection(s0))
                s3s0len = (len(s3s0))
            if set(s3).intersection(s1):
                print ('s3s1')
                print (set(s3).intersection(s1))
                s3s1.update(set(s3).intersection(s1))
                s3s1len = (len(s3s1))
            if set(s3).intersection(s2):
                print ('s3s2')
                print (set(s3).intersection(s2))
                s3s2.update(set(s3).intersection(s2))
                s3s2len = (len(s3s2))
            if s3s0len >= s3s1len:
                if s3s0len >= s3s2len:
                    if set(s3).intersection(s0):
                        print (set(s3).intersection(s0))
                        support += values
                        result0 = value0[:value0.find('/')]
                        print ('The experimental data is: ', result0)
                        print ('Support: %.4f' % support)
                        plausibility = (1 - (val1 - support))
                        print ('Plausibility: ', plausibility)
            elif s3s1len >= s3s0len:
                if s3s1len >= s3s2len:
                    if set(s3).intersection(s1):
                        print (set(s3).intersection(s1))
                        support += values
                        result1 = value1[:value1.find('/')]
                        print ('The experimental data is: ', result1)
                        print ('Support: %.4f' % support)
                        plausibility = (1 - (val1 - support))
                        print ('Plausibility: ', plausibility)
            elif s3s2len >= s3s0len:
                if s3s2len >= s3s1len:
                    if set(s3).intersection(s2):
                        print (set(s3).intersection(s2))
                        support += values
                        result2 = value2[:value2.find('/')]
                        print ('The experimental data is: ', result2)
                        print ('Support: %.4f' % support)
                        plausibility = (1 - (val1 - support))
                        print ('Plausibility: ', plausibility)



