#!/bin/python3
"""
Restaurant

Problem: Martha is interviewing at Subway. One of the rounds of the interview requires 
her to cut a bread of size lxb into smaller identical pieces such that each piece is a 
square having maximum possible side length with no left over piece of bread.

Input Format
The first line contains an integer T. T lines follow. Each line contains two space 
separated integers l and b which denote length and breadth of the bread.

Constraints
1 <= T <= 1000
1 <= l, b <= 1000

Output Format
T lines, each containing an integer that denotes the number of squares of maximum size, 
when the bread is cut as per the given condition.

Sample Input
2
2 2
6 9

Sample Output
1
6

Explanation
The 1st testcase has a bread whose original dimensions are 2x2, the bread is uncut and 
is a square. Hence the answer is 1.
The 2nd testcase has a bread of size 6x9. We can cut it into 54 squares of size 1x1, 6 
of size 3x3. For other sizes we will have leftovers. Hence, the number of squares of 
maximum size that can be cut is 6.
"""

import os
import sys

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

#
# Complete the restaurant function below.
#
def restaurant(l, b):
    #
    # Write your code here.
    #
    if l == b:
        return 1
    else:
        gcdNum = gcd(l, b)
        return int((l/gcdNum) * (b/gcdNum))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        lb = input().split()
        l = int(lb[0])
        b = int(lb[1])
        result = restaurant(l, b)
        fptr.write(str(result) + '\n')

    fptr.close()
