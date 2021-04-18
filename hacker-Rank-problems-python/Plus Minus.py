#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr,n):
    positive = 0
    negative = 0 
    neutral = 0
    
    for i in range(n):
        if arr[i]==0:
            neutral += 1
        if arr[i] < 0:
            negative += 1
        if arr [i] > 0:
            positive += 1
    
    print(positive/n) 
    print(negative/n)
    print(neutral/n)      

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr,n)