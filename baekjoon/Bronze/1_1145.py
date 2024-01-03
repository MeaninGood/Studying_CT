arr = list(map(int, input().split(' ')))

def gcd(a, b):
    if b > a:
        a, b = b, a
        
    A, B = a, b
    print('##', a, b)
    while a % b != 0:
        a, b = b, a % b
        
    return A * B // b

ans = 0
arr.sort()
print(arr)

for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            tmp = gcd(arr[i], arr[j])
            tmp2 = gcd(tmp, arr[k])
            print(tmp, tmp2)
            
            if tmp == tmp2:
                ans = tmp
                break
            
print(ans)