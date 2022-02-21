from functools import total_ordering


n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

arr1 = []
arr2 = []
for i in range(n):
    for j in range(n):
        arr1.append(li[i][0] + li[j][1])
        
for i in range(n):
    for j in range(n):
        arr2.append(li[i][2]+li[j][3])
        
arr1.sort()
arr2.sort()

s = 0
e = len(arr2) - 1
ans = 0
while e > 0 and s < len(arr1):
    
    if arr1[s] + arr2[e] == 0:
        ans += 1
        e -= 1

    if arr1[s] + arr2[e] > 0:
        e -= 1
        
    else:
        s += 1
        
print(ans)


