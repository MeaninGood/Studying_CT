# 16756번_Pismo

## N개의 정수로 구성된 배열 A에서 최소값의 간격 찾는 프로그램 작성


'''
# 첫째 줄에는 정수 N
# 둘째 줄에 N개의 정수가 공백을 기준으로 주어짐
## 최소값의 간격 출력

(입력)
2
1 3

3
1 1 1

5
1 2 1 2 1

(출력)
2

0

1
'''

import sys

n  = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))


val = []
for i in range(len(arr)-1) :
    k = arr[i+1] - arr[i]
    val.append(abs(k))

print(min(val))


