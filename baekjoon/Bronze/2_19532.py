a, b, c, d, e, f = map(int, input().split(' '))

def getResult(x, y):
    return a * x + b * y == c and d * x + e * y == f

for i in range(1000):
    for j in range(1000):
        if getResult(i, j):
            print(i, j)
            break
            
        if getResult(-i, j):
            print(-i, j)
            break
            
        if getResult(i, -j):
            print(i, -j)
            break
            
        if getResult(-i, -j):
            print(-i, -j)
            break
            