from collections import deque

def solution(tickets):
    global answer
    answer = []
    
    tickets = sorted(tickets, key = lambda x: (x[0], x[1]))
    
    d = {}
    for i in range(len(tickets)):
        a, b = tickets[i]
        d[a] = d.get(a, []) + [b]

    
    def dfs(st = ["ICN"], tmp = []):
        global answer
        if not st:
            answer = tmp[::-1]
            return
        
        if st[-1] not in d or len(d[st[-1]]) == 0:
            c = st.pop()
            dfs(st, tmp + [c])
            
        else:
            dfs(st + [d[st[-1]].pop(0)], tmp)
            
        
    dfs() 
    
        
    return answer