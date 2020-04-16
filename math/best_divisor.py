#!/bin/python3
"""
Best Divisor

Problem: Kristen loves playing with and comparing numbers. She thinks that if she takes 
two different positive numbers, the one whose digits sum to a larger number is better 
than the other. If the sum of digits is equal for both numbers, then she thinks the 
smaller number is better. For example, Kristen thinks that 13 is better than 31 and that 
12 is better than 11.
Given an integer, n, can you find the divisor of n that Kristin will consider to be the 
best?

Input Format
A single integer denoting n.

Constraints
0 < n <= 10e5

Output Format
Print an integer denoting the best divisor of n.

Sample Input
12

Sample Output
6

Explanation
The set of divisors of 12 can be expressed as {1, 2, 3, 4, 6 12}. The divisor whose 
digits sum to the largest number is 6 (which, having only one digit, sums to itself). 
Thus, we print 6 as our answer.
"""
import math
import os
import random
import re
import sys

def getDivisors(n):
    arr = []
    for i in range(1, n+1):
        # Get all divisors
        if (n%i == 0):
            arr.append(i)
    return arr

def sumDigits(n):
    numberStr = str(n)
    result = 0
    for s in numberStr:
        result += int(s)
    return result

def bestDivisor(n):
    divisors = getDivisors(n)
    bestDivisor = 1
    for i in divisors:
        newNumber = sumDigits(i)
        if newNumber == bestDivisor:
            mins = [i, bestDivisor]
            bestDivisor = min(mins)
        elif newNumber > sumDigits(bestDivisor):
            bestDivisor = i
    return bestDivisor

if __name__ == '__main__':
    n = int(input())
    result = bestDivisor(n)
    print(result)