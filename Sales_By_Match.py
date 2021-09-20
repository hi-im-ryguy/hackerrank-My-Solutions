#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    ar.sort()
    
    head = 0
    numberOfPairs = 0

    while (head < len(ar)):
        numberOfThisSock = ar.count(ar[head])
        numberOfPairsOfThisSock = math.floor(numberOfThisSock/2)
        numberOfPairs += numberOfPairsOfThisSock
        head += numberOfThisSock
    
    return numberOfPairs
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
