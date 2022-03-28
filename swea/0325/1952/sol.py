'''
1일 이용권 : 1일 이용 가능 : 10원
1달 이용권 : 1달 이용 가능, 매달 1일부터 시작 : 40원
3달 이용권 : 연속된 3달 이용 가능, 매달 1일부터 시작 : 100원
1년 이용권 : 1년 이용 가능 : 300원


'''


def dfs(month):

    if month >= 12:
        return 0
    
    if dp[month] != -1:
        return dp[month]
    
    dp[month] = min(dfs(month + 1) + price[0] * plan[month], dfs(month + 1) + price[1], dfs(month+3) + price[2])

    return dp[month]
T = int(input())

for tc in range(1, T+1):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    dp = [-1 for i in range(len(plan) + 1)]
    min_price = price[3]

    a = dfs(0)
    if a > min_price:
        a = min_price
        print(f'#{tc} {a}')
    else:
        print(f'#{tc} {a}')