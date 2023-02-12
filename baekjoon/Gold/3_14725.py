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
        
    def print_node(self, cur, cur_node = None):
        if cur == 0:
            cur_node = self.root
            
        for nxt in sorted(cur_node.keys()):
            if nxt != "*":
                print("--" * cur + nxt)
            self.print_node(cur + 1, cur_node[nxt])
            
trie = Trie()
n = int(input())
for i in range(n):
    arr = list(input().split())
    trie.insert(arr[1:])
    
trie.print_node(0)        