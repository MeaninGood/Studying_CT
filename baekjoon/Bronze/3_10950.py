# 10950번_A + B - 3

## 테스트 케이스 개수 T, 각 줄에 A B 주어지며 합 출력
import sys

N = int(input())

for i in range(N) :
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)