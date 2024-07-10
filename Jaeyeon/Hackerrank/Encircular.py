#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'doesCircleExist' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY commands as parameter.
#

def doesCircleExist(commands):
    # Write your code here
    result=[]
    for command in commands:
        x,y=0,0
        direction=0
        
        for move in command:
            if move=='G':
                if direction==0:
                    y+=1
                elif direction==1:
                    x+=1
                elif direction==2:
                    y-=1
                elif direction==3:
                    x-=1
            elif move=='L':
                direction=(direction-1)%4
            elif move=='R':
                direction=(direction+1)%4
        if x==0 and y==0 or direction!=0: #direction!=0만 추가했더니 잡혔다...왜...?
            result.append('YES')
        else:
            result.append('NO')
    # for i in range(len(commands)):
    #     if len(commands[i])==1:
    #         if commands[i]=='G':
    #             result.append('NO')
    #         else:
    #             result.append('YES')
    #     else:
    #         #L과 R의 비율이 같지 않으면 무한 루프?
    #         #사실 가는 방향으로 앞밖에 없고 도는 것만 양방향.
    #         if commands[i].count('L')==commands[i].count('R'):
    #             result.append('NO')
    #         else:
    #             result.append('YES')
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    commands_count = int(input().strip())

    commands = []

    for _ in range(commands_count):
        commands_item = input()
        commands.append(commands_item)

    result = doesCircleExist(commands)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
