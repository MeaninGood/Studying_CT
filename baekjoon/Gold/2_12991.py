# import sys
# input = lambda: sys.stdin.readline().strip()

# n, k = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]

# def check(x):
#     total = 0
#     for i in range(1, n + 1):
#         total += 

n, k = 3, 3
arr = []
a = [2, 3, 7]
b = [3, 5, 7]
for i in range(n):
    for j in range(n):
        arr.append(a[i] * b[j])
        
print(arr)