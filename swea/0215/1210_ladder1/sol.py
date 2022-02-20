import sys

sys.stdin = open('input.txt')
t = int(input())

for tc in range(1):
    arr = []
    for _ in range(100):
        arr.append(list(map(int, input().split())))

    arr.reverse()
    # 좌, 우, 하
    dx = [-1, 1, 0]
    dy = [0, 0, -1]

    x = 0
    y = 0
    dir = 0
    for i in range(100):
