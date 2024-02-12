import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

d = {0: 1}
total1, total2 = 0, 0
ans = 0
for i in range(n):
    total1 += arr1[i]
    total2 += arr2[i]
    tmp = total1 - total2
    ans += d.get(tmp, 0)
    d[tmp] = d.get(tmp, 0) + 1
    
print(ans)
    