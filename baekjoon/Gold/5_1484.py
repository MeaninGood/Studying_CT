import sys

input = lambda: sys.stdin.readline().strip()


n = int(input())
# e: 현재, s : 원래
s, e = 1, 1
ans = []
while s <= e and e < 100001:
    total = e ** 2 - s ** 2
    if total == n:
        ans.append(e)
        s += 1
        s += 1
        
    elif total > n:
        s += 1
        
    else:
        e += 1

if ans:
    for a in ans:
        print(a)

else:
    print(-1)