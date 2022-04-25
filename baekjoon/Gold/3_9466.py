# 9466번_가장 긴 바이토닉 부분 수열

## 프로젝트 팀을 구성하기 위해, 모든 학생들은 프로젝트를 함께하고 싶은 학생을 선택
## (단, 단 한 명만 선택할 수 있다.) 
## 혼자 하고 싶어하는 학생은 자기 자신을 선택하는 것도 가능
## 주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성

'''
# 첫째 줄에 테스트 케이스의 개수 T
# 각 테스트 케이스의 첫 줄에는 학생의 수가 정수 n (2 ≤ n ≤ 100,000)으로 주어짐
# 각 테스트 케이스의 둘째 줄에는 선택된 학생들의 번호가 주어짐
# 모든 학생들은 1부터 n까지 번호가 부여됨
## 각 테스트 케이스마다 한 줄에 출력
## 각 줄에는 프로젝트 팀에 속하지 못한 학생들의 수를 나타내면 됨

(입력)
2
7
3 1 3 7 3 4 6
8
1 2 3 4 5 6 7 8

(출력)
3
0

'''

import sys
input = sys.stdin.readline


# def dfs(cur):
#     global idx
    
#     visited[cur] = True
    
#     for nxt in v[cur]:
#         print(f'#{cur} {nxt} : {idx} ')
#         if nxt == idx:
#             return 1
      
#         if visited[nxt]:
#             continue
        
#         # if prv[cur] == nxt:
#         # visited[nxt] = True
#         if dfs(nxt):
#             return 1
        
#     visited[cur] = False
#     return 0


def dfs(cur, cnt):
    global idx
    
    visited[cur] = True
    
    for nxt in v[cur]:
        # print(f'#{cur} {nxt} : {idx} ')
      
        if visited[nxt]:
            return cnt
        
        # if prv[cur] == nxt:
        # visited[nxt] = True
        ret = dfs(nxt, cnt + 1)
        return ret
        
    visited[cur] = False
    return 0


    

T = int(input())
for tc in range(T):
    n = int(input())
    v = [[] for _ in range(n + 1)]
    arr = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        v[i].append(arr[i])

    # par = [[] for _ in range(n + 1)]

    ans = 0
    idx = 0
    visited = [False for _ in range(n + 1)]
    for k in range(n + 1):
        if not visited[k]:
            ans += dfs(k, 1)
            idx += 1
            # print(ans)

    print(n - ans)
    

'''
1
7
3 1 3 7 3 4 6
'''
