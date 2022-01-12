# 5054번_주차의 신

## 첫 번째 줄에 test case 개수 t
## 모든 tc는 두 줄
## 첫째 줄에는 방문할 상점의 수 n
## 둘째 줄에는 상점의 위치
## 상점 다 방문하고 돌아오기 위해 걸어야 하는 거리의 최소값 출력
## 24 13 89 37 -> 152
## 7 30 41 14 39 42 -> 70


'''
sys.stdin.readline() -- 메모리 30860KB, 시간 84ms
'''

import sys

t = int(input()) # 테스트 케이스 개수

for _ in range(t) : # 테스트 케이스 개수만큼 반복
    n = int(input()) # 방문할 상점 수 n
    shop = sorted(map(int, sys.stdin.readline().split())) # 상점 위치

    print((shop[-1] - shop[0])*2)
    # (맨 뒤에 위치한 상점 - 맨 앞에 위치한 상점) * 2


## 뒤에 거에서 앞에 거 빼기 + 맨 마지막에서 앞에 거 빼기
## 더 쉬운 방법 없나,,,
## 입력 13 24 37 89 --> 거리 11, 13, 52, 76 --> 76, 76
## 입력 7 14 30 39 41 42 --> 거리 7, 16, 9, 2, 1, 35 --> 35, 35
## 맨 뒤에서 맨 앞에 거 빼기 * 2


'''
< int(input()) -- 메모리 30860KB, 시간 76ms >

t = int(input()) # 테스트 케이스 개수

for _ in range(t) : # 테스트 케이스 개수만큼 반복
    n = int(input()) # 방문할 상점 수 n
    shop = sorted(map(int, input().split())) # 상점 위치

    print((shop[-1] - shop[0])*2)

'''
