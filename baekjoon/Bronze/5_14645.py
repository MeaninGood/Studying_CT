# 14645번_와이버스 부릉부릉

## N개의 정거장을 거친 후 종착역에 도착
## 각 정거장은 내릴 인원수와 올라탈 인원수가 정해져 있다.
## 종착역에 도착하면 버스에 타고 있던 모든 사람이 내린다.

'''
# 첫 줄에 출발역과 종착역을 제외한 정거장의 수 N
# 출발역에서 탑승하는 사람의 수 K
# 둘째 줄부터 N개의 줄에 걸쳐 각 줄마다 i번째 정거장에서 탑승하는 인원 A
## 종착역에 도착했을 때, 버스 운전수의 이름을 출력

(입력)
3 2
10 3
21 8
0 15

(출력)
비와이

'''

n, k = map(int, input().split())

for i in range(n) :
    a, b = input().split()
    
print("비와이")