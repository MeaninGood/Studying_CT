'''
# input()

파이썬 내장 함수
input -> 개행 문자 벗기고 -> 문자열로 변환 -> return

# sys.stdin

file object
입력 -> buffer에 저장 -> 읽기





##

nums = []
for line in sys.stdin :
    nums.append(line)

print(nums)

##

< 결과  >

1
2
3
...(중략)
['1\n', '2\n', '3\n'] -> rstrip으로 제거  // nums.append(line.rstirp())




## 한 줄 입력
x, y = sys.stdin.readline().split()

## 여러 줄 입력 # 개행문자 함께 출력됨
import sys
N = int(input())
a= [sys.stdin.readline() for _ in range(N)]

print(a)

## ['1\n', '2\n']





## sys.stdin.readline()
for x in sys.stdin.readline() :
    print(x)

12 3 4 5
    --> 1
        2

        3

        4

        5

## for line in sys.stdin :
    print(line)

1 1
    --> 1 1
2 2
    --> 2 2
5 1
    --> 5 1

## list(map(int, sys.stdin.readline().split()))

## for line in sys.stdin :
    li.append(tuple(map(int, line.strip().split())))

    --> strip()은 인자 값으로 주어진 문자를 기준으로 문자열을 슬라이싱하는 메소드,
        한 줄에 입력된 문자들은 공백이나 특정한 문자 기준으로
        슬라이싱하지 않을 거면 그냥 for문으로 iterating

1 1
2 2
3 3
4 4
    --> [(1, 1), (2, 2), (3, 3), (4, 4)]


## num = sys.stdin.readline(2) --> 1234
print(num) --> 12
'''



# print(sum(map(int, input().split())))
## 입력 : 54321
## 출력 : 15

# import sys
# print(sum(map(int,sys.stdin.readline().split())))
## 입력 : 54321
## 출력 : 54321


import sys

li = []

for i in range(5) :
    li.append(sys.stdin.readline().strip()) # 한 줄 씩 입력받을 때 .strip()
    

print(li)