# 14501번_퇴사

## 오늘부터 N+1일째 되는 날 퇴사, 남은 N일 동안 최대한 많은 상담하기
## 각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와
## 상담을 했을 때 받을 수 있는 금액 Pi
## 상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다
## 또한, N+1일째에는 회사에 없기 때문에, 상담 기간이 넘어간다면 할 수 없다
## 상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하기

'''
# 첫째 줄에 N (1 ≤ N ≤ 15)
# 둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어짐
# 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)
## 첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력

(입력)
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

(출력)
45

'''

dp = [-1 for i in range(150010)]
def recur(cur):
    if cur > n:
        return -10000000
    
    if cur == n:
        return 0
    
    if dp[cur] != -1:
        return dp[cur]
    
    dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
    
    return dp[cur] 

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]

print(recur(0))