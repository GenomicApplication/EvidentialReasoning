import re
from collections import Counter
from utils import dprint
from output import *

class Analysis:

    translatedFrame1 = {}
    translatedFrame2 = {}
    newFrame = ''
    b = []
    final_dic = []

    def __init__(self):
        pass

    #adjust the impact based on new evidence
    def discount(self, alpha, mass):
        try:
            print("Entered discount operation")
            file_write('\n')
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
    def translate(self, frame1, frame2, compatibilityRelations,count):
        print("Entered Translate Operation\n")
        dprint("PRINTING FRAMES 1 AND 2")
        dprint(frame1)
        dprint(frame2)

        x = 3
        y = 3

        if count == 1:
            mass = 0
            mass2 = 0

        if count > 1:
            mass = 1
            mass2 = 1

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

                if count == 1:
                    mass = float(mass) + float(value)
                    theta = float(1 - float(mass))

                if count > 1:
                    mass = float(mass) * float(value)
                    theta = float(1- float(mass))

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
                                    print("FOUND A MATCH FOR STRING 1 : " + string + ' in ' + elements)

                                    temp = elements.split('/')
                                    dprint("printing temp")
                                    dprint(temp)

                                    if elements.find('v') != -1:
                                        dprint("Found the v in the string so split , ")

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

                if count == 1:
                    mass2 = float(mass2) + float(value2)
                    theta2 = float(1- mass2)

                if count > 1:
                    mass2 = float(mass2)* float(value2)
                    theta2 = float(1-mass2)

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
                            print("PRINT STRING 2")
                            print(string2)

                            for elements2 in value3:
                                if elements2.find(string2+'/') != -1:
                                    print("FOUND A MATCH FOR STRING 2 : " + string2 + ' in ' + elements2)
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

        file_write('\t{0}\n'.format("Translated Frame"))
        file_write('\t{0}\n\n'.format("____________________________________________________________________________________________________________________"))
        file_write('\t{0:10}{1}\n\n'.format("Frame:", strToMatch1x2))
        file_write('\t{0:105}{1}\n\n'.format("Cross Product Propositions","End Mass"))

        for k,v in self.translatedFrame1.items():
            if k == 'theta':
                file_write('\t{0:105}{1:1.4f}\n'.format(k + " for frame " + frame1[0],v))
            else:
                file_write('\t{0:105}{1:1.4f}\n'.format(k,v))

        for k,v in self.translatedFrame2.items():
            if k =='theta':
                file_write('\t{0:105}{1:1.4f}\n'.format(k + " for frame " + frame2[0],v))
            else:
                file_write('\t{0:105}{1:1.4f}\n'.format(k,v))

        file_write('\n\n')

        self.fuse(self.translatedFrame1, self.translatedFrame2, frame1, frame2)

        return self.translatedFrame1, self.translatedFrame2, self.newFrame


     # Dempster's combination rule
    def fuse(self, translatedFrame1, translatedFrame2):
        print("Entered fuse operation")
        file_write('\n')
        file_write('\tFUSE Operation\n')
        file_write('\t___________________________________\n\n')
        sum1 = []
        sumk = []
        b = []
        Mass1 = []
        Mass2 = []
        file_write('\n')
        file_write('\tOrthogonal Sum begins here for Frame1 and Frame2')
        file_write('\n\n')
        temp1 = []
        temp2 = []
        v1 = 1
        z = 1
        y = ''
        h = 1
        f = ''

        for k, v in (self.translatedFrame1.items()):
            if k == "theta":
                x = (k, float(v))
                Mass1.append(x)
            elif k != 'theta':
                r = (k,float(v))
                temp1.append(r)
        for keys, values in temp1:
            y += keys
            z *= float(values)
        d = (y, float(z))
        Mass1.append(d)
        file_write('\n\n')
        file_write('\tMass1 : {0:}'.format(Mass1))
        file_write('\n')
        v2 = 1
        for k, v in (self.translatedFrame2.items()):
            if k == "theta":
                s = (k, float(v))
                Mass2.append(s)
            elif k != 'theta':
                t = (k,float(v))
                temp2.append(t)
        for keys, values in temp2:
            f += keys
            h *= float(values)
        l = (f, float(h))
        Mass2.append(l)
        file_write('\n\n')
        file_write('\tMass2 : {0:}'.format(Mass2))
        file_write('\n')

        for key, value in Mass1:
            for keys, values in Mass2:
                if key == "theta" and keys == "theta":
                    result = (value * values)
                    file_write('\t{0:}, {1:.4f}\n'.format(keys, result))
                    file_write('both theta')
                    file_write('\n')
                    sum1.append(result)
                    x = (key, result)
                    b.append(x)
                elif key == "theta" and keys != "theta":
                    result = (value * values)
                    file_write('\t{0:}, {1:.4f}\n'.format(keys, result))
                    file_write('one theta')
                    file_write('\n')
                    sum1.append(result)
                    x = (keys, result)
                    b.append(x)
                elif key != "theta" and keys == "theta":
                    result = (value * values)
                    file_write('\t{0:}, {1:.4f}\n'.format(key, result))
                    file_write('one theta')
                    file_write('\n')
                    sum1.append(result)
                    x = (key, result)
                    b.append(x)
                elif keys != "theta" and key != "theta":
                    s1 = (re.split('[,/vU\s]+', key))
                    s2 = (re.split('[,/vU\s]+', keys))
                    if any(set(s1).intersection(s2)):
                        intersect = (set(s1).intersection(s2))
                        intersect = repr(intersect)
                        file_write('\t{0:1}\n'.format(intersect))
                        file_write('\tintersect')
                        file_write('\n')
                        result1 = (value * values)
                        file_write('\t{0:1}, {1:.4f}\n'.format(intersect, result1))
                        file_write('\n')
                        sum1.append(result1)
                        x = (intersect, result1)
                        b.append(x)
                    else:
                        diff = (set(s1).difference(s2))
                        diff = repr(diff)
                        file_write('{0:1}\n'.format(diff))
                        file_write('diff')
                        file_write('\n')
                        result2 = (value * values)
                        file_write('\t{0:1}, {1:2}, {2:.4f}\n'.format(key, keys, result2))
                        file_write('\n')
                        x = ((key, keys), result2)
                        #K = (float(1/1-result2))
                        sumk.append(result2)
                        b.append(x)
        file_write('\tDictionary after orthogonal sum: {0:} '.format(b))
        file_write('\n')
        count = 0
        b1 = dict(b)
        for keys, values in b1.items():
            if "PR" in keys:
                x = (keys, values)
                self.final_dic.append(x)
        #final_dic = repr(final_dic)
        file_write("\tFinal frame dictionary: {0:}".format(self.final_dic))
        #final_dic_values = 0
        final_sum = float(sum(sum1))
        file_write('\n')
        file_write('\n\n')
        k = 0
        for i in sumk:
            k += (i)
        if float(k) == 0.0000:
            file_write('\n')
            massAxB = final_sum
            file_write("\tThe mass of 1 and 2 is : {0:.4f}".format(massAxB))
        elif float(k) != 0:
            K = (1/((1-k)))
            file_write('\n')
            massAxB = float(K) * final_sum
            file_write("\tThe mass of 1 and 2 is : {0:.4f}".format(massAxB))

        file_write('\n\n')
        return b1, self.final_dic

    def interpret(self, crossed_frame, final_dic):
        val = []
        countresult0 = 0
        countresult1 = 0
        countresult2 = 0
        support0 = 0
        plausibility0 = 0
        support1 = 0
        plausibility1 = 0
        support2 = 0
        plausibility2 = 0
        result3 = ()
        result4 = ()
        result5 = ()
        file_write('\n')
        file_write('\tInterpret Operation\n')
        file_write('\t___________________________________\n\n')

        for key,value in crossed_frame.items():
            if 'Q' in key:
                value0 = (value[0])
                result0 = value0[:value0.find('/')]
                props0 = value0[value0.find('/'):]
                s0 = (re.split('[,/vU\s]+', props0))
                value1 = (value[1])
                result1 = value1[:value1.find('/')]
                props1 = value1[value1.find('/'):]
                s1 = (re.split('[,/vU\s]+', props1))
                value2 = (value[2])
                result2 = value2[:value2.find('/')]
                props2 = value2[value2.find('/'):]
                s2 = (re.split('[,/vU\s]+', props2))
        for keys, values in final_dic:
            val.append(values)
        val1 = sum(val)
        for keys, values in final_dic:
            s3 = (re.split('[,vU\s]+', keys))
            #file_write('\t{0:}'.format(s3))
            #file_write('\n\n')
            s3s0 = set()
            s3s1 = set()
            s3s2 = set()
            s3s0len = 1
            s3s1len = 1
            s3s2len = 1
            support = 0
            plausibility = 0
            if set(s3).intersection(s0):
                s3s0.update(set(s3).intersection(s0))
                s3s0len = (len(s3s0))
            elif set(s3).intersection(s1):
                s3s1.update(set(s3).intersection(s1))
                s3s1len = (len(s3s1))
            elif set(s3).intersection(s2):
                s3s2.update(set(s3).intersection(s2))
                s3s2len = (len(s3s2))
            if s3s0len >= s3s1len:
                if s3s0len >= s3s2len:
                    if set(s3).intersection(s0):
                        file_write('\n\n')
                        support += values
                        result0 = value0[:value0.find('/')]
                        file_write('\t{0:}'.format(s3))
                        file_write('\n')
                        file_write('\tThe experimental data has: {0:}'.format(result0))
                        file_write('\n')
                        file_write('\tSupport: {0:.4f}'.format(support))
                        file_write('\n')
                        plausibility = (1 - ((val1-support)))
                        file_write('\tPlausibility: {0:.4f}'.format(plausibility))
                        file_write('\n')
                        countresult0 = countresult0 + 1
                        result3 = repr(result0)
                        support0 += support
                        plausibility0 += plausibility
            elif s3s1len >= s3s0len:
                if s3s1len >= s3s2len:
                    if set(s3).intersection(s1):
                        file_write('\n\n')
                        support += values
                        result1 = value1[:value1.find('/')]
                        file_write('\t{0:}'.format(s3))
                        file_write('\n')
                        file_write('\tThe experimental data has: {0:}'.format(result1))
                        file_write('\n')
                        file_write('\tSupport: {0:.4f}'.format(support))
                        file_write('\n')
                        plausibility = (1 - (val1-support))
                        file_write('\tPlausibility: {0:.4f}'.format(plausibility))
                        file_write('\n')
                        countresult1 = countresult1 + 1
                        result4 = repr(result1)
                        support1 += support
                        plausibility1 += plausibility
            elif s3s2len >= s3s0len:
                if s3s2len >= s3s1len:
                    if set(s3).intersection(s2):
                        file_write('\n\n')
                        support += values
                        result2 = value2[:value2.find('/')]
                        file_write('\t{0:}'.format(s3))
                        file_write('\n')
                        file_write('\tThe experimental data has: {0:}'.format(result2))
                        file_write('\n')
                        file_write('\tSupport: {0:.4f}'.format(support))
                        file_write('\n')
                        plausibility = (1 - (val1-support))
                        file_write('\tPlausibility: {0:.4f}'.format(plausibility))
                        file_write('\n\n')
                        countresult2 = countresult2 + 1
                        result5 = repr(result2)
                        support2 += support
                        plausibility2 += plausibility

        if countresult0 >= countresult1:
            if countresult0 >= countresult2:
                file_write('\tOverall the experiment has: {0:}'.format(result3))
                file_write('\n')
                file_write('\t Support: {0:.4f}'.format(support0))
                file_write('\n')
                file_write('\t Plausibility: {0:.4f}'.format(plausibility0))
                file_write('\n')
                file_write('\tEI = [{0:.4f}, {1:.4f}]'.format(support0, plausibility0))
                file_write('\n\n')
        elif countresult1 >= countresult0:
            if countresult1 >= countresult2:
                file_write('\tOverall the experiment has: {0:}'.format(result4))
                file_write('\n')
                file_write('\t Support: {0:.4f}'.format(support1))
                file_write('\n')
                file_write('\t Plausibility: {0:.4f}'.format(plausibility1))
                file_write('\n')
                file_write('\tEI = [{0:.4f}, {1:.4f}]'.format(support1, plausibility1))
                file_write('\n\n')
        elif countresult2 >= countresult0:
            if countresult2 >= countresult1:
                file_write('\tOverall the experiment has: {0:}'.format(result5))
                file_write('\n')
                file_write('\t Support: {0:.4f}'.format(support2))
                file_write('\n')
                file_write('\t Plausibility: {0:.4f}'.format(plausibility2))
                file_write('\n')
                file_write('\tEI = [{0:.4f}, {1:.4f}]'.format(support2, plausibility2))
                file_write('\n\n')

        file_write('\n\n')

