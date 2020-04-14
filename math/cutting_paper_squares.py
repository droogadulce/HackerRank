#!/bin/python3
"""
Problem: Cutting Paper Squares
Mary has an nxm piece of paper that she wants to cut into 1x1 pieces according to the following 
rules:
    - She can only cut one piece of paper at a time, meaning she cannot fold the paper or layer 
    already-cut pieces on top of one another.
    - Each cut is a straight line from one side of the paper to the other side of the paper. 
    For example, the diagram below depicts the three possible ways to cut a 3x2 piece of paper:

                                A 3x2 paper
                                 __ __
                                |__|__|
                                |__|__|
                                |__|__|

        Option 1                Option 2            Option 3
         __ __                   __ __               __   __
        |__|__|                 |__|__|             |__| |__|
         __ __                  |__|__|             |__| |__|
        |__|__|                  __ __              |__| |__|
        |__|__|                 |__|__|
    
Given n and m, find and print the minimum number of cuts Mary must make to cut the paper into 
nxm squares that are 1x1 unit in size.

Input Format
A single line of two space-separated integers denoting the respective values of n and m.

Constraints
1 <= n, m <= 10e9

Output Format
Print a long integer denoting the minimum number of cuts needed to cut the entire paper into
1x1 squares.

Sample Input
3 1

Sample Output
2

Explanation
Mary first cuts the 3x1 piece of paper into a 1x1 piece and a 2x1 piece. She then cuts the 2x1 
piece into two 1x1 pieces. Because it took her two cuts to get nxm pieces of size 1x1, we print
2 as our answer.

"""

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(n, m):
    return (n*m) - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    result = solve(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()
