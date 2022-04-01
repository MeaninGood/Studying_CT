# n, *arr = map(int, input().split())

# def recur(cur, c):
#     ret = 0
    
#     if cur >= n - 1:
#         return ret
    
#     if c < 0:
#         return 100000000

    
#     ret = min(recur(cur + 1, arr[cur] - 1) + 1, recur(cur + 1, c - 1))

#     return ret

# print(recur(0, arr[0]))

'''
def recur(현재위치, 충전량):
   if 도착했으면:
      도착

   if 충전량 0이면:
      return

   recur(cur + 1, 충전)
   recur(cur + 1, 그냥 가기)
        


print(recur(1))
'''

# 현재 위치, 충전량
def recur(cur, c):
    # 초기 리턴 값 0으로 초기화
    ret = 0
    # 가지치기, 충전량이 0 밑으로 떨어지면 바로 아주 큰 값 리턴
    # 가지치기를 먼저 해야 함, 도착했을 때 c == -1이라면 버스기사가 밀어준 것이 되기 때문에
    # 충전량 먼저 적기
    if c < 0:
        return 100000000
    # 기저, 우리가 원하는 도착 상황
    # 충전량을 만족하면서, 도착지점에 도착했을 때
    if cur >= n - 1:
        return ret
    # 인자가 2개이므로 2차원 dp배열 생성
    if dp[cur][c] != -1:
        return dp[cur][c]
    # cur + 1 : 다음칸 봐주기
    # arr[cur] - 1 : 충전량, 다음 칸에서는 1 빠진 충전량으로 계산해야 하므로
    # arr[cur] - 1로 해 줌
    # 충전했을 때는 + 1, 충전 안 했을 때는 그냥 재귀호출하면서원래의 충전량 c - 1
    # ret에 가장 적은 횟수를 저장해 줌
    ret = min(recur(cur + 1, arr[cur] - 1) + 1, recur(cur + 1, c - 1))
    # dp배열에 저장
    dp[cur][c] = ret

    return ret

T = int(input())

for tc in range(1, T + 1):
    n, *arr = map(int, input().split())
    dp = [[-1 for i in range(210)] for j in range(210)]

    print(f'#{tc} {recur(0, arr[0])}')
    
