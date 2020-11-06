
import os
import sys

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar):
    Totalsum = 0
    for i in range(len(ar)):
        Totalsum += ar[i]
    return Totalsum    
    
    #
    # Write your code here.
    #

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
