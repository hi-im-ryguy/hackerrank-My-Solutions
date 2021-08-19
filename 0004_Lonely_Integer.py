#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    
    unique_dictionary = {}
    
    for integer in a:
        try:
            if unique_dictionary[integer] == True:
                unique_dictionary[integer] = False
        except:
            unique_dictionary[integer] = True
        
        # unique_list.pop(integer) if integer in unique_list else unique_list[integer] = 1
    for key, value in unique_dictionary.items():
        if (value == True):
            lonelyinteger = key
    return (lonelyinteger)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
