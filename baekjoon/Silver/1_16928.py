# 16928번_뱀과 사다리 게임

## 주사위를 조작해 내가 원하는 수가 나오게 만들 수 있다면, 최소 몇 번만에 도착점에 도착하나
## 주사위의 각 면에는 1부터 6까지 수가 하나씩 적혀있다
## 게임은 크기가 10×10이고, 총 100개의 칸으로 나누어져 있는 보드판에서 진행
## 보드판에는 1부터 100까지 수가 하나씩 순서대로 적혀져 있음
## 플레이어는 주사위를 굴려 나온 수만큼 이동
## 만약 주사위를 굴린 결과가 100번 칸을 넘어간다면 이동할 수 없음
## 도착한 칸이 사다리면, 사다리를 타고 위로 올라감(이동한 칸은 원래 있던 칸의 번호보다 큼)
## 뱀이 있는 칸에 도착하면, 뱀을 따라서 내려가게 됨(이동한 칸은 원래 있던 칸의 번호보다 작아짐)
## 100번 칸에 도착하기 위해 주사위를 굴려야 하는 횟수의 최솟값을 구해보자


'''
# 첫째 줄에 게임판에 있는 사다리의 수 N(1 ≤ N ≤ 15)과 뱀의 수 M(1 ≤ M ≤ 15)
# 둘째 줄부터 N개의 줄에는 사다리의 정보를 의미하는 x, y (x < y)
# x번 칸에 도착하면, y번 칸으로 이동한다는 의미
# 다음 M개의 줄에는 뱀의 정보를 의미하는 u, v (u > v)
# u번 칸에 도착하면, v번 칸으로 이동한다는 의미
# 1번 칸과 100번 칸은 뱀과 사다리의 시작 또는 끝이 아님
# 모든 칸은 최대 하나의 사다리 또는 뱀을 가지고 있으며, 동시에 두 가지를 모두 가지고 있는 경우는 없다.
# 항상 100번 칸에 도착할 수 있는 입력만 주어짐
## 100번 칸에 도착하기 위해 주사위를 최소 몇 번 굴려야 하는지 출력

(입력)
3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17

(출력)
3

'''

# from collections import deque

# def bfs(s):
#     que = deque()
#     visited = [False for i in range(100)]
#     cnt = 0
    
#     que.append(s)
#     visited[s] = True
    
#     while len(que) > 0:
#         size = len(que)
        
#         for _ in range(size):
#             cur = que[0]
#             que.popleft()

#             if cur == 100:
#                 return cnt
            
#             for nxt in range(cur+1, cur+7):
#                 if not (1 <= nxt < 100) or visited[nxt]:
#                     continue
                
#                 que.append(arr[nxt])
#                 visited[nxt] = True
                
#                 if nxt in up:
#                     que.append(up[nxt])
#                     visited[up[nxt]] = True
            
#                 if nxt in down:
#                     que.append(down[nxt])
#                     visited[down[nxt]] = True
                    
#         cnt += 1            
        
                    
# arr = [i for i in range(1, 101)]

# n, m = map(int, input().split())
# up = {}
# down = {}
# for ladder in range(n):
#     x, y = map(int, input().split())
#     up[x] = y

# for snake in range(m):
#     u, v = map(int, input().split())
#     down[u] = v
    
# print(bfs(1))
# print(up)
# print(down)


from collections import deque

def bfs(s):
    que = deque()
    visited = [False for i in range(101)]
    cnt = 0
    
    que.append(s)
    visited[s] = True
    
    while len(que) > 0:
        size = len(que)
        
        for _ in range(size):
            cur = que[0]
            que.popleft()

            if cur == 100:
                return cnt
            
            for nxt in range(cur+1, cur+7):
                if not (1 <= nxt < 101) or visited[nxt]:
                    continue
                
                que.append(arr[nxt])
                visited[nxt] = True
                
                if nxt in move:
                    que.pop()
                    visited[move[nxt]] = True
                    que.append(move[nxt])
            
        cnt += 1          
        
                    
arr = [i for i in range(101)]

n, m = map(int, input().split())
move = {}
for _ in range(n):
    x, y = map(int, input().split())
    move[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    move[u] = v
    
print(bfs(1))