import sys
input = sys.stdin.readline


def dfs(cur):
    visited[cur] = True
    ret = 0
    for nxt, d in v[cur]:
        if visited[nxt]:
            continue
        
        ret += dfs(nxt) + d
        print(ret)
    st.append(cur)
    
    return ret


n = int(input())
m = int(input())

v = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    v[a].append([b, c])

print(v)
st = []
ans = -100000000
for i in range(1, n + 1):
    if not visited[i]:
        ans = max(ans, dfs(i))
        
        
print(ans)
print(st)