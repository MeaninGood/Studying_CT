from collections import deque

def bfs():
    que = deque()
    
    for i in range(1, m + 1):
        que.append([v[i], i])
    print(que)
    
    while len(que) > 1:
        cur, idx = que[0][0], que[0][1]
        que.popleft()

        print(que)
        
        if cur != 0:
            cur = cur // 2
            que.append([cur, idx])
            
        
    
    return que[0][1]

T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())
    v = [0] + list(map(int, input().split()))

    print(f'{tc} {bfs()}')