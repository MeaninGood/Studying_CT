import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
d = {}
for i in range(n):
    tmp = input()
    d[tmp] = d.get(tmp, 0) + 1

answer = 0
for i in range(m):
    tmp = input()
    if d.get(tmp):
        answer += 1
        
print(answer)