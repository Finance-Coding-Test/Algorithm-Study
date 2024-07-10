#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'raisingPower' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def raisingPower(arr):
    # Write your code here
    print(arr)
    result=[]
    for i in range(len(arr)-1):
        result.append([i+1,((arr[i])**arr[i+1])%(10**9+7)])
    result.sort(key=lambda x: (-x[1],x[0]))
    print(result)
    return result[0][0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = raisingPower(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
