arr = list(map(str, input()))

n = len(arr)

tmp = []
for i in range(1, n - 1):
    for j in range(i + 1, n):
        a = arr[0:i]
        b = arr[i:j]
        c = arr[j:]
        
        a.reverse()
        b.reverse()
        c.reverse()
        
        tmp.append(a + b + c)
        
tmp.sort()

print("".join(tmp[0]))