# 14400번_편의점 2

## 고객들이 어느 위치에 존재하는지 파악을 하였고
## 모든 고객들의 거리의 합을 최소로 하려함
## 두 위치의 거리는 |x1-x2|+|y1-y2|로 정의
## n명의 주요 고객들의 위치 (xi,yi)이 주어질 때
## 모든 고객들의 거리 합을 최소로 하는 위치에 편의점을 세울 때, 그 최소 거리 합을 출력

'''
# 첫째 줄에는 주요 고객들의 수n이 주어진다.(1≤n≤100,000)
# 다음 n줄에는 고객들의 위치 (x,y)가 주어진다.(-1,000,000≤x,y≤1,000,000)
## 모든 고객들의 거리 합을 최소로 하는 위치에 편의점을 세울 때, 그 최소 거리 합을 출력

(입력)
5 
2 2
3 4
5 6 
1 9
-2 -8

(출력) 
30

'''

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# nx = set()
# ny = set()
# for i in range(n):
#     nx.add(arr[i][0])
#     ny.add(arr[i][1])
    
# tx = 0
# for i in nx:
#     tx += abs(i)

# ty = 0
# for i in ny:
#     ty += abs(i)

# total = 0
# for x, y in arr:
#     total += abs(x - tx // n)
#     total += abs(y - ty // n)


# tx = 0
# ty = 0
# for x, y in arr:
#     tx += abs(x)
#     ty += abs(y)


# total = 0
# for x, y in arr:
#     total += abs(x - tx // n)
#     total += abs(y - ty // n)
    
    
# print(total)


# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]

# nx = sorted(arr)
# tx = nx[n // 2][0] if n // 2 else nx[(n // 2) - 1][0]

# arr.sort(key=lambda y: y[1])
# ty = arr[n // 2][1] if n // 2 else arr[(n // 2) - 1][1]


# total = 0
# for x, y in arr:
#     total += abs(x - tx)
#     total += abs(y - ty)

# print(total)


import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]

arr.sort()
nx = arr[n // 2][0] if n % 2 else arr[n // 2 - 1][0]

arr.sort(key = lambda x: x[1])
ny = arr[n // 2][1] if n % 2 else arr[n // 2 - 1][1]

total = 0
for x, y in arr:
    total += abs(x - nx) + abs(y - ny)
    
print(total)