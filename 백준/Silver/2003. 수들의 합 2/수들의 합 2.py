import sys
input = lambda : sys.stdin.readline().strip()


n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0]

s, e = 0, 0
ans = 0
total = arr[0]
while e < n:
    if total == m:
        ans += 1
        
        e += 1
        total += arr[e]
        
    elif total < m:
        e += 1
        total += arr[e]
        
    else:
        total -= arr[s]
        s += 1

        
print(ans)