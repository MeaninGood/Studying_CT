# 11021번_A + B - 7

## 테스트 케이스 개수 T, 각 줄에 A B 주어지며 합 출력
## 합 출력 시 앞에 "Case #1: 합"의 형태로 출력

import sys

T = int(input())

for i in range(T) :
    A, B = map(int, sys.stdin.readline().split())
    print(f'Case #{i+1}: {A+B}')