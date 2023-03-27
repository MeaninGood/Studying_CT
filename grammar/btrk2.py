import sys
input = lambda : sys.stdin.readline().strip()


# 차이를 최대로
# n = int(input())
# arr = list(map(int, input().split()))

# visited = [False for _ in range(n)]
# ans = 0
# def recur(cur, tmp):
#     global ans

#     # 기저조건 - 여기서 마무리를 한다, if뭐면 return을 하겠다
#     if cur == n:
#         # print(tmp)
#         total = 0
#         for i in range(1, n):
#             total += abs(tmp[i] - tmp[i - 1])

#         ans = max(ans, total)
#         return
    
#     # 재귀호출
#     for i in range(n):
#         if visited[i]:
#             continue

#         visited[i] = True
#         recur(cur + 1, tmp + [arr[i]])
#         visited[i] = False

# recur(0, [])

# print(ans)
    

# 신기한 소수
# n = int(input())

# # 소수 판정
# def is_prime(x):
#     if x == 1:
#         return False
    
#     for i in range(2, x):
#         if i * i > x:
#             break
        
#         if x % i == 0:
#             return False
            
#     return True


# # 코드 1
# def recur(cur, tmp):
#     if cur == n:
#         print(tmp)
#         return
    
#     for i in range(1, 10):
#         if is_prime(10 * tmp + i):
#             recur(cur + 1, 10 * tmp + i)

# recur(0, 0)


# # 코드 2
# def recur(cur, tmp):
#     # 가지치기 - 잘못 들어갔으면 나간다
#     if not is_prime(tmp):
#         return
    
#     # 기저
#     if cur == n:
#         print(tmp)
#         return
    
#     # 재귀호출
#     for i in range(1, 10):
#         recur(cur + 1, 10 * tmp + i)

# recur(0, 0)



# n-queen

# n = int(input())
# visited = [False for _ in range(n)]


# def check(x):
#     # 어쩌고 저쩌고 조건
#     return True

# def recur(cur, tmp):
#     # 가지치기
#     # 대각선으로 되냐 안 되냐만 잘 체크해주면 끝
#     if check(cur):
#         return

#     if cur == n:
#         return
    
#     for i in range(n):
#         if visited[i]:
#             continue

#         visited[i] = True
#         recur(cur + 1, tmp + [i])
#         visited[i] = False

# recur(0, [])

# # 모든 케이스는 다 봤고 대각선에 겹치는 애들이 있냐 없냐만 잘 봐주면 됨



# 4번 템플릿
# 도영이 문제 3번 템플릿으로 풀어보고, 4번 왜 쓰는지 알려줌
## 3번 템플릿 - 2번 템플릿도 되긴 하는데 시간이 오래 걸림
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# ans = 1 << 60
# 하나만 고르는 것도 보고, 2, 3개 고르는 것 등 길이가 정해져 있지 않음 - length 정하기
# def recur(cur, start, tmp):
#     if cur == length:
#         # ans = min(ans, #계산값)
#         return
    
#     for i in range(start, n):
#         recur(cur + 1, i + 1, tmp + [i])


# 3번 템플릿 응용
# def recur(cur, start, a, b):
#     global ans

#     if cur == length:
#         ans = min(ans, abs(a - b))
#         return
    
#     for i in range(start, n):
#         recur(cur + 1, i + 1, a * arr[i][0], b + arr[i][1])


# for i in range(1, n + 1):
#     length = i
#     # recur(0, 0, [])
#     recur(0, 0, 1, 0)

# print(ans)



## 4번 템플릿
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 1 << 60

def recur(cur, cnt, a, b):
    global ans

    # 몇 개를 고르든 다 보겠다
    if cnt != 0:
        ans = min(ans, abs(a - b))

    # O를 내가 원하는 개수만큼 골랐으면 조기 종료
    # if cnt == length: # 충분히 골랐으면 return하겠다
    #     ans = min(ans, abs(a - b))
    #     return
    
    if cur == n: # 충분히 못 골랐는데 끝까지 왔다
        return
    
    # 반복문이 없으니 cur이 들어감
    # 하나의 함수에서 두개씩 호출
    recur(cur + 1, cnt + 1, a * arr[cur][0], b + arr[cur][1]) # 고르겠다
    recur(cur + 1, cnt, a, b) # 안 고르겠다


