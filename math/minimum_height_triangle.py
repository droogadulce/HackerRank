#!/bin/python3
"""
Minimum Height Triangle

Problem: Given integers b and a, find the smallest integer h, such that there exists a triangle 
of height h, base b, having an area of at least a.

Input Format
In the first and only line, there are two space-separated integers b and a, denoting respectively 
the base of a triangle and the desired minimum area.

Constraints
1 <= b <= 10e6
1 <= a <= 10e6

Output Format
In a single line, print a single integer h, denoting the minimum height of a triangle with base b 
and area at least a.

Sample Input 0
2 2

Sample Output 0
2

Explanation 0
The task is to find the smallest integer height of the triangle with base 2 and area at least 2. 
It turns out, that there are triangles with height 2, base 2 and area 2, for example a triangle 
with corners in the following points: (1, 1), (3, 1), (1, 3).
It can be proved that there is no triangle with integer height smaller than 2, base 2 and area 
at least 2.

Sample Input 1
17 100

Sample Output 1
12

Explanation 1
The task is to find the smallest integer height of the triangle with base 17 and area at least 100. 
It turns out, that there are triangles with height 12, base 17 and area 102, for example a 
triangle with corners in the following points: (2, 2), (19, 2), (16, 14).
It can be proved that there is no triangle with integer height smaller than 12, base 17 and area 
at least 100.
"""

import sys
import math

def lowestTriangle(base, area):
    # Complete this function
    return int(math.ceil((2*area)/base))

base, area = input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)