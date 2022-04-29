# 1485번_정사각형

## 네 점을 이용해 정사각형을 만들 수 있는지 없는지 출력

'''
# 첫째 줄에 테스트 케이스의 개수 T
# 각 테스트 케이스는 네 줄로 이루어져 있으며, 점의 좌표가 한 줄에 하나씩 주어짐
# 점의 좌표는 -100,000보다 크거나 같고, 100,000보다 작거나 같은 정수
# 같은 점이 두 번 이상 주어지지 않는다
## 각 테스트 케이스마다 입력으로 주어진 네 점을 이용해서 정사각형을 만들 수 있으면 1을, 없으면 0을 출력

(입력)
2
1 1
1 2
2 1
2 2
2 2
3 3
4 4
5 5

(출력)
1
0

'''

import sys
input = sys.stdin.readline

# def is_square(arr):
#     tmp = arr[0]
#     for i in range(1, 4):
#         if tmp == arr[i]:
#             return True
#     return False


T = int(input())
    
for tc in range(T):
    x = {}
    y = {}
    for i in range(4):
        a, b = map(int, input().split())
        x[a] = x.get(a, 0) + 1
        y[b] = y.get(b, 0) + 1
    
    print(x)
    print(y)