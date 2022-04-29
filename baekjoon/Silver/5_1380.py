idx = 1

while 1:
    n = int(input())
    if n == 0:
        break
    visited = [-1] + [0 for _ in range(n)]
    arr = ['#'] + [input() for _ in range(n)]
    # print(visited)
    # print(arr)
    for i in range(2 * n - 1):
        a, b = input().split()
        visited[int(a)] += 1
    
    print(idx, end = ' ')
    for i in range(1, n + 1):
        if visited[i] != 2:
            print(arr[i], end = ' ')
    
    idx += 1
    