#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    number_of_positives = 0
    number_of_negatives = 0
    number_of_zeroes = 0
    length = len(arr)
    
    for number in arr:
        if number > 0:
           number_of_positives+=1
        elif number < 0:
            number_of_negatives+=1
        elif number == 0:
            number_of_zeroes+=1
    
    positive_ratio = number_of_positives/length
    negative_ratio = number_of_negatives/length
    zero_ratio = number_of_zeroes/length
    
    print("{0:.6f}".format(positive_ratio))
    print("{0:.6f}".format(negative_ratio))
    print("{0:.6f}".format(zero_ratio))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
