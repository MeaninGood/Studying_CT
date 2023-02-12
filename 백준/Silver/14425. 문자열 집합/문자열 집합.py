import sys
input = lambda : sys.stdin.readline().strip()

class Trie():
    
    def __init__(self):
        self.root = {}
        
        
    def insert(self, arr):
        cur_node = self.root
        
        for nxt in arr:
            if nxt not in cur_node:
                cur_node[nxt] = {}
            
            cur_node = cur_node[nxt]
            
        cur_node["*"] = {}
        
        
    def search(self, arr):
        cur_node = self.root
        
        for nxt in arr:
            if nxt in cur_node:
                cur_node = cur_node[nxt]
                
            else:
                return False
            
        return "*" in cur_node


n, m = map(int, input().split())
trie = Trie()
for i in range(n):
    tmp = list(input())
    trie.insert(tmp)
    
answer = 0
for i in range(m):
    tmp = list(input())
    if trie.search(tmp):
        answer += 1
        
print(answer)