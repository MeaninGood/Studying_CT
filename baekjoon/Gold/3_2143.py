import sys

input = lambda: sys.stdin.readline().strip()

k = int(input())
n = int(input())
aarr = list(map(int, input().split()))
m = int(input())
barr = list(map(int, input().split()))

prefixa = [aarr[0] for _ in range(n)]
ad = {aarr[0]: 1}
for i in range(1, n):
    prefixa[i] = prefixa[i - 1] + aarr[i]
    ad[prefixa[i]] = ad.get(prefixa[i], 0) + 1
    ad[aarr[i]] = ad.get(aarr[i], 0) + 1
    

prefixb = [barr[0] for _ in range(m)]
bd = {barr[0]: 1}    
for i in range(1, m):
    prefixb[i] = prefixb[i - 1] + barr[i]
    bd[prefixb[i]] = bd.get(prefixb[i], 0) + 1
    bd[barr[i]] = bd.get(barr[i], 0) + 1
    
print(ad)
print(bd)
ans = 0
for i in range(n):
    if prefixa[i] == k:
        ans += 1
        
    target = prefixa[i] - k
    ans += bd.get(target, 0)
        
for i in range(m):
    target = prefixb[i] - k
    ans += ad.get(target, 0)
    
print(ans)
