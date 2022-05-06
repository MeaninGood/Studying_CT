import sys
input = sys.stdin.readline

from collections import deque

n = int(input())

que = deque([i + 1 for i in range(n)])

while 1:
    if len(que) == 1:
        break
    
    que.popleft()
    a = que.popleft()
    que.append(a)

print(que[0])