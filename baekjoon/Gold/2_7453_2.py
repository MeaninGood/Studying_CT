import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


arr1 = []
arr2 = []

for seq in range(2):
    for i in range(n):
        for j in range(n):
            if seq == 0:
                arr1.append(arr[i][0] + arr[j][1])
                
            else:
                arr2.append(arr[i][2] + arr[j][3])
                
arr1.sort()
arr2.sort()

s, e = 0, n ** 2 - 1
cnt = 0
while s < n ** 2 and e >= 0:
    total = arr1[s] + arr2[e]
    
    if total == 0:
        tmp1 = arr1[s]
        x = 0
        while s < n ** 2 and tmp1 == arr1[s]:
            s += 1
            x += 1
            
        tmp2 = arr2[e]
        y = 0
        while e >= 0 and tmp2 == arr2[e]:
            e -= 1
            y += 1
            
        cnt += x * y
        
    elif total < 0:
        s += 1
        
    else:
        e -= 1
        
print(cnt)