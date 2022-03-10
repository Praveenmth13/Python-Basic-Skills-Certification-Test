!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def transformSentence(sentence):
    # Write your code here
    words=sentence.split()
    res=""
    for i in words:
        res+=i[0]
        for j in range(1,len(i)):
            if i[j-1].lower()<i[j].lower():
                res+=i[j].upper()
            elif i[j-1].lower()>i[j].lower():
                res+=i[j].lower()
            else:
                res+=i[j]
        res+=" "
    return res[:-1:]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = transformSentence(sentence)

    fptr.write(result + '\n')

    fptr.close()
