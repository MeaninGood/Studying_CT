# 1764번_듣보잡

## 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때
## 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성

'''
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M
# 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름
# N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어짐
# 이름은 띄어쓰기 없이 알파벳 소문자로만 이루어짐, 길이는 20 이하
# N, M은 500,000 이하의 자연수
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지
## 듣보잡의 수와 그 명단을 사전순으로 출력

(입력)
3 4
ohhenrie
charlie
baesangwook
obama
baesangwook
ohhenrie
clinton

(출력)
2
baesangwook
ohhenrie

'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li1 = [input().rstrip() for _ in range(n)]
li2 = [input().rstrip() for _ in range(m)]

d = {}

for i in range(n):
    d[li1[i]] = d.get(li1[i], 0) + 1
    
    
for i in range(m):
    d[li2[i]] = d.get(li2[i], 0) + 1
    
    
cnt = 0
ans = []
for key, value in d.items():
    if value >= 2:
        ans.append(key)
        cnt += 1

ans.sort()
print(cnt)
for i in ans:
    print(i)

