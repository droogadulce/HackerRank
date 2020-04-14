#!/bin/python3
"""
Leonardo's Prime Factors

Problem: Leonardo loves primes and created q queries where each query takes the form of an 
integer, n. For each n, he wants you to count the maximum number of unique prime factors of any 
number in the inclusive range [1, n] and then print this value on a new line.
Note: Recall that a prime number is only divisible by 1 and itself, and 1 is not a prime number.

Input Format
The first line contains an integer, q, denoting the number of queries.
Each line i of the q subsequent lines contains a single integer, n.

Constraints
1 <= q <= 10e5
1 <= n <= 10e18

Output Format
For each query, print the maximum number of unique prime factors for any number in the inclusive 
range [1, n] on a new line.

Sample Input
6
1
2
3
500
5000
10000000000
11

Sample Output
0
1
1
4
5
10
2

Explanation
1. The maximum number of unique prime factors of any number in the inclusive range [1, 1] is 0, 
because 1 is not prime and its only factor is itself.
2. The maximum number of unique prime factors of any number in the inclusive range [1, 2] is 1. 
We already know that the number 1 has 0 prime factors, but 2 has 1 prime factor (itself).
3. The maximum number of unique prime factors of any number in the inclusive range [1, 3] is 1. 
The number 3 has 1 prime factor (itself), and we already know that the number 2 has 1 prime 
factor and the number 1 has 0 prime factors.
4. The maximum number of unique prime factors in the inclusive range [1, 500] is 4. The product 
of our first four unique primes is 2x3x5x7 = 210, and there are no additional unique primes we 
can multiply that number by that results in a value <= 500.
"""

import os
import sys

#
# Complete the primeCount function below.
#
def primeCount(n):
    #
    # Write your code here.
    #
    prod = 1
    count = 0
    primes_leq_10e18 = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]
    while prod <= n and count < 16:
        prod *= primes_leq_10e18[count]
        count = count + 1
    return count - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = primeCount(n)

        fptr.write(str(result) + '\n')

    fptr.close()
