# 1002번_터렛

## 조규현과 백승환은 각각 자신의 터렛 위치에서 현재 적까지의 거리를 계산
## 조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고,
## 조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때
## 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성

'''
# 첫째 줄에 테스트 케이스의 개수 T, 각 테스트 케이스는 다음과 같이 이루어져 있다.
# 한 줄에 x1, y1, r1, x2, y2, r2가 주어짐
# x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수
# r1, r2는 10,000보다 작거나 같은 자연수
## 각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력
## 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력

(입력)
3
0 0 13 40 0 37
0 0 3 0 7 4
1 1 1 1 1 5

(출력)
2
1
0

'''
T = int(input())

for tc in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
        continue
    
    if x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
        continue

    d = (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** (1 / 2)

    if r1 > r2 and r1 - r2 == d:
        print(1)
        continue
    
    elif r2 > r1 and r2 - r1 == d:
        print(1)
        continue
        
    elif abs(r1 - r2) < d < r1 + r2 :
        print(2)
        continue
        
    elif r1 + r2 == d:
        print(1)
        continue
        
    else:
        print(0)
