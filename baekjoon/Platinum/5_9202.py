import sys
from collections import deque
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
            
    
    def search(self, arr):
        cur_node = self.root
        
        for nxt in arr:
            if nxt in cur_node:
                cur_node = cur_node[nxt]
            
            else:
                return False
            
        return "*" in cur_node


def in_range(x, y):
    return 0 <= x < 4 and 0 <= y < 4


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
visited = [[False for i in range(4)] for j in range(4)]
def dfs(x, y, tmp):
    global idx
    visited[x][y] = True

    if len(tmp) == 16:
        idx.add(tmp)
        return

    for i in range(8):
        nx = x + dx[i] 
        ny = y + dy[i]

        if not in_range(nx, ny) or visited[nx][ny]:
            continue

        dfs(nx, ny, tmp+arr[nx][ny])
        visited[nx][ny] = False

trie = Trie()
n = int(input())
for _ in range(n):
    tmp = input()
    trie.insert(tmp)
    
x = input()
m = int(input())
for _ in range(m):
    idx = set()
    arr = [list(input()) for _ in range(4)]
    
    x = input()
    dfs(0, 0, arr[0][0])
    print(idx)