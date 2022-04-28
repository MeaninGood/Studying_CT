# 12852번_1로 만들기 2

## 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
## 2. X가 2로 나누어 떨어지면, 2로 나눈다.
## 3. 1을 뺀다.
## 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 함
## 연산을 사용하는 횟수의 최솟값을 출력

'''
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 자연수 N
## 첫째 줄에 연산을 하는 횟수의 최솟값을 출력
## 둘째 줄에는 N을 1로 만드는 방법에 포함되어 있는 수를 공백으로 구분해서 순서대로 출력
## 정답이 여러 가지인 경우에는 아무거나 출력

(입력)
10

(출력) 
3
10 9 3 1

'''

import sys
input = sys.stdin.readline

n = int(input())
dp = [-1 for i in range(20)]
dp[1] = 0
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 3
dp[6] = 2

ans = [n]
if n > 6:
    for i in range(6, n + 1):
        if i % 6 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i // 2] + 1)

        elif i % 3 == 0:
            dp[i] = min(dp[i // 3] + 1, dp[i - 1] + 1)

        elif i % 2 == 0:
            dp[i] = min(dp[i // 2] + 1, dp[i - 1] + 1)

        else:
            dp[i] = dp[i - 1] + 1

    print(dp[n])
else:
    print(dp[n])

print(dp)
ans = [n]
tmp = n
while 1:
    if tmp == 1:
        break
    
    if tmp % 6 == 0:
        if dp[tmp // 3] + 1 <= dp[tmp // 2] + 1:
            ans.append(tmp // 3)
            tmp //= 3
        else:
            ans.append(tmp // 2)
            tmp //= 2
            
    elif tmp % 3 == 0:
        if dp[tmp // 3] + 1 <= dp[tmp - 1] + 1:
            ans.append(tmp // 3)
            tmp //= 3
        else:
            ans.append(tmp - 1)
            tmp -= 1
            
    elif tmp % 2 == 0:
        if dp[tmp // 2] + 1 <= dp[tmp - 1] + 1:
            ans.append(tmp // 2)
            tmp //= 2
        else:
            ans.append(tmp - 1)
            tmp -= 1
            
    else:
        ans.append(tmp - 1)
        tmp -= 1
        
print(*ans)