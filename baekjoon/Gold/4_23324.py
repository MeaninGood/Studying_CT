import sys
input = sys.stdin.readline



n, m, k = map(int, input().split())
arr = []
for _ in range(m):
    a, b = map(int, input().split())
    arr.append([a, b, 0])
    
arr[k][-1] = 1
