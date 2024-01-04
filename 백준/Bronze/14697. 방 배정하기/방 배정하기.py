a, b, c, n = map(int, input().split(' '))

arr = sorted([a, b, c], reverse=True)
a, b, c = arr[0], arr[1], arr[2]

for i in range(300):
    if a * i > n:
        break
    
    for j in range(300):
        if (b * j) > n:
            break

        if (n - (a * i) + (b * j)) % c == 0:
            print(1)
            exit()
            
print(0)