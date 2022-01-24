# 2869번_달팽이는 올라가고 싶다

## 달팽이가 높이 V미터인 나무 막대 올라감
## 낮에 A미터 올라갔다가 밤에 자는 동안 B미터 미끄러짐
## 정상에 올라간 후에는 미끄러지지 않음
## 달팽이가 나무 막대를 모두 올라가려면 며칠이 걸리는지

'''
# 첫쨰 줄에 세 정수 A, B, V가 공백으로 구분되어서 주어짐
## 첫째 줄에 달팽이가 나무 막대를 올라가는데 며칠이 걸리는지 출력

(입력)
2 1 5

(출력)
4

'''


# 문제에서 원하는 코드 (시간제한)==========================

import sys
import math
a, b, v = map(int, sys.stdin.readline().split())
v = v - a
c = 1 + math.ceil(v/(a-b))
print(int(c))




# 정석 ====================================================

import sys
a, b, v = map(int, sys.stdin.readline().split())

day = 1
dis = 0
while 1 :
    if dis >= v :
        break
    
    dis += a    
      
    if dis < v :
        day += 1
    dis -= b
    
print(day)
