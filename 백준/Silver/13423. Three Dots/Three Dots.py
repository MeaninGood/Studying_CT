import sys

input = lambda: sys.stdin.readline().strip()

t = int(input())

for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    d = {}
    for i in arr:
        d[i] = d.get(i, 0) + 1
        
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % 2:
                continue
            
            tmp = (arr[i] + arr[j]) // 2
            
            if d.get(tmp):
                ans += 1
    print(ans)