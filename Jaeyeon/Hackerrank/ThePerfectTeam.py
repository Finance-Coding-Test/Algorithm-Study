#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'perfectTeam' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING skills as parameter.
#

def perfectTeam(skills):
    # Write your code here
    result=[]
    P_student=skills.count('p')
    C_student=skills.count('c')
    M_student=skills.count('m')
    B_student=skills.count('b')
    Z_student=skills.count('z')
    
    return min(P_student,C_student, M_student,B_student,Z_student)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    skills = input()

    result = perfectTeam(skills)

    fptr.write(str(result) + '\n')

    fptr.close()
