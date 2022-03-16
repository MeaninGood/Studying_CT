# 5


n = int(input())

for i in range(1, n+1):
    print(' ' * (n - i) + '*' * (2 * i - 1))



# 6


n = int(input())

for i in range(1, n+1)[::-1]:
    print(' ' * (n - i) + '*' * (2 * i - 1))