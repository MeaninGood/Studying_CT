# 1920번_수 찾기

## N개의 정수가 주어졌을 때, 이 안에 X라는 정수가 존재하는지
## 첫째 줄 자연수 N, 다음 줄 N개의 정수 A[1], A[2], ...
## 다음 줄에 M 주어짐
## 다음 줄에 M개의 수들 주어짐, 이 수들이 A안에 존재하는지

N = int(input())
A = set(map(int, input().split()))
M = int(input())
target = list(map(int,input().split()))

for i in range(M) :
    if target[i] in A :
        print("1")
    else :
        print("0")
