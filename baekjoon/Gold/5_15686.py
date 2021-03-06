# 15686번_치킨 배달

## 크기가 N×N인 도시가 있다. 도시는 1×1크기의 칸으로 나누어져 있다.
## 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나
## 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리
## 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있다
## 도시의 치킨 거리는 모든 집의 치킨 거리의 합
## 임의의 두 칸 (r1, c1)과 (r2, c2) 사이의 거리는 |r1-r2| + |c1-c2|
## 가장 수익을 많이 낼 수 있는  치킨집의 개수는 최대 M개
## 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업하려 할 때
## 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성

'''
# 첫째 줄에 N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)
# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어짐
# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈 칸, 1은 집, 2는 치킨집
# 집의 개수는 2N개를 넘지 않으며, 적어도 1개는 존재
# 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같음
## 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력

(입력)
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

(출력)
5

'''

