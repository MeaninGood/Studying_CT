n, m = map(int, input().split(' '))

ans = []
for x in range(100010):
    if x ** 2 + (2 * n * x) + m == 0:
        ans.append(x)
        
    elif (x ** 2) -(2 * n * x) + m == 0:
        ans.append(-x)
        
ans.sort()
print(*ans)