# 11050번_이항 계수 1

## 자연수 N과 정수 K가 주어졌을 때 이항 계수를 구하는 프로그램 작성

'''
# 첫째 줄에 N과 K가 공백을 기준으로 입력됨
## 이항계수 출력

(입력) 5 2
(출력) 10

'''

## 이항계수 : nCk 즉, n! / k!(n-k)!

# 1. for문으로 풀기

import sys

n, k = map(int, sys.stdin.readline().split())

val_1 = 1 # n!을 구해주는 for문
for i in range(1, n+1) :
    val_1 *= i

val_2 = 1 # k!을 구해주는 for문
for j in range(1, k+1) :
    val_2 *= j

val_3 = 1 # (n-k)!을 구해주는 for문   
for l in range(1,n-k+1) :
    val_3 *= l
    
print(val_1//(val_2*val_3)) # 이항계수 식으로 print, 



'''
# 2. factorial 함수 ** 구글링

from math import factorial

n, k = map(int, input().split())
b = factorial(n) // (factorial(k)*factorial(n - k))
print(b)

'''