import sys
input = sys.stdin.readline

n = int(input())
arr = [-1000000010] + list(map(int, input().split()))
prv = [-1 for i in range(n + 1)]
lis = [-1000000010]

for i in range(n + 1):
    if lis[-1] < arr[i]:
        lis.append(arr[i])
        
    else:
        s = 0
        e = len(lis)
        
        while s < e:
            mid = (s + e) // 2
            
            if arr[i] > lis[mid]:
                s = mid + 1
                
            else:
                e = mid
                
        lis[e] = arr[i]
        prv[i] = i
        
            
print(len(lis) - 1)
print(*lis[1:])
print(prv)