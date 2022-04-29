def recur(cur, sin, ssen):
    if cur == n:
        return sin - ssen
    
    recur(cur + 1, sin * arr[0][cur], ssen)
    recur(cur + 1, sin, ssen + arr[1][cur])
    recur(cur + 1, sin * arr[0][cur], ssen + arr[1][cur])


n = int(input())
arr = [[] for _ in range(2)]
for _ in range(n):
    a, b = map(int, input().split())
    arr[0].append(a)
    arr[1].append(b)
    
print(arr)
print(recur(0, 1, 0))
    
