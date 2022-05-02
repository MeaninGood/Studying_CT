
import sys
input = sys.stdin.readline

n = int(input())

cnt = [0 for _ in range(10010)]

for i in range(n):
    a = int(input())
    cnt[a] += 1

for i in range(10010):
    for _ in range(cnt[i]):
        print(i)