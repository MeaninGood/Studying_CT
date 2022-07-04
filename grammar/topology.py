from collections import deque

def topology():
    queue = deque()

    result = []

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        result.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
                
    
    return result

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    indegree[y] += 1

print(graph[1:])
print(indegree[1:])

ans = topology()
print(*ans)