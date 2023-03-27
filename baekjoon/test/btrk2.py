"""
1번 템플릿 - 순열
000
001
002
003
004
010
...
444

2번 템플릿 - 같은 케이스에서 중복을 제거한 순열
012
021
...

3번 템플릿 - 조합
012
120 x
210 x
013
014
...
410 x
423 ?
"""
# n자리 m진수 출력
# 3자리 5진수 출력

# for i in range(5):
#     for j in range(5):
#         for k in range(5):
#             print(i, j, k)


# 차이를 최대로 - 2번 템플릿
# n = int(input())
# arr = list(map(int, input().split()))

# visited = [False for _ in range(n)]
# ans = 0
# # 20 1 15 8 4 10
# arr2 = []
# def recur(cur, tmp):
#     global ans, arr2
#     # 기저조건
#     if cur == n:
#         total = 0
#         for i in range(1, n):
#             total += abs(tmp[i] - tmp[i - 1])
        
#         ans = max(ans, total)
#         arr2 = tmp
#         return
    
    
#     # 재귀호출
#     for i in range(n):
#         if visited[i]:
#             continue
        
#         visited[i] = True
#         recur(cur + 1, tmp + [arr[i]])
#         visited[i] = False
        
# # recur(0, "")
# recur(0, [])

# print(ans)
# print(arr2)


# # 신기한 소수
# n = int(input())
# """
# 2222
# 2333

# 1번템플릿
# """

# def is_prime(x):
#     if x == 1:
#         return False
    
#     for i in range(2, x):
#         if i * i > x:
#             break
        
#         if x % i == 0:
#             return False
        
#     return True

# def recur(cur, tmp):
#     # 가지치기
#     if not is_prime(tmp):
#         return
    
#     # 기저조건
#     if cur == n:
#         print(tmp)
#         return
    
#     # 재귀호출
#     for i in range(1, 10):
#         # if is_prime(10 * tmp + i):
#         recur(cur + 1, 10 * tmp + i)
        
# recur(0, 0)



# n = int(input())
# visited = [False for _ in range(n)]

# def check():
#     # 대각선으로 갔을 때 만나냐 안 만나냐
#     pass

# def recur(cur, tmp):
#     #가지치기
#     if check():
#         return
    
#     #기저조건
#     if cur == n:
#         return
    
#     #재귀호출
#     for i in range(n):
#         if visited[i]:
#             continue
        
#         visited[i] = True
#         recur(cur + 1, tmp + [i])
#         visited[i] = False
        
# recur(0, [])




# 도영이의 음식
# 3번템플릿 - 왜 4번템플릿 쓰는지
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# ans = 1 << 60
# 기존
# def recur(cur, start, tmp):
#     if cur == length:
#         print(tmp)
#         return
    
#     for i in range(start, n):
#         recur(cur + 1, i + 1, tmp + [i])


# 응용 a: 신맛, b: 쓴맛
# def recur(cur, start, a, b):
#     global ans
#     if cur == length:
#         # ans = min(ans, tmp)
#         # print(tmp)
#         ans = min(ans, abs(a - b))
#         return
    
#     for i in range(start, n):
#         recur(cur + 1, i + 1, a * arr[i][0], b + arr[i][1])
        
# for i in range(1, n + 1):
#     length = i
#     recur(0, 0, [])
#     # recur(0, 0, 1, 0)
    
# print(ans)


# 4번템플릿
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# ans = 1 << 60

# def recur(cur, cnt, a, b):
#     global ans

#     # cnt(고른 음식의 개수) == 0인 경우는 안 봄, cnt가 0이 아닌 경우만 계산
#     # 몇 개를 고르든 0개만 아니면 다 보겠다
#     # 가지치기나 조건 
#     if cnt != 0:
#         ans = min(ans, abs(a - b))
    
#     # 기저조건
#     if cur == n: # 끝까지 오면
#         return
    
#     # 반복문(for문)이 없으니까 cur 넣어줌
#     # 하나의 함수에서 두개씩 호출
#     # 재귀호출 2번 - 고른다 안 고른다
#     recur(cur + 1, cnt + 1, a * arr[cur][0], b + arr[cur][1]) # 고른다
#     recur(cur + 1, cnt, a, b) # 안 고른다

# recur(0, 0, 1, 0)


# # 3번으로 풀리긴 함
# # 4번이 훨씬 더 직관적 - 2차원 백트래킹을 하기 위해

# # 소문난 칠공주
# arr = [list(input()) for _ in range(5)]

# # bfs, dfs알아야 풀 수 있음
# def check():
#     pass

# # cnt = 전부 몇 명 골랐냐, scnt = 이다솜파가 몇 명이냐
# def recur(x, y, cnt, scnt):
#     if cnt == 7:
#         check()
#         return
    
#     if y == 5:
#         x += 1
#         y = 0
        
#     recur(x, y + 1, cnt + 1, scnt + (arr[x][y] == 'S'))
#     recur(x, y + 1, cnt, scnt)
        


"""
시간복잡도

1번 템플릿 : 하나의 함수에서 m개를 호출 + n중 중첩 => m^n (아무런 가지치기 없을 때)
2번 템플릿 : nPm
3번 템플릿 : nCm

# 가지치기가 들어가면 시간복잡도 계산 따로 해줘야함
"""