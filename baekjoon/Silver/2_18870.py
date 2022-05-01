import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

tmp = sorted(list(set(arr)))

d = {}

for idx, i in enumerate(tmp):
    d[i] = idx
    
# print(d)
# ans = list(d)

for i in arr:
    print(d[i], end = ' ')