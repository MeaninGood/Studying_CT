# 15652번_N과 M (4)

## 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하기
## 1부터 N까지 자연수 중에서 M개를 고른 수열
## 같은 수를 여러 번 골라도 됨
## 고른 수열은 비내림차순

'''
# 첫쨰 줄에 자연수 N과 M이 주어짐
## 한 줄에 하나씩 조건 만족하는 수열 출력.
## 중복 수열을 여러 번 출력하면 안되며, 각 수열은 공백 기준.
## 수열은 사전 순으로 증가하는 순서로 출력

(입력)
4 2

(출력)
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4

'''


# n =3 이고 m = 5일 때

import sys
m, n = map(int, sys.stdin.readline().split())

arr = [0 for i in range(n)]
def recur(cur, start) :
    if cur == n :
        # for i in range(n-1) :
        #     if arr[i] <= arr[i+1] : 
        #         return print(*arr)
        return print(*arr)
    
    for i in range(start-1, m) :
        # if arr[0] > arr[1] :
        #     continue
        
        arr[cur] = i + 1
        recur(cur + 1, i + 1)
            
recur(0, 1)