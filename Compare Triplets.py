#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice_point = 0
    bob_point = 0 
    if a[0] > b[0]:
        alice_point += 1
    if a[1] > b[1]:
        alice_point += 1
    if a[2] > b[2]:
        alice_point += 1 
    if a[0] < b[0]:
        bob_point += 1
    if a[1] < b[1]:
        bob_point += 1
    if a[2] < b[2]:
        bob_point += 1
      
    else:
        alice_point += 0
        bob_point += 0
        
    return (alice_point , bob_point)    
            
        
              

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
