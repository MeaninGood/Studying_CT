n = int(input())
# a[i] - a[i+1] = a[i+2]
res = -100
idx = 0
li = []
for i in range(n):
    arr = [n, n-i]
    # arr[0] = n
    # arr[1] = n - i
    cnt = 1
    for j in range(n):
        arr.append(arr[j-2] - arr[j-1])
        cnt += 1
        # print(arr)
        
        if cnt > res:
            res = cnt
            idx = i
            li = arr 
            
        if arr[j] < 0:
            break
            
print(idx)
print(res)
# li = [n, n-idx]
# for i in range(2, res):
#     li.append(li[i-2] - li[i-1])

print(li)