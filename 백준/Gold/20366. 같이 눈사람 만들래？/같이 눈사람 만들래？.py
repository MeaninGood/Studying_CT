import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

mn = 1 << 31
for i in range(n):
    for j in range(i + 3, n):
        s, e = i + 1, j - 1
        
        while s < e:
            total = (arr[i]  + arr[j]) - (arr[s] + arr[e])
            mn = min(mn, abs(total))
            
            if total < 0:
                e -= 1
            
            else:
                s += 1
                
print(mn)