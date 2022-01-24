# 15654번_N과 M (5)

## 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
## N개의 자연수 중에서 M개를 고른 수열

'''
# 첫쨰 줄에 자연수 N과 M이 주어짐
## 한 줄에 하나씩 조건 만족하는 수열 출력.
## 중복 수열을 여러 번 출력하면 안되며, 각 수열은 공백 기준.
## 수열은 사전 순으로 증가하는 순서로 출력

(입력)
4 2
9 8 7 1

(출력)
1 7
1 8
1 9
7 1
7 8
7 9
8 1
8 7
8 9
9 1
9 7
9 8

'''


import sys

# n = 3, m = 5 일 때

m, n = map(int, sys.stdin.readline().split())
idx = list(map(int, sys.stdin.readline().split()))

arr = [ 0 for i in range(n)]
visited = [False for i in range(m)]

def recur(cur) :
    # 종료 조건
    if cur == n :
        return print(*arr)
    
    # 명령어
    
    for i in range(m) :
        if visited[i] :
            continue
    
    


