'''
    Document Distance - A detailed description is given in the PDF
'''

import math
filename = "stopwords.txt"

def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    list1 = ""
    list2 = ""
    for i in dict1:
        if i not in '!@#$%^&*()_+,.=1234567890':
            if i not in "'":
                list1 = list1+i
    for i in dict2:
        if i not in '!@#$%^&*()_+=1234567890':
            if i not in "'":
                list2 = list2+i
    list1 = list1.split()
    list2 = list2.split()
    list3 = list1 + list2 
    adict = {}
    for word in list3:
       if word not in load_stopwords(filename).keys():
           adict[word]= (list1.count(word),list2.count(word))
    num=0
    add1=0
    add2=0
    for a_check in adict:
        num = num+adict[a_check][0]*adict[a_check][1]
        add1 += adict[a_check][0]**2
        add2 += adict[a_check][1]**2
        den = math.sqrt(add1) * math.sqrt(add2)
    sum1 = num/den
    return sum1                                    

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input().lower
    input2 = input().lower

    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
