# N x N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미
# M x M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다
# 죽은 파리의 개수를 구하라
# 각 테스트 케이스의 첫 번째 줄에 N 과 M
# 다음 N 줄에 걸쳐 N x N 배열이 주어짐

'''
n = 배열 n * n
m = 파리채 크기 m * m
그 다음 n * n 배열 주어짐

'''

# T = int(input())
# for t in range(1, T+1):
#     n, m = map(int, input().split())
#     arr = [int(input().split()) + [0] for _ in range(n)]
    
#     s = 0
#     e = m-1
    
#     while e < n:
#         for i in range(n):
#             arr[i][s:e]
            
# [1, 5, 2, 3, 5, 6, 7, 0]
# n = 7
# m = 3
# s = 0
# e = 0
# [1, 5, 2, 3, 5, 6, 7, 0]
#  s
#        e
# total = arr[0]
# while e < n:
#     temp = 0
#     for i in range(2):
#         e += 1
#         total += arr[e]
        
#         if temp > total
        
'''
1. 한 행을 다 돌면 -> 다음 행
각 행 : 가장 겉의 for문
각 열 : 안의 for문

2. 각 행의 개별 값 돌기
각 행 : 1행, 2행 -> 겉의 for문
개별 값 : 1행의 1열과 2열 -> 안의 for문

toal
2중 for문
    temp
        2중 for문 구조
    if 조건문:
        total 저장할 값
        
구조
'''


T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    
    total = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            temp = 0
            for k in range(i, i+m):
                for l in range(j, j+m):
                    temp += arr[k][l]
            if temp > total:
                total = temp
    print(f'#{t} {total}')