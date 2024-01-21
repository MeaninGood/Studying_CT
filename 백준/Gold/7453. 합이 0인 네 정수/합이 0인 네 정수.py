# n = int(input())
# li = [list(map(int, input().split())) for _ in range(n)]

# arr1 = []
# arr2 = []
# for i in range(n):
#     for j in range(n):
#         arr1.append(li[i][0] + li[j][1])
        
# for i in range(n):
#     for j in range(n):
#         arr2.append(li[i][2]+li[j][3])
        
# arr1.sort()
# arr2.sort()

# s = 0
# e = len(arr2) - 1
# ans = 0
# while e > 0 and s < len(arr1):
    
#     if arr1[s] + arr2[e] == 0:
#         ans += 1
#         e -= 1

#     if arr1[s] + arr2[e] > 0:
#         e -= 1
        
#     else:
#         s += 1
        
# print(ans)




import sys
input = sys.stdin.readline


n = int(input())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
    
arr1 = []
arr2 = []
for k in range(2):
    for i in range(n):
        for j in range(n):
            if k == 1:
                arr2.append(arr[i][2] + arr[j][3])
                
            else:
                arr1.append(arr[i][0] + arr[j][1])

arr1.sort()
arr2.sort()

s = 0
e = len(arr2) - 1


cnt = 0
while s < len(arr1) and e >= 0:
    total = arr1[s] + arr2[e]
    
    if total == 0:
        tmp = arr1[s]
        x = 0
        while s < len(arr1) and tmp == arr1[s]:
            s += 1
            x += 1
        
        tmp = arr2[e]
        y = 0
        while e >= 0 and tmp == arr2[e]:
            e -= 1
            y += 1
        
        cnt += x * y
        
    elif arr1[s] + arr2[e] < 0:
        s += 1
    
    else:
        e -= 1
        
print(cnt)