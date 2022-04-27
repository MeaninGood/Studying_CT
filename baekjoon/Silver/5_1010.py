dp = [-1 for i in range(40)]
def fact(cur):
    if cur == 1:
        return 1
    
    if dp[cur] != -1:
        return dp[cur]
    
    dp[cur] = cur * fact(cur - 1)
    return dp[cur]
    

T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    if a == b:
        print(1)
    else:
        print(fact(b) // (fact(b - a) * fact(a)))