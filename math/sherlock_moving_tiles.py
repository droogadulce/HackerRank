#!/bin/python3
"""
Sherlock and Moving Tiles

Problem: Sherlock is given 2 square tiles, initially both of whose sides have length L placed in 
an x-y plane; so that the bottom left corner of each square coincides with the the origin and 
their sides are parallel to the axes.

At t=0, both squares start moving along line y=x (along the positive x and y) with velocities S1 
and S2.

For each query of form qi, Sherlock has to report the time at which the overlapping area of 
tiles is equal to qi.

Note: Assume all distances in meter, time in seconds and velocities in meter per second unless 
otherwise specified.

Input Format
First line contains integers L, S1, S2. Next line contains Q, the number of queries. Each of the 
next Q lines consists of one integer qi in one line.

Constraints
1 <= L, S1, S2 <= 10e9
1 <= Q <= 10e5
1 <= qi <= Le2
S1 != S2

Output Format
For each query, print the required answer in one line. Your answer will be considered correct if 
it is at most 0.0001 away from the true answer. See the explanation for more details.

Sample Input
10 1 2
2
50
100

Sample Output
4.1421
0.0000

Explanation
For the first case, note that the answer is around 4.1421356237..., so any of the following will 
be accepted:
4.1421356237
4.14214
4.14215000
4.1421
4.1422
"""
import os
import sys
import math

#
# Complete the movingTiles function below.
#
def movingTiles(l, s1, s2, queries):
    #
    # Write your code here.
    #
    arr = []
    ss_list = [s1, s2]
    maxVel = max(ss_list)
    minVel = min(ss_list)
    deltaVelocities = maxVel - minVel
    for qi in queries:
        hip = math.sqrt(2*l*l)
        hip_li = math.sqrt(2*qi)
        time = (hip - hip_li) / deltaVelocities
        arr.append(time)
    return arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lS1S2 = input().split()

    l = int(lS1S2[0])

    s1 = int(lS1S2[1])

    s2 = int(lS1S2[2])

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = movingTiles(l, s1, s2, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
