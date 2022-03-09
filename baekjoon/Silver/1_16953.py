# 16953번_A->B

## 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지
## 1. 2를 곱한다
## 2. 1을 수의 가장 오른쪽에 추가
## A를 B로 바꾸는데 필요한 연산의 최솟값 구하기

'''
# 첫째 줄에 A, B (1 ≤ A < B ≤ 109)가 주어진
## A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력
## 만들 수 없는 경우에는 -1을 출력

(입력)
2 162

(출력) 
5

'''

import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())

def bfs(a):
    que = deque()
    visited = {} # 필요한 인덱스만 만들기
    cnt = 0
    
    que.append(a)
    visited[a] = True
    
    while len(que) > 0:
        size = len(que)
        cnt += 1
    
        for _ in range(size):
            cur = que[0]
            que.popleft()
            
            if cur == b:
                return cnt
            
            for nxt in [cur*2, (cur*10) + 1]:
                if not nxt <= b or visited.get(nxt, False):
                    continue
                
                que.append(nxt)
                visited[nxt] = True
                
    return -1

print(bfs(a))


# 배열 크기가 과할 정도로 많은데 실제 사용하는 칸 수가 얼마 안 될 때
##### 딕셔너리 쓰기

# visited = {}
# visited[cur] = True
## for -> if 문에서
# visited.get(nxt, False)
##  -> nxt가 딕셔너리에 있으면 그거 반환
## 없으면 False 반환