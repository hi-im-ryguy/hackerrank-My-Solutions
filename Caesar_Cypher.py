#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

_LOWERCASE = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
_UPPERCASE = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def caesarCipher(s, k):
    # Write your code here
    encryptedText = ""
    
    for charIndex in range(0, len(s)):
        dictionaryName = ""
        
        if s[charIndex] in _LOWERCASE:
            dictionaryName = "_LOWERCASE"
        elif s[charIndex] in _UPPERCASE:
            dictionaryName = "_UPPERCASE"
            
        if dictionaryName == "":
            encryptedText += s[charIndex]
            continue
        
        newIndex = (int(eval(dictionaryName).index(s[charIndex])) + k) % len(eval(dictionaryName)) # Get the index of the 
        encryptedText += eval(dictionaryName)[newIndex]
        
    return encryptedText
            
            
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
