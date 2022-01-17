# 15552번_빠른A+B

## A+B를 sys 임포트하여 빠르게 출력하기
# import sys

# N = int(input())

for i in range(N) :
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
