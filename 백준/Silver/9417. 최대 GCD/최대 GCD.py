import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
for _ in range(n):
    arr = list(map(int, input().split(' ')))
    arr.sort(reverse=True)
    
    m = len(arr)
    mx = -1 << 31
    for i in range(m):
        for j in range(i + 1, m):
            a, b = arr[i], arr[j]
            
            while a % b != 0:
                a, b = b, a % b
                
            mx = max(mx, b)
            
    print(mx)