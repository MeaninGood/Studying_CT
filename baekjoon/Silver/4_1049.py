# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(m)]

# v = [[0, n]]
# a = 0
# b = n
# while b > 0:
#     a += 1
#     b -= 6
    
#     if b < 0:
#         b = 0
    
#     v.append([a, b])

# print(v)

# total = 100000000
# for i in range(m):
#     for x, y in v:
#         total = min(total, arr[i][0] * x + arr[i][1] * y)
        
# print(total)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

a = sorted(arr)
b = arr.copy()
b.sort(key = lambda x: x[1])

total = 10000000
total = min(total, a[0][0] * ((n // 6) + 1))
total = min(total, (n // 6) * a[0][0] + (n % 6) * b[0][1])
total = min(total, b[0][1] * n)
# if (a[0][0] * (n // 6) + 1) < b[0][1] * n:
#     total = min(total, a[0][0] * ((n // 6) + 1))
    
# if b[0][1] * 6 > a[0][0]:
#     total = min(total, (n // 6) * a[0][0] + (n % 6) * b[0][1])

# else:
#     total = min(total, b[0][1] * n)
    
print(total)