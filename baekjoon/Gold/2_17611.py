import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

sum_arr = [[0, 0] for _ in range(1000010)]

arr = input().split()
x, y = int(arr[0]) + 500000, int(arr[1]) + 500000
startX, startY = x, y

def get_x(sum_arr, x, cur_x):
    if x > cur_x:
        for j in range(cur_x, x):
            sum_arr[j][0] += 1
    else:
        for j in range(x, cur_x):
            sum_arr[j][0] += 1

def get_y(sum_arr, y, cur_y):
    if y > cur_y:
        for j in range(cur_y, y):
            sum_arr[j][1] += 1
    else:
        for j in range(y, cur_y):
            sum_arr[j][1] += 1

for i in range(1, n):
    line = input().split()
    cur_x, cur_y = int(line[0]) + 500000, int(line[1]) + 500000

    if x == cur_x:
        get_y(sum_arr, y, cur_y)
    else:
        get_x(sum_arr, x, cur_x)

    x, y = cur_x, cur_y

if x == startX:
    get_y(sum_arr, y, startY)
else:
    get_x(sum_arr, x, startX)

res = max(max(row) for row in sum_arr)
print(res)
