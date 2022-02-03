# 1644번_소수의 연속합

## 하나 이상의 연속된 소수의 합으로 나타낼 수 있는 자연수
## 한 소수는 반드시 한 번만 덧셈에 사용
## 자연수가 주어졌을 때
## 이 자연수를 연속된 소수의 합으로 나타낼 수 있는 경우의 수


'''
# 첫째 줄에 자연수 N
## N을 연속된 소수의 합으로 나타낼 수 있는 경우의 수

(입력)
20 / 41

(출력)
0 / 3

'''

import sys

n = int(sys.stdin.readline())
# 소수 구해줄 에라토스테네스의 체 생성
# 0 ~ n까지의 sieve
sieve = [True] * (n + 1)
# 0, 1은 소수가 아니고, -> 이건 나중에 지워주면 됨
# 2와 3은 이미 소수이므로 True 그대로 둠
# i*i부터 시작할 것이기 때문에 i가 2부터 4 -> 6 -> 8 ...
# 그 다음 i가 3일 때 3 -> 6 -> 9 순으로 지워줄 것임
i = 2

for i in range(2, n+1) : # i는 자동으로 증가함 2부터 n+1까지
    if i * i > n : # i * i가 n을 넘어가면 멈춤
        break
    
    if not sieve[i] : # sieve[i]가 False면
        continue # 맨 처음으로 돌아감 (i 증가)
    
    for j in range(i*i, n + 1 , i) :
        sieve[j] = False # i의 배수를 따라 값들을 False로 바꿔줌
        

arr = [k for k in range(2, n+1) if sieve[k] == True] + [0]

s = 0
e = 0
cnt = 0
total = arr[0]

print(arr)
while e < len(arr)-1 :
    print(arr[s], arr[e])
    print(total)
    print(cnt)

    if total == n :
        cnt += 1
        e += 1
        total += arr[e]
    
    # elif arr[s] == arr[e] :
    #     e += 1
    #     total += arr[e]
    
    elif total < n :
        e += 1
        total += arr[e]
    
    else :
        total -= arr[s]
        s += 1

print(cnt)