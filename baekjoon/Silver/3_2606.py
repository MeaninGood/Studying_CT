# 2606번_바이러스

## 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때
## 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력

'''
# 첫째 줄에는 컴퓨터의 수
# 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨짐
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어짐
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어짐
## 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수 출력


(입력)
7
6
1 2
2 3
1 5
5 2
5 6
4 7

(출력) 
4

'''

visited = [False for i in range(110)]

def dfs(cur):
    visited[cur] = True

    for nxt in v[cur]: # 1번과 연결된 애들
        if visited[nxt]: # True면 continue
            continue
        
        dfs(nxt) # 1번과 연결된 애들부터 싹 돌면서 차례로 True로 바꿔줌


n = int(input())
m = int(input())

v = [[] for i in range(110)]

for i in range(m):
    a, b = map(int, input().split())
    v[a].append(b) # 무향이니까 둘 다 추가
    v[b].append(a) # 무향이니까 둘 다 추가

dfs(1)

print(visited.count(True) - 1) # 1은 제외니까 -1 해줌