# 1647번_도시 분할 계획

## 개의 집과 그 집들을 연결하는 M개의 길, 두 개의 분리된 마을로 분할할 계획
## 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할
## 각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다는 뜻
## 마을에는 집이 하나 이상 있어야 함
## 일단 분리된 두 마을 사이에 있는 길들은 필요가 없으므로 없앨 수 있음
## 그리고 각 분리된 마을 안에서도 임의의 두 집 사이에 경로가 항상 존재하게 하면서 길을 더 없앨 수 있음
## 마을의 이장은 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하고 싶음


'''
# 첫째 줄에 집의 개수 N, 길의 개수 M
# N은 2이상 100,000이하인 정수이고, M은 1이상 1,000,000이하인 정수
# 그 다음 줄부터 M줄에 걸쳐 길의 정보가 A B C 세 개의 정수
# A번 집과 B번 집을 연결하는 길의 유지비가 C (1 ≤ C ≤ 1,000)라는 뜻
## 첫째 줄에 없애고 남은 길 유지비의 합의 최솟값을 출력

(입력)
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

(출력)
8

'''

import sys
input = sys.stdin.readline


def find_(x):
    if par[x] == x:
        return x
    return find_(par[x])


def union_(a, b):
    a, b = find_(a), find_(b)
    
    if a == b:
        return
    
    if rnk[a] > rnk[b]:
        par[b] = a
        
    elif rnk[a] < rnk[b]:
        par[a] = b
        
    else:
        par[a] = b
        rnk[b] += 1
        

n, m = map(int, input().split())
v = []

for _ in range(m):
    a, b, c = map(int, input().split())
    v.append([a, b, c])

v.sort(key = lambda x: x[2])


rnk = [0 for i in range(n + 1)]
par = [i for i in range(n + 1)]
total = 0
cnt = 0
for i in range(m):
    a, b, c = v[i]
    
    a = find_(a)
    b = find_(b)
    
    if a == b:
        continue
    
    union_(a, b)
    cnt += 1
    total += c
    
    if cnt == n - 2:
        break
    
print(total)