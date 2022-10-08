import sys

input = lambda : sys.stdin.readline()

arr = [int(input()) for _ in range(10)]

d = {}
mx = 0
idx = 0
for num in arr:
    d[num] = d.get(num, 0) + 1
    if mx < d[num]:
        idx = num
        mx = d[num]

print(sum(arr) // 10)
print(idx)