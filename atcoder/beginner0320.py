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

# import sys
# sys.setrecursionlimit(200000)
# n, m, k, s, t, x = map(int, input().split())

# arr = [[] for i in range(n + 1)]
# for i in range(m):
#     u, v = map(int, input().split())
#     arr[u].append(v)
#     arr[v].append(u)
    
# def dfs(cur):
#     ret = 0
#     if cur == t:
#         return ret
    
#     for i in range(k):
#         for nxt in arr[cur]:
#             ret += dfs(nxt)

# print(dfs(s))

'''
# d
R G B
R G B

R G B
G R B


R G B
G B R
# 세 개가 다 교차돼서 다른 경우
# 세가지 경우 밖에 없음

짝수 번 안에 원래 상태로 돌릴 수 있으면 된다


초기 상태랑 끝상태가 다 같거나
초기 상태랑 끝상태가 다 다르다면 yes




# E

그래프 하나
수열 하나 -> 다 주어지는 건 아닌데, 제일 앞, 제일 뒤 알려줌

K 수열의 길이




'''

# E

import sys
sys.setrecursionlimit(3000)

n, m, k, s, t, x = map(int, input().split())
v = [[] for i in range(n + 1)]
dp = [[[-1 for i in range(2)] for j in range(2010)] for _ in range(2010)]

for i in range(m):
    a, b = map(int, input().split())

    v[a].append(b)
    v[b].append(a)

def dfs(cur, cnt, mod):
    ret = 0

    if cnt == k:
        if cur == t and mod == 0:
            return 1
        else:
            return 0

    if dp[cur][cnt][mod] != -1:
        return dp[cur][cnt][mod]

    for nxt in v[cur]:
        nmod = mod
        if nxt == x:
            nmod += 1

        ret += dfs(nxt, cnt + 1, nmod % 2)
        ret %= 998244353

    dp[cur][cnt][mod] = ret
    return ret

print(dfs(s, 0, 0))