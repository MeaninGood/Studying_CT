# 5


n = int(input())

for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2 * i - 1))



# 6


n = int(input())

for i in range(1, n+1)[::-1]:
    print(' ' * (n - i) + '*' * (2 * i - 1))
    


# 8

n = int(input())

for i in range(1, n + 1):
    print('*' * i + ' ' * (n - i) + ' ' * (n - i) + '*' * i)

for i in range(n)[::-1]:
    print('*' * i + ' ' * (n - i) + ' ' * (n - i) + '*' * i)