a, b, c, n = map(int, input().split(' '))


for i in range(300):
    for j in range(300):
        if (a * i) + (b * j) > n:
            break
        
        if (n - (a * i) - (b * j)) % c == 0:
            print(1)
            exit()
            
print(0)