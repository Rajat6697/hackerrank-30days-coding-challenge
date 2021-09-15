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
    
    sorted_arr= arr
    temp=0
    for i in range(len(arr)-1):
        if sorted_arr[i] > sorted_arr[i+1]:
            temp= arr[i]
            arr[i]= arr[i+1]
            arr[i+1]= temp
    max= sorted_arr[len(arr)-1]
    
    for i in range(len(arr)-1):
        if sorted_arr[i] < sorted_arr[i+1]:
            temp= arr[i]
            arr[i]= arr[i+1]
            arr[i+1]= temp
    min= sorted_arr[len(arr)-1]
    
    sum= 0
    for num in arr:
        sum+= num
    
    max_val= sum- min
    min_val= sum- max
    
    print(min_val, max_val)
    
    
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)




"""
Problem Statement:
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

Example

The minimum sum is  and the maximum sum is . The function prints

16 24
Function Description

Complete the miniMaxSum function in the editor below.

miniMaxSum has the following parameter(s):

arr: an array of  integers
Print

Print two space-separated integers on one line: the minimum sum and the maximum sum of  of  elements.

Input Format

A single line of five space-separated integers.

Constraints


Output Format

Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than a 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
"""