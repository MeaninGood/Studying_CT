import sys

input = lambda: sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
odd_cnt = 1 if arr[e] % 2 == 1 else 0
even_cnt = 1 if arr[e] % 2 == 0 else 0

while e < n:
    pass