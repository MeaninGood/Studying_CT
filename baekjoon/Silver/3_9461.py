T = int(input())

arr = [ -1 for i in range(110)]
arr[1] = 1
arr[2] = 1
arr[3] = 1

for i in range(4, 110):
    arr[i] = arr[i - 3] + arr[i - 2]
    
for tc in range(T):
    n = int(input())
    print(arr[n])