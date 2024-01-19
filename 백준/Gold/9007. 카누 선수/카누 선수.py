import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    tmp = [list(map(int, input().split())) for _ in range(4)]

    arr1 = []
    arr2 = []

    a, b = 0, 1
    for k in range(2):
        for i in range(m):
            for j in range(m):
                if k == 0:
                    arr1.append(tmp[a][i] + tmp[b][j])
                    
                elif k == 1:
                    arr2.append(tmp[a][i] + tmp[b][j])
                
        a += 2
        b += 2


    arr1.sort()
    arr2.sort()
    
    s = 0
    e = len(arr2) - 1
    x = arr1[s]
    y = arr2[e]
    while s < len(arr1) and e >= 0:        
        if abs(n - (x + y)) > abs(n - (arr1[s] + arr2[e])):
            x = arr1[s]
            y = arr2[e]
        
        elif abs(n - (x + y)) == abs(n - (arr1[s] + arr2[e])):
            if x + y > arr1[s] + arr2[e]:
                x = arr1[s]
                y = arr2[e]
        
        if arr1[s] + arr2[e] < n:
            s += 1
            
        else:
            e -= 1
            
    print(x + y)