# for i in range(1, n + 1):
#     length = i
#     recur(0, 0, 1, 0)

recur(0, 0, 1, 0)


# 4번 몰라도 3번으로도 풀리긴 함
# 근데 4번이 훨씬 더 직관적임.
# 일반적으로 알려주는 이유는 2차원 백트래킹을 풀기 위해
# 이거는 1차원이고
# 퇴사는 쉬우니까 그냥 푸는 걸로


# 소문난 칠공주
# 2번은 bfs, dfs 알아야 하기 때문에 2번 빼고 알려줌

"""
YYYYY   SYSYS   YYYYY   YSYYS   YYYYY
가로세로 인접한다는 신경 안 씀
일차원으로 봐도 됨
아까랑 똑같다는 뜻
저 조건을 만족하는 애들이 몇 개 있는지는 check함수로 구현
모든 케이스를 다 보기만 하면 됨
잘못 연결했다 싶으면 그때 나가면 됨.
"""

arr = [input() for i in range(5)]


def check():
    pass
    # 조건 다 만족하는지 check로 구현하면 됨
    

# 4번 템플릿
def recur(x, y, cnt, scnt):
    
    # if y != 4:
    #     recur(x, y + 1, cnt + 1)
    #     recur(x, y + 1, cnt)

    # else:
    #     recur(x + 1, 0, cnt + 1)
    #     recur(x, y + 1, cnt)
    
    if cnt == 7:
        # if scnt < 4:
            # return
        
        check()
        return
    
    if y == 5:
        x += 1
        y = 0
    
    if x == 5:
        return
    
    # 자바 안 되고 C, C++, 파이썬은 됨
    recur(x, y + 1, cnt + 1, scnt + (arr[x][y] == 'S'))
    recur(x, y + 1, cnt, scnt)
    
recur(0, 0, 0, 0)



# 이차원은 3번 템플릿은 까다로운 경우가 많음
# 그래서 이렇게 이차원으로 풀어야 한다



# 스도쿠
arr = [input() for i in range(9)]


def rect_check(x, y):
    visited = [False for i in range(10)]
    
    for i in range(x + 3):
        for j in range(y + 3):
            if arr[i][j] == '0':
                continue
            
            if visited[int(arr[i][j])]:
                return False
            visited[int(arr[i][j])] = True   

def check():
    # 각 줄마다 중복된 게 있냐 없냐, 카운팅배열
    # 가로줄
    for i in range(9):
        visited = [False for _ in range(10)]
        
        for j in range(9):
            if arr[i][j] == '0':
                continue
            
            if visited[int(arr[i][j])]:
                return False
            
            visited[int(arr[i][j])] = True
            
    # 세로줄, i j만 바꾸면 된다
    for i in range(9):
        visited = [False for _ in range(10)]
    
        for j in range(9):
            if arr[j][i] == '0':
                continue
            
            if visited[int(arr[j][i])]:
                return False
            
            visited[int(arr[j][i])] = True
            
    # 3x3 사각형 체크
    for i in range(3):
        for j in range(3):
            # 한 칸 체크에 이중포문 써야 하는데..
            if not rect_check(3 * i, 3 * j):
                return False
            
    return True


            
            

def recur(x, y):
    # 우리는 가지치기 배웠으니까
    if check():
        return
    
    if y == 9:
        x += 1
        y = 0
        
        # if x == 9:
        #     check()
        #     return
        
        if x == 9:
            for i in range(9):
                print(*arr[i])
            exit()
        
    if arr[x][y] != '0':
        recur(x, y + 1) # 그냥 다음칸으로
        
    # 0이면 1~9 다 넣어봄
    else:
        for i in range(1, 10):
            arr[x][y] = str(i)
            recur(x, y + 1)
            arr[x][y] = '0'
            
recur(0, 0)



## 시간복잡도
"""
1번 템플릿 : 하나의 함수에서 m개 호출 +  n중 중첩 => m^n
m의 n승 - 아무 가지치기가 없다라고 가정하면
2번템플릿 : nPm
3번 템플릿 : nCm

# 가지치기가 들어가면 시간복잡도 계산 따로해야 함
for문 들어가면 n * m^n

"""
