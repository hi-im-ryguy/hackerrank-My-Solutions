#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    middle_sum = 0
    
    arr.sort()
    
    for i in range(1, len(arr) - 1):
        middle_sum += arr[i]
        
    minimum_sum = middle_sum + arr[0]
    maximum_sum = middle_sum + arr[len(arr) - 1]
    
    print(f"{minimum_sum} {maximum_sum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
