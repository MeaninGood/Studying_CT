import sys
input = lambda : sys.stdin.readline().strip()


# n = int(input())
# arr = [list(map(int,  input().split())) for _ in range(n)]


# # 퇴사
# # 2^n = 2^15
# # 2^20 = 100만 // 1초 안에 돌아간다
# ans = 0
# def recur(cur, total):
#     global ans
    
#     if cur > n: # 잘못 들어간 경우, 끝이 n일을 초과한 경우
#         return
    
#     if cur == n: # 잘 들어간 경우
#         ans = max(ans, total)
#         return
    
#     # 일을 한다 - 골랐을 때
#     recur(cur + arr[cur][0], total + arr[cur][1])
#     # 일을 안 한다 - 안 골랐을 때
#     recur(cur + 1, total)
    
# recur(0, 0)
# print(ans)
    
# # 2^150만 승 O(n)
# # 앞으로 고르는 것들 주엥서 가장 많은 돈을 리턴
# def recur(cur):
#     # 비정상적인 케이스
#     if cur > n:
#         return -10000000
    
#     # 정상적인 케이스
#     if cur == n:
#         return 0
    
#     # cur + arr[cur][0]을 하면서 뒤로 가서 벌 수 있는 돈 + 지금 벌 수 있는 돈
#     return max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))

# recur(0)

# dp = [-1 for i in range(1500010)]
# def recur(cur):
#     if cur > n:
#         return -10000000
    
#     if cur == n:
#         return 0
    
#     if dp[cur] != -1:
#         return dp[cur]
    
#     dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
#     return dp[cur]
#     # 지금 4: dp[4]
#     # 지금이 5 : dp[cur]
    
# recur(0)
# O(n)

# 메모이제이션
# 1. 처음에 dp테이블 만든다
# 2. 리턴하기 전에 원래 리턴하던 걸 dp테이블에 저장해서 리턴하는 걸로 바꾼다
# 3. 재귀를 돌기 바로 직전에 dp값이 초기값이 아니면 리턴하겠다는 if문

# 1, 2, 3 더하기
# 1. 일단 백트래킹으로 짜
# 2. 하향식 설계로 바꿔
# 3. 리턴하기 전에, dp[cur]에 저장
# 4. dp[cur] != -1 조건 추가

# def recur(cur, total, tmp):
#     global cnt
#     if total > n:
#         return
    
#     if total == n:
#         cnt += 1
#         print(tmp)
#         return
    
#     for i in range(1, 4):
#         recur(cur + 1, total + i, tmp + str(i))
        
# T = int(input())
# for tc in range(T):
#     n = int(input())
#     cnt = 0
#     recur(0, 0, '')
    
#     print(cnt)

# def recur(total):
#     ret = 0
    
#     if total > n: # 1. 경우의 수 구하는 거니까
#         return 0
    
#     if total == n: # 2. n에 도착했을 때
#         return 1 # cnt += 1
    
#     for i in range(1, 4):
#         ret += recur(total + i)
        
#     return ret
        
# T = int(input())
# for tc in range(T):
#     n = int(input())
    
#     print(recur(0))

# dp = [-1 for i in range(1000010)]
# def recur(total):
#     ret = 0
    
#     if total > n: # 1. 경우의 수 구하는 거니까
#         return 0
    
#     if total == n: # 2. n에 도착했을 때
#         return 1 # cnt += 1
    
#     if dp[total] != -1:
#         return dp[total]
    
#     for i in range(1, 4):
#         ret += recur(total + i)
    
#     dp[total] = ret
#     return dp[total]
        
# T = int(input())
# for tc in range(T):
#     n = int(input())
    
#     print(recur(0))

# dp = [-1 for i in range(1000010)]
# def recur(total):
#     ret = 0
    
#     if total < n:
#         return 0
    
#     if total == 0:
#         return 1
    
#     if dp[total] != -1:
#         return dp[total]
    
#     for i in range(1, 4):
#         ret += recur(total - i) # dp[total] total - i
#         # dp[total - 1] + dp[total - 2] + dp[total - 3]
    
