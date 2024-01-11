import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())

arr = []
for i in range(2, n):
    if i * i > n:
        break

    while n % i == 0:
        arr.append(i)
        n //= i

if n > 1:
    arr.append(n)

print(len(arr))
arr.sort()
print(*arr)
