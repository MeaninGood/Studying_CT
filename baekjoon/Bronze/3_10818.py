# 10818번_최소, 최대

## N개의 정수 주어지면 최솟값과 최댓값 출력
## 첫째줄 N, 둘째 줄 공백 구분 N개의 정수 주어짐

import sys
N = int(input())
num = list(map(int, sys.stdin.readline().split()))

print(min(num), max(num))