# 2263번_트리의 순회

## n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있음
## 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성


'''
# 첫째 줄에 n(1 ≤ n ≤ 100,000)
# 다음 줄에는 인오더를 나타내는 n개의 자연수
# 그 다음 줄에는 같은 식으로 포스트오더가 주어짐
## 첫째 줄에 프리오더를 출력

(입력)
3
1 2 3
1 3 2

(출력)
2 1 3

'''

'''
ABDCEFG

중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

'''

import sys
input = sys.stdin.readline

n = int(input())
inodr = list(map(int, input().split()))
postorder = list(map(int, input().split()))



def inorder(cur):
    print(inorder[cur])
    
    inorder()
    inorder()

inorder(postorder[-1])