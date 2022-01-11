# 11720번_숫자의 합

## N개의 숫자가 공백 없이 쓰였을 때 모두 합해서 출력하는 프로그램
## 첫째줄에 N, 둘째 줄에 숫자 N개 공백없이 주어짐
## 근데 첫째줄 N 왜 있음?

N = int(input())
print(sum(map(int, input())))

# import sys

# N = int(input())
# print(sum(map(int, sys.stdin.readline().split())))


'''
# print(sum(map(int, input()))) 결과
## 입력 : 54321
## 출력 : 15

# print(sum(map(int,sys.stdin.readline().split()))) 결과
## 입력 : 54321
## 출력 : 54321

'''
