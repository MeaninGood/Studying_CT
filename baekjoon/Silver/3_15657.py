m, n = map(int, input().split())

arr = sorted(list(map(int, input().split())))

v = [0 for i in range(n)]

def recur(cur, start):
    if cur == n:
        print(*v)
        return
    
    for i in range(start, m):
        v[cur] = arr[i]
        recur(cur + 1, i + 1)

        
recur(0, 0)