# 15650번_N과 M (2)

## 자연수 N과 M이 주어졌을 떄, 아래 조건을 만족하는 길이가 M인 수열 모두 구하는 프로그램
## 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
## 고른 수열은 오름차순이어야 함

'''
# 첫째 줄에 N과 M이 공백 기준으로 주어짐
## 한 줄에 하나씩 문제의 조건을 만족하는 수열 출력.
## 중복되는 수열 여러 번 출력하면 안되며, 공백으로 구분해서 출력
## 수열은 사전 순으로 증가하는 순서로 출력

(입력)
4 2

(출력)
1 2
1 3
1 4
2 3
2 4
3 4

'''




import sys

m, n = map(int, sys.stdin.readline().split())


# n = 3, m = 5 일 때
arr = [ 0 for i in range(n)]
def recur(cur, start) : 
    if cur == n :  # arr[cur]에서 cur이 n과 같아지면 return   
        return print(*arr)
   
    for i in range(start, m+1) : # start부터 m+1까지 순열 생성
          
        arr[cur] = i # arr[0], arr[1], arr[2] ... arr의 인덱스
        recur(cur + 1, i + 1) # cur +1 자리 옆으로 넘김, start를 i+1 바꿔서 오름차순 만들어줌 
        
recur(0, 1)