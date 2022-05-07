def gcd(a, b):
    if b == 0:
        return a
    
    else:
        return gcd(b, a%b)
    
    
n = int(input())

arr = list(map(int, input().split()))
idx = arr[0]
for i in range(1, n):
    if idx > arr[i]:
        tmp = gcd(idx, arr[i])
        print(f'{idx // tmp }/{arr[i] // tmp}')
    
    if idx < arr[i]:
        tmp = gcd(arr[i], idx)
        print(f'{idx // tmp}/{arr[i] // tmp}')
        
    if idx == arr[i]:
        print(f'1/1')
    