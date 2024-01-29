import sys

input = lambda: sys.stdin.readline().strip()

k = int(input())
n = int(input())
aarr = list(map(int, input().split()))
m = int(input())
barr = list(map(int, input().split()))

prefixa = [aarr[0] for _ in range(n)]
d = {aarr[0]: 1}
for i in range(1, n):
    prefixa[i] = prefixa[i - 1] + aarr[i]
    d[prefixa[i]] = d.get(prefixa[i], 0) + 1
    for j in range(i):
        tmp = prefixa[i] - prefixa[j]
        d[tmp] = d.get(tmp, 0) + 1

ans = d.get(k - barr[0], 0)
prefixb = [barr[0] for _ in range(m)]
for i in range(1, m):
    prefixb[i] = prefixb[i - 1] + barr[i]
    ans += d.get(k - prefixb[i], 0)
    for j in range(i):
        tmp = prefixb[i] - prefixb[j]
        ans += d.get(k - tmp, 0)
        
print(ans)