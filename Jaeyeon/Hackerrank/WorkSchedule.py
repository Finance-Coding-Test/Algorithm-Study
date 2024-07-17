
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findSchedules' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER workHours
#  2. INTEGER dayHours
#  3. STRING pattern
#
def findSchedules(workHours, dayHours, pattern):
    from itertools import product
    # Write your code here
    result=[]
    pattern_list=list(pattern)
    work_done=0
    n=pattern_list.count('?')
    for i in range(len(pattern_list)):
        if pattern_list[i]!='?':
            work_done+=int(pattern_list[i])
    more_work=workHours-work_done
    
    def isValidCombination(combination):
        return sum(combination)==more_work and all(0<=x<=dayHours for x in combination)
    
    possible_combination=[
        comb for comb in product(range(dayHours+1),repeat=n) if isValidCombination(comb)
    ]
    
    for comb in possible_combination:
        pattern_copy=pattern_list[:]
        idx=0
        for i in range(len(pattern_copy)):
            if pattern_copy[i]=='?':
                pattern_copy[i]=str(comb[idx])
                idx+=1 
        result.append(''.join(pattern_copy))
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    workHours = int(input().strip())

    dayHours = int(input().strip())

    pattern = input()

    result = findSchedules(workHours, dayHours, pattern)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
