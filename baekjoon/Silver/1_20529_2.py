import sys

input = lambda: sys.stdin.readline().strip()
from itertools import combinations


def getDist(a, b):
    total = 0
    for i in range(4):
        if a[i] != b[i]:
            total += 1
            
    return total


tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = list(input().split())
    
    if n >= 33: # n이 33을 넘으면 무조건 3개는 같다
        print(0)
        continue
    
    pick = list(combinations(arr, 3))
    
    res = 1 << 31
    for a, b, c in pick:
        total = 0
        total += getDist(a, b)
        total += getDist(b, c)
        total += getDist(a, c)
        res = min(res, total)
        
    print(res)