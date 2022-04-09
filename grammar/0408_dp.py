# 탑다운

# 2600 구슬게임

# 한 쪽에 a만큼, 한쪽에 b만큼
# recur = 내가 이기냐 지냐
def recur(a, b):
    # 이기는지 지는지 결과 저장, 처음엔 진다고 가정
    ret = False
    
    if dp[a][b] != -1:
        return dp[a][b]
    
    for i in range(3):
        if a >= arr[i]:
            # 상대방이 이기냐 지냐가 나옴
            # 여기서 False가 나오면 내가 이긴다
            # recur(a - arr[i], b)
            if not recur(a - arr[i], b):        # dp[a - arr[i]][b]와 동치
                ret = True
        
        if b >= arr[i]:
            # recur(a, b - arr[i])
            if not recur(a, b - arr[i]):
                ret = True
                
    dp[a][b] = ret
            
    return ret

arr = list(map(int, input().split()))

# a가 이기냐 지냐는 어느순간부터 일정함
dp = [[-1 for i in range(510)] for j in range(510)]

for _ in range(5):
    a, b = map(int, input().split())
    
    if recur(a, b):
        print('A')
    else:
        print('B')
        
        
## 바텀업
# recur(a, b) 와 dp[a][b]는 동치

'''
recur(a, b) => False
dp[a][b] = False

'''


'''
dp[i]
1. 게임 : i 상황이 되면 이길 수 있는지
2. i번째 수까지만 존재할 떄 최대값, 최소값, 경우의 수
3. i번째 수를 마지막으로 하는 최대값, 최소값, 경우의 수

'''