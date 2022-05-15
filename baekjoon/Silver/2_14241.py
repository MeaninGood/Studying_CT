n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

m = arr[0] + arr[1]
total = arr[0] * arr[1]

if n > 2:
    for i in range(2, n):
        total += m * arr[i]
        m += arr[i]
        
print(total)