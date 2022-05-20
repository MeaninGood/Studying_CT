import sys
input = sys.stdin.readline

n = int(input())

s = 1
e = 1
cnt = 0
total = 1
while s <= e:
    if total == n:
        cnt += 1
        total -= s
        s += 1
        continue
        
    elif total < n:
        e += 1
        total += e
        
    else:
        total -= s
        s += 1

print(cnt)