from collections import deque

def solution(begin, target, words):
    answer = 0
    n = len(words)
    
    def bfs(word):
        que = deque()
        visited = [False for i in range(n)]
        
        que.append([word, 0])
        
        while que:
            word, cnt = que.popleft()
            
            if word == target:
                return cnt
            
            for i in range(n):
                diff = 0
                
                if not visited[i]:
                    for j in range(len(word)):
                        if word[j] == words[i][j]:
                            continue
                            
                        diff += 1
                        
                if diff == 1:
                    que.append([words[i], cnt + 1])
                    visited[i] = True
                    
        return 0
    
    answer = bfs(begin)
        
    return answer