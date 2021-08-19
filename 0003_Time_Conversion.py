#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    
    time_components = s.split(":")
    
    hour = time_components[0]
    minute = time_components[1]
    seconds = time_components[2]
    
    if "PM" in seconds:
        seconds = seconds.replace("PM", "")
        if hour != "12":
            hour = int(hour) + 12

    elif "AM" in seconds:
        seconds = seconds.replace("AM", "")
        if hour == "12":
            hour = "00"
    
    military_time_format = f"{hour}:{minute}:{seconds}"
    
    return military_time_format

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
