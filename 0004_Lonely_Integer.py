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
    
    unique_list = []
    
    for integer in a:
        if integer in unique_list:
            unique_list.remove(integer)
        else:
            unique_list.append(integer)
        
        # unique_list.pop(integer) if integer in unique_list else unique_list[integer] = 1
        
    
    return unique_list[0]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
