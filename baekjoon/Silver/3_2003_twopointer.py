# 2003번_수들의 합 2

## N개의 수로 된 수열 A[1], A[2], …, A[N] 
##  수열의 i번째 수부터 j번째 수까지의 합
## A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수 출력

'''
# 첫째 줄에 N(1 ≤ N ≤ 10,000), M(1 ≤ M ≤ 300,000,000)
# 다음 줄에는 A[1], A[2], …, A[N]이 공백으로 분리되어 주어짐
# 각각의 A[x]는 30,000을 넘지 않는 자연수
## 첫째 줄에 경우의 수를 출력

(입력)
10 5
1 2 3 4 2 5 3 1 1 2

(출력)
3

'''

import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split())) + [0] # 마지막 end 끝내기 위해 [0]하나 추가

s = 0 # start
e = 0 # end
total = arr[0] #  합계 저장해줄 변수
cnt = 0 # 카운트해줄 변수

while e < n : # end가 n보다 작을 때만 while문 돌기
    if total == m : # total이 m과 같으면
        cnt += 1 # 카운트 +1
        e += 1 # end를 뒤로 한 칸 보냄
        total += arr[e] #total에 뒤로 한칸 보낸 e의 값을 추가해줌
        
    elif total < m : # total이 m보다 작으면
        e += 1 # e를 한칸 뒤로 보냄
        total += arr[e] # total에 뒤로 뺀 e 값 더해줌
    
    else :
        total -= arr[s] # total이 m보다 크면 현재의 s값을 먼저 빼고
        s += 1 # s를 뒤로 보냄

print(cnt)

## total이 m보다 작으면 e를 뒤로 보내고 total에 값 더해주기
# total이 m보다 크면 s값을 먼저 빼고 s를 뒤로 보내주기