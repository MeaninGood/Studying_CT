a, b, c, n = map(int, input().split(' '))

arr = sorted([a, b, c], reverse=True)
a, b, c = arr[0], arr[1], arr[2]

for i in range(1, 300):
    for j in range(1, 300):
        
        if not (a % i or b % j or c % (n // (i + j))):
            print(1)
            exit()
            
print(0)