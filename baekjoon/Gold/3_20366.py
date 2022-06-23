'''
5
3 5 2 5 9 7 8 4 2 1 1 3 5 4 3
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

mx = 1 << 30
for i in range(n):
    for j in range(i + 3, n):
        x = i
        y = j
        
        s = i + 1
        e = j - 1
        while s < e:
            total = (arr[i] + arr[j]) - (arr[s] + arr[e])
            
            mx = min(mx, abs(total))
            
            if total < 0:
                e -= 1
            
            else:
                s += 1

print(mx)
    