#     dp[total] = ret
#     return dp[total]
        
# T = int(input())
# for tc in range(T):
#     n = int(input())
    
#     print(recur(n))
    

# 1, 2, 3더하기 바텀업 코드
# dp = [0 for i in range(1000010)]

# for i in range(4, 1000010):
#     dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

# T = int(input())
# for tc in range(T):
#     n = int(input())
#     print(dp[n])

"""
1	1
2	2 (1+1, 2)
3	4 (1+1+1, 1+2, 2+1, 3)
4	7

1 + dp[3]
2 + dp[2]
3 + dp[1]

dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 3]
"""
n = int(input())
### 제곱수의 합
# 백트래킹 1번 템플릿
ans = 100000
def recur(cur, total, tmp):
    global ans
    
    if total == n:
        ans = min(ans, cur)
        print(tmp)
        return
    
    for i in range(1, n + 1):
        if i * i > n - total:
            break
        
        # 1411
        # 0, 0, ''
        # 1, 1, '1'
        # 2, 1 + 4, '14'
        # 3, 1 + 4 + 1, '141'
        # 4, 1 + 4 + 1 + 1, '1411'
        recur(cur + 1, total + i * i, tmp + str(i * i))

        
recur(0, 0, '')
print(ans)


n = int(input())

def recur(total):
    if total == n:
        return 0
    # 지금 현재 total일 때, 몇개의 제곱수가 더 필요하냐 라는 식으로 설계
    # n에 도착했으면 더이상 제곱수는 필요가 없다
    
    # 그렇지 않으면
    ret = 100000
    for i in range(1, n + 1):
        if i * i > n - total:
            break

        ret = min(ret, recur(total + i * i) + 1)
    return ret

"""
total + i * i만큼의 횟수가 될 텐데
# 이자리에다가 지금 i * i를 넣은 거니까 + 1를 해줌

15 를 만들 거면, 이번 자리에 4를 넣든, 9든

15

1 -  recur(14)
4 -  recur(11)
9 - recur(6)
recur(어쩌고) + 1

"""



# n = int(input())

# dp = [-1 for _ in range(100010)]
# def recur(total):
#     if total == n:
#         return 0
    
#     if dp[total] != -1:
#         return dp[total]

#     ret = 100000
#     for i in range(1, n + 1):
#         if i * i > n - total:
#             break

#         ret = min(ret, recur(total + i * i) + 1)
    
#     dp[total] = ret
#     return dp[total]

# print(recur(0))


### 제곱수의 합 바텀업 코드
n = int(input())
dp = [100000 for _ in range(100010)]

dp[0] = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j * j > i: # i가 16일 때 5by5는 보지 마라
            break 
        
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        
print(dp[n])


"""
DP

백트래킹
시간복잡도를 줄이기 위해 리턴하도록 변형
메모이제이션 적용
-- 무조건 한문제는 푼 거나 마찬가지
-- 1번 문제로 나온다 == 백트래킹 템플릿 안에서 다 풀수 있고
-- 2, 3번으로 나와 == 백트래킹 템플릿 + 메모이제이션(?) 변형만 하면
## 3문제 중에 2솔해서 안전빵은 먹고 들어감

경우의 수를 구해라? => 무조건 DP
최대값을 구해라 => 이진탐색 or DP
누가 이기냐 => 무조건 DP


탑다운을 바텀업으로


웰노운 DP문제들
냅색
가장 긴 증가하는 부분 수열
피보나치
전깃줄
-- 유튜브에 점화식 구하는 것만 백날 설명해 줌


앞으로 공부해야할 DP 이론들
1. 웰노운 모두 풀어보기(필수)
2. DP 역추적(필수)
3. 비트마스킹 DP(카카오)
4. 트리 DP(카카오)
5. 행렬 DP(앞으로 나올수도)


쳐다도 보지 말 것
1. 구사과 블로그 DP 최적화 테크닉 9가지
2. 이름에 "트릭" 붙은 것들

"""