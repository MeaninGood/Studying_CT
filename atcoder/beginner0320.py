# A
# n = int(input())
# arr = input()
# print(arr[n - 1])



# B
'''
S : 전진
R : 시계방향으로 90도 회전 -> left
 
0,0 에서 출발해서 다 거치면 좌표
x  ->
y ^
'''

# n = int(input())
# move = input()


# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]
# x = 0
# y = 0


# d = 0

# for i in range(n):
#     if move[i] == 'S':
#         x = x + dx[d]
#         y = y + dy[d]
#     elif move[i] == 'R':
#         d = (d + 1) % 4
        
# print(x, y)


# C

# n = int(input())
# arr = [i for i in range(2 * n + 2)]
# cnt = 2 * n + 1
# while len(arr) > 0:
#     if len(arr) == 0:
#         break
    
#     for i in range(len(arr))[::-1]:
#             print(arr[i])
#             arr.remove(arr[i])
#             break
        
#     d = int(input())
#     if d in arr:
#         arr.remove(d)
#     elif d not in arr:
#         break



# E

import sys
sys.setrecursionlimit(200000)
n, m, k, s, t, x = map(int, input().split())

arr = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
    
def dfs(cur):
    ret = 0
    if cur == t:
        return ret
    
    for i in range(k):
        for nxt in arr[cur]:
            ret += dfs(nxt)

print(dfs(s))