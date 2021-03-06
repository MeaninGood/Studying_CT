# 15651번_N과 M (3)

## 자연수 N과 M이 주어졌을 떄, 아래 조건을 만족하는 길이가 M인 수열 모두 구하는 프로그램
## 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
## 같은 수를 여러 번 골라도 됨

'''
# 첫째 줄에 N과 M이 공백 기준으로 주어짐
## 한 줄에 하나씩 문제의 조건을 만족하는 수열 출력.
## 중복되는 수열 여러 번 출력하면 안되며, 공백으로 구분해서 출력
## 수열은 사전 순으로 증가하는 순서로 출력

(입력)
4 2

(출력)
1 1
1 2
1 3
1 4
2 1
2 2
2 3
2 4
3 1
3 2
3 3
3 4
4 1
4 2
4 3
4 4

'''

import sys

m, n = map(int, sys.stdin.readline().split())

# n = 3일 떄, m = 5일 때
arr = [0 for i in range(n)]

def recur(cur, start) : # arr[cur], 시작 조건 주기
    if cur == n : # arr[cur] == arr[n]일 때 print
        return print(*arr)
    
    
    for i in range(m) : # m까지 -> i + 1을 더하므로 1~m까지의 값이 들어감
        arr[cur] = i + 1 # arr[cur] = i + 1이라서 0이 안 들어감
        recur(cur + 1, i + 1) # cur 1증가, i 1 증가 -> 1
        
recur(0, 1)



''' 시잡 코드
m, n = map(int, input().split())

arr = [0 for i in range(n)]
def recur(cur):
    if cur == n:
        print(*arr)
        return

    for i in range(1,m+1):
        arr[cur] = i
        recur(cur + 1)


recur(0)

'''