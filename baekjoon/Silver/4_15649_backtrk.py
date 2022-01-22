# 15649번_N과 M (1)

## 자연수 N과 M이 주어졌을 떄, 아래 조건을 만족하는 길이가 M인 수열 모두 구하는 프로그램
## 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열


'''
# 첫째 줄에 N과 M이 공백 기준으로 주어짐
## 한 줄에 하나씩 문제의 조건을 만족하는 수열 출력.
## 중복되는 수열 여러 번 출력하면 안되며, 공백으로 구분해서 출력

(입력)
4 2

(출력)
1 2
1 3
1 4
2 1
2 3
2 4
3 1
3 2
3 4
4 1
4 2
4 3

'''

import sys

n, m = map(int, sys.stdin.readline().split())

arr = [ 0 for i in range(m)]
visited = [False for i in range(n)]

def recur(cur) :
    if cur == m :
        return print(*arr)
    
    for i in range(n) :
        if visited[i] :
            continue
        
        arr[cur] = i+1
        visited[i] = True
        recur(cur + 1)
        visited[i] = False
        
recur(0)