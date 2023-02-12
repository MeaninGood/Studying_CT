class Trie:
    def __init__(self):
        self.root = {}
    
    
    # insert
    def insert(self, arr):
        cur_node = self.root # 처음 노드 루트로 잡아줌
        for x in arr: # 문자열 하나하나에 대해
            if x not in cur_node: # 현재 노드에 해당하는 문자가 없으면 새로 만들기
                cur_node[x] = {}
                
            cur_node = cur_node[x] # 노드 들어가기(a -> p -> p)
            
        cur_node["*"] = {} # "*" 노드를 만들어 단어 끝 표시
    
    
    # search
    def search(self, arr):
        cur_node = self.root
        
        for x in arr:
            if x in cur_node: # 해당하는 단어가 있을 때만 들어가기
                cur_node = cur_node[x]
            else: # 없으면 False return
                return False
            
        return "*" in cur_node # 노드의 끝까지("*") False return 하지 않았다면 
    
arr = [["a", "p", "p"], ["a", "n", "t"], ["a", "p", "p", "l", "e"]]
trie = Trie()
for i in range(3):
    trie.insert(arr[i])


print(trie.search("ant"))


# a : {p : {p : { * : * } } }
#     {n : { t : { * : *} } }
#  요런 느낌으로 돌리는거 같은 느낌스 