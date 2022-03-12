# 19095번_1, 2, 3 더하기

## 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수 구하기


'''
# 첫째 줄에 테스트 케이스의 개수 T
# 각 테스트 케이스는 한 줄로, 정수 n이 주어짐
# n은 양수이며 11보다 작다.
## 각 테스트 케이스마다, n을 1, 2, 3의 합으로 나타내는 방법의 수를 출력

(입력)
3
4
7
10

(출력)
7
44
274

'''

dp = [-1 for i in range(100010)]
def recur(cur):
    ret = 0
    
    if cur < 0:
        return 0
    
    if cur == 0:
        return 1
    
    if dp[cur] != -1:
        return dp[cur]
    
    for i in range(1, 4):
        ret += recur(cur - i)
        
    dp[cur] = ret
    return ret 
    
t = int(input())
for _ in range(t):
    print(recur(int(input())))
    