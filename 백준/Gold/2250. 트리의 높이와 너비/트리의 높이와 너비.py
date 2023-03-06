import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
width_d = {} # key: level, value: list of x

# node : current node
# 재귀 호출함 => 깊이가 됨(level)
cnt = 1
def preorder(node, level = 1):
    global cnt
    # 자식 없으면 return
    if node == -1:
        return

    """
    전위순회 : Left -> Middle -> Right
    """
    l_child, r_child = tree[node] # l, r
    
    # 왼쪽 자식 탐색
    preorder(l_child, level + 1)
    # 현재 노드
    # print(f'({node}, {level})', end = ' ')
    width_d[level] = width_d.get(level, []) + [cnt] # width_d에 넣어줌
    cnt += 1
    # 오른쪽 자식 탐색
    preorder(r_child, level + 1)
    

tree = [[] for _ in range(n + 1)]
parent = [-1 for _ in range(n + 1)] # 부모 노드 저장
for _ in range(n):
    node, l_child, r_child = map(int, input().split())
    tree[node] = [l_child, r_child]

    # 자식노드가 있으면
    if l_child != -1:
        parent[l_child] = node

    if r_child != -1:
        parent[r_child] = node


# 루트 노드 찾기
root = parent[1:].index(-1) + 1
preorder(root)

ans = [-1, -1] # 너비가 가장 넓은 레벨, 너비
for level in sorted(width_d.keys()):
    tmp = max(width_d[level]) - min(width_d[level]) + 1
    
    if tmp > ans[1]:
        ans = [level, tmp]

print(*ans)