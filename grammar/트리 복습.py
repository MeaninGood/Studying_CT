# 이진 트리 구현
"""
        1
    2       3
  4   5   6
7 
"""


# 1. 두개의 배열 이용하기

left = [-1, 2, 4, 6, -1, -1, -1, -1]
right = [-1, 3, 5, -1, -1, -1, -1 ,-1]


# 2. 합쳐서 하나의 배열 만들기
# arr[i][0]은 i의 왼쪽자식, arr[i][1]은 i의 오른쪽 자식
tree = [[], [2, 3], [4, 5], [6, -1], [7, -1], [-1, -1], [-1, -1], [-1, -1]]


# 3. 딕셔너리 활용하기 - 위와 동일

tree = {
    0 : [],
    1: [2, 3],
    2: [4, 5],
}

# 4. 하나의 배열로 만들기 + 이진트리의 성질 활용
"""
완전 이진트리의 경우 n의 자식 노드
      n
(n*2)   (n*2+1)
있다, 없다만 표시해주면 됨
"""
tree = [0, 1, 1, 1, 1, 1, 1, 0, 1]

node = 3
l_child = node * 2
r_child = node * 2 + 1


# 5. node라는 클래스를 생성
class Node:
    def __init__(self, v, l_child = -1, r_child = -1):
        self.v = v
        self.l_child = l_child
        self.r_child = r_child


root = Node(1)
root.l_child(Node(2))
root.r_child(Node(3))

root.l_child.l_child(Node(4))