#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    numberOfPossibilities = 0
    head = 0
    tail = m
        
    while tail <= len(s):
        sumOfSegments = 0
        for segment in range(head, tail):
            print("Adding: " + str(s[segment]))
            sumOfSegments += s[segment]
            print("Sum so far: " +str(sumOfSegments))
            
        print("Checking if sumOfSegments: " +str(sumOfSegments) +" = day: " +str(d))
        if sumOfSegments == d:
            numberOfPossibilities += 1
            head += 1
            tail += 1
        else:
            head += 1
            tail += 1
            
    return numberOfPossibilities

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
