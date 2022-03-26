# 11659번_구간 합 구하기 4

## 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성



'''
# 첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M
# 둘째 줄에는 N개의 수가 주어짐
# 수는 1,000보다 작거나 같은 자연수
# 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어짐
## 총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력

(입력)
5 3
5 4 3 2 1
1 3
2 4
5 5

(출력)
12
9
1

'''

import sys
si = sys.stdin.readline

n, m = map(int, si().split())
arr = [0] + list(map(int, si().split()))
prefix = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    prefix[i] = prefix[i - 1] + arr[i]
    
for _ in range(m):
    a, b = map(int, si().split())
    
    print(prefix[b] - prefix[a - 1])