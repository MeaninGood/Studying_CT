import sys
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]
arr.sort()

d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1

mx = -1000000
for i in d:
    if d[i] > mx:
        mx = d[i]

for i in arr:
    if d[i] == mx:
        print(i)
        
        
'''
for i in d:
    if d[i] == mx:
        print(i)
        break
'''
    
