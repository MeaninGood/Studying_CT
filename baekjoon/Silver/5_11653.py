import sys
input = sys.stdin.readline
n = int(input())

x = n

for i in range(2, n + 1):
    if i * i > n:
        break

    while x % i == 0:
        print(i)
        x //= i

if x != 1:
    print(x)