def dfs(cur, option):
    if cur == 0:
        return
    
    if option == 0:
        print(cur, end=' ')
        
    dfs(lft[cur], option)
    
    if option == 1:
        print(cur, end=' ')
        
    dfs(rgt[cur], option)
    
    if option == 2:
        print(cur, end=' ')
        
        
n, m = map(int, input().split())

lft = [0 for i in range(n + 1)]
rgt = [0 for i in range(n + 1)]

arr = list(map(int, input().split()))

for i in range(0, len(arr) - 1, 2):
    if lft[arr[i]] != 0:
        rgt[arr[i]] = arr[i + 1]
    else:
        lft[arr[i]] = arr[i + 1]


dfs(1, 0)
print()
dfs(1, 1)
print()
dfs(1, 2)