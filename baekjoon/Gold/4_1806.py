# 1806번_부분합

## 10,000 이하의 자연수로 이루어진 길이 N짜리 수열
## 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중
## 가장 짧은 것의 길이를 구하는 프로그램을 작성

'''
# 첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)
# 둘째 줄에는 수열
# 수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수
## 첫째 줄에 구하고자 하는 최소의 길이를 출력
## 만일 그러한 합을 만드는 것이 불가능하다면 0을 출력

(입력)
10 15
5 1 3 5 10 7 4 9 2 8

(출력)
2

'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = 0
total = arr[s]
cnt = 0
ans = 1000010
while s <= e:   
        
    if total >= m:
        cnt += 1
        ans = min(ans, e - s + 1)
        total -= arr[s]
        s += 1
    
    elif total < m:
        e += 1
        
        if e >= n :
            break
        
        total += arr[e]
    
    # print(f's는 {s}')
    # print(f'e는 {e}')
    # print(f'합은 {total}')
    # print(f'개수는 {cnt}')
    # print(f'길이는 {ans}')

if cnt == 0:
    print(cnt)
else:
    print(ans)