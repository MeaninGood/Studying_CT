# 1676번_팩토리얼 0의 개수

## N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성

'''
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)
## 첫째 줄에 구한 0의 개수를 출력

(입력)
10

(출력)
3

'''

import sys
input = sys.stdin.readline

n = int(input())

tmp = 1
for i in range(1, n + 1):
    tmp *= i

tmp2 = str(tmp)

ans = 0
for i in range(len(tmp2))[::-1]:
    if tmp2[i] != '0':
        print(ans)
        break
    
    else:
        ans += 1