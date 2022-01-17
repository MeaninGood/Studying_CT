# 1978번_소수 찾기

## 주어진 수 N개 중 소수가 몇 개인지 찾아서 출력.

''' 
# 첫 줄에 수의 개수 N이 주어짐, N은 100 이하.
# 다음으로 N개의 수가 주어지는데 수는 1,000이하의 자연수.

## 주어진 수들 중 소수의 개수 출력
'''

'''
(입력)
4
1 3 5 7

(출력)
3
'''

# 약수가 없는 수(소수)를 찾는 것이 목표
# 1. 주어진 수들을 다 돌아서
# 2. 약수가 있을 때를 제외해야 함
# 3. 약수가 없는 숫자만(== 약수가 1과 본인 자신으로 2개만 있는 숫자) 찾기
# 4. 따로 카운트해주기 -> 소수 개수

import sys

n = int(input())
Nli = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in Nli :
    cntx = 0
    if i == 1 :
        continue 
    for j in range(2, i) :
        if i % j == 0 :
            cntx += 1
        
    if cntx == 0 :
        cnt += 1
print(cnt)