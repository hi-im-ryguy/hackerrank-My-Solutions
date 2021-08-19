#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    absolute_difference = 0

    diagonal_one = 0
    diagonal_two = 0
    
    column = 0
    for row in arr:
        row_size = len(row)
        diagonal_one += row[column]
        diagonal_two += row[row_size - 1 - column]
        column += 1
    
    absolute_difference = abs(diagonal_one - diagonal_two)
    
    return absolute_difference
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
