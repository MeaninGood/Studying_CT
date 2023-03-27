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
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 1 << 60
# 하나만 고르는 것도 보고, 2, 3개 고르는 것 등 길이가 정해져 있지 않음 - length 정하기
# def recur(cur, start, tmp):
#     if cur == length:
#         # ans = min(ans, #계산값)
#         return
    
#     for i in range(start, n):
#         recur(cur + 1, i + 1, tmp + [i])


# 3번 템플릿 응용
def recur(cur, start, a, b):
    global ans

    if cur == length:
        ans = min(ans, abs(a - b))
        return
    
    for i in range(start, n):
        recur(cur + 1, i + 1, a * arr[i][0], b + arr[i][1])


for i in range(1, n + 1):
    length = i
    # recur(0, 0, [])
    recur(0, 0, 1, 0)

print(ans)