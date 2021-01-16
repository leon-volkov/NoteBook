# The input data contains sorted unique numeric values. A continuous sequence is a sequence where each value is exactly 1 higher than the previous one, such as 1 2 3 etc. Find minimum and maximum of the longest continuous sequence. If there are multiple longest sequences, output min and max of the first one that was found (i.e. for 1 2 3 5 6 7, output 1 3).
# Input
# Line 1: An integer N for the number of input values.
# Line 2: N input values X separated by space.
# Output
# Line 1: MIN MAX - min and max values separated by space
# Constraints
# 1 <= N <= 100
# -10000 <= X <= 10000
# Example
# Input

# 6
# 1 2 3 4 5 6

# Output

# 1 6


def input()


inn = input().split()
cmi = inn[0]
cma = inn[0]
for i in inn:
    x = int(i)
    if (i - la == 1):
        lo += 1
        cma = i
    else:
        cmi = i
        clo = 0


#

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
xs = []
for i in input().split():
    x = int(i)
    xs.append(x)
cnt = 0
maxcnt = 0
maxc = xs[0]
pidx = -999
for i in xs:
    if pidx == i -1:
        cnt += 1
        pidx = i
        if cnt > maxcnt:
            maxcnt = cnt
            maxc = i
    else:
        cnt = 0
        pidx = i
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("%s %s" % (maxc - maxcnt, maxc))
