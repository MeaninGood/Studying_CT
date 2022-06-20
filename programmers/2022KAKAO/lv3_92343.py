def solution(info, edges):
    visited = [False for _ in range(18)]
    v = [[] for _ in range(18)]
    for a, b in edges:
        v[a].append(b)

    answer = 0
    
    for i in range(len(info)):
        if info[i] == 0:
            info[i] = 1
        
        else:
            info[i] = -1
    
    def dfs(cur):
        visited[cur] = True
        ret = 1
        for nxt in v[cur]:
            if visited[nxt]:
                continue
            
            ret += max(ret, dfs(nxt) + info[nxt])
        return ret
    
    answer = dfs(0)

    return answer



info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))