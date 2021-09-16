#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    birth_dict= {}
    
    for num in candles:
        if num in birth_dict:
            birth_dict[num]+=1
        else:
            birth_dict[num] = 1
    
    sorted_candles= candles
    temp=0
    for i in range(len(candles)-1):
        if sorted_candles[i] > sorted_candles[i+1]:
            temp= sorted_candles[i]
            sorted_candles[i]= sorted_candles[i+1]
            sorted_candles[i+1]= temp
        else:
            continue
    max= sorted_candles[-1]
    
    return birth_dict[max]
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
 

 """
 Problem Statement:
 You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Example


The maximum height candles are  units high. There are  of them, so return .

Function Description

Complete the function birthdayCakeCandles in the editor below.

birthdayCakeCandles has the following parameter(s):

int candles[n]: the candle heights
Returns

int: the number of candles that are tallest
Input Format

The first line contains a single integer, , the size of .
The second line contains  space-separated integers, where each integer  describes the height of .

Constraints

Sample Input 0

4
3 2 1 3
Sample Output 0

2
 """