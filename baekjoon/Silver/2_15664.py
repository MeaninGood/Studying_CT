import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))


visited = [False for _ in range(n)]
def recur(cur, start, tmp):
    if cur == m:
        print(tmp)
        return
    
    num = -1
    for i in range(start, n):
        if visited[i] or num == arr[i]:
            continue
        
        visited[i] = True
        num = arr[i]
        recur(cur + 1, i, tmp + str(arr[i]) + ' ')
        visited[i] = False
        
recur(0, 0, '')