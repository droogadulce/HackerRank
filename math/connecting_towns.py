#!/bin/python3
"""
Problem: Connecting Towns

Gandalf is travelling from Rohan to Rivendell to meet Frodo but there is no direct route from 
Rohan (T1) to Rivendell (Tn). But there are towns T2,T3,T4...Tn-1 such that there are N1 routes 
from Town T1 to T2, and in general, Ni routes from Ti to Ti+1 for i=1 to n-1 and 0 routes for any 
other Ti to Tj for j ≠ i+1

Find the total number of routes Gandalf can take to reach Rivendell from Rohan.

Note
Gandalf has to pass all the towns Ti for i=1 to n-1 in numerical order to reach Tn.
For each Ti, Ti+1 there are only Ni distinct routes Gandalf can take.

Input Format
The first line contains an integer T, T test-cases follow.
Each test-case has 2 lines. The first line contains an integer N (the number of towns).
The second line contains N - 1 space separated integers where the ith integer denotes the number 
of routes, Ni, from the town Ti to Ti+1

Output Format
Total number of routes from T1 to Tn modulo 1234567

Constraints
1 <= T <=1000
2 < N <= 100
1 <= Ni <= 1000

Sample Input
2
3
1 3
4
2 2 2

Sample Output
3
8

Explanation
Case 1: 1 route from T1 to T2, 3 routes from T2 to T3, hence only 3 routes.
T1  T2  T3
      / o
o - o - o
      \ o
Case 2: There are 2 routes from each city to the next, at each city, Gandalf has 2 choices to 
make, hence 2 * 2 * 2 = 8.
"""

import os
import sys

#
# Complete the connectingTowns function below.
#
def connectingTowns(n, routes):
    #
    # Write your code here.
    #
    result = 1
    for i in routes:
        result *= i
    return result % 1234567

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        routes = list(map(int, input().rstrip().split()))

        result = connectingTowns(n, routes)

        fptr.write(str(result) + '\n')

    fptr.close()
