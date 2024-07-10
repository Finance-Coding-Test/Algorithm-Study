#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'largestSubgrid' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY grid
#  2. INTEGER maxSum
#
#시간 초과=>중간 숫자부터 탐색->binary search 사용

def largestSubgrid(grid, maxSum):
    # Write your code here
    n=len(grid)
    for i in range(n-1,-1,-1):
        sum=0
        answer=0
        for j in range(i+1):
            for k in range(i+1):
                sum+=grid[j][k]
        if sum<=maxSum:
            answer=i+1
            break
    return answer
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    maxSum = int(input().strip())

    result = largestSubgrid(grid, maxSum)

    fptr.write(str(result) + '\n')

    fptr.close()
