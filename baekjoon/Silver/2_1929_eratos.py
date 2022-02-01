# 1929번_소수 구하기

## M이상 N이하의 소수를 모두 출력하는 프로그램 작성

'''
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어짐
## 한 줄에 하나씩, 증가하는 순서대로 소수를 출력

(입력)
3 16

(출력)
3
5
7
11
13

'''

import sys

m, n = map(int, sys.stdin.readline().split())


sieve = [True] * (n+1)
sieve[1] = False
i = 2
while i * i <= n :
    if not sieve[i] :
        i += 1
        continue  
    for j in range(i*i, n+1, i) :
        sieve[j] = False   
    i += 1
    
   
for i in range(m, n+1) :
    if sieve[i] :
        print(i)


import sys

m, n = map(int, sys.stdin.readline().split())

i = 2
sieve = [True] * (n + 1)
sieve[1] = False  
for i in range(2, n + 1):
    if i * i > n:
        break
    
    if not sieve[i]:
        continue

    for j in range(i * i, n + 1, i):
        sieve[j] = False
      
for i in range(m, n+1) :
    if sieve[i] :
        print(i)