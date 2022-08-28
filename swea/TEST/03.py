"""
1 2 3 4 / 5 6 7
5 6 1 2

7 6 5 4 / 3 2 1


6 1 4 7 2 5 8 3

"""

import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))