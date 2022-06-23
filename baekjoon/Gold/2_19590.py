import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

idx = arr.pop(arr.index(max(arr)))
if sum(arr) <= idx:
    print(idx - sum(arr))
else:
    print(((sum(arr) + idx) % 2))