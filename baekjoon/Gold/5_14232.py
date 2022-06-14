import sys
input = sys.stdin.readline

n = int(input())

x = n
tmp = []
for i in range(2, n + 1):
    if i * i > n:
        break

    while x % i == 0:
        tmp.append(i)
        x //= i

if x != 1:
    tmp.append(x)
    
print(len(tmp))
tmp.sort()
print(*tmp)