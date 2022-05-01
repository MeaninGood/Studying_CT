n = int(input())

arr = []
for i in range(6):
    q, w = map(int, input().split())
    
    arr.append(w)
    
tmp = max(arr)
a = arr[arr.index(tmp) - 1]
b = arr[arr.index(tmp) - 2]
c = arr[arr.index(tmp) - 5]
d = arr[arr.index(tmp) - 4]

e = a * b
f = c * d
print(n * (e + f))

