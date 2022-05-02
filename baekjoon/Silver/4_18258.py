import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

que = deque()
for i in range(n):
    tmp = input().split()
    
    if len(tmp) > 1:
        x, y = tmp[0], int(tmp[1])
    else:
        x = tmp[0]
    
    if x == 'push':
        que.append(y)
    
    if x == 'pop':
        if len(que) > 0:
            print(que.popleft())
        else:
            print(-1)
            
    if x == 'size':
        print(len(que))
    
    if x == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
        
    if x == 'front':
        if len(que) > 0:
            print(que[0])
        else:
            print(-1)
    
    if x == 'back':
        if len(que) > 0:
            print(que[-1])
        else:
            print(-1)
        
        