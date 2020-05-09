#!/bin/python3
"""
Combo Meal

Problem: A fast-food chain menu is selling a burger, a can of soda, and a combo meal 
containing a burger and a can of soda, at prices known to you.

They have chosen the selling price for each item by first determining the total cost of 
making the individual items and then adding a fixed value to it, representing their profit. 
Assume that the cost of making a regular burger is fixed and the cost of making a regular 
soda is fixed.

For example, if the cost of making a regular burger is 206, the cost of making a regular 
soda is 145 and the fixed profit is 69, then the fast-food chain will set selling prices as:

            Making cost     Fixed profit    Selling price
Burger          206             69          206+69=275
Soda            145             69          145+69=214
Burger+Soda  206+145=351        69          351+69=420

Given the price of a burger, a can of soda and a combo meal on the menu, your task is to 
compute the fixed profit.

Complete the function named profit which takes in three integers denoting selling price 
of a burger, a can of soda and a combo meal respectively, and returns an integer denoting 
the fixed profit.

Input Format
The first line contains t, the number of scenarios. The following lines describe the 
scenarios.
Each scenario is described by a single line containing three space-separated integers, b,
 s and c, denoting how much a burger, a can of soda and a combo meal cost respectively.

Constraints
1 <= t <= 100
3 <= c <= 2000
2 <= b, s < c
It is guaranteed that the cost of making each item and the profit are positive.

Output Format
For each scenario, print a single line containing a single integer denoting the profit 
that the fast-food chain gets from every purchase. It is guaranteed that the answer is 
positive.

Sample Input
3
275 214 420
6 9 11
199 199 255

Sample Output
69
4
143

Explanation
Case 1: Refer to the problem statement for this case.
Case 2: The selling price of a burger is 6, soda is 9, and combo meal is 11. If the cost 
to make a burger is 2, the cost to make a can of soda is 5 and the fixed profit is 4, you 
can verify the given selling prices as, b=2+4, s=5+4 and c=2+5+4. Hence, the answer is 4.
Case 3: The selling price of a burger is 199, soda is 199, and combo meal is 255. If the 
cost to make a burger is 56, the cost to make a can of soda is 56 and the fixed profit 
is 143, you can verify the given selling prices as, b=56+143, s=56+143 and s=56+56+143. 
Hence, the answer is 143.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the profit function below.
def profit(b, s, c):
    # Return the fixed profit.
    return -1 * (c - b - s)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        bsc = input().split()

        b = int(bsc[0])

        s = int(bsc[1])

        c = int(bsc[2])

        result = profit(b, s, c)

        fptr.write(str(result) + '\n')

    fptr.close()