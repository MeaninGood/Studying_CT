import sys
import heapq
input = lambda : sys.stdin.readline().strip()

"""
조건
1. 아기 상어의 처음 크기 2
--
2. 1초에 상하좌우 인접 1칸씩 이동
3. 자기보다 큰 물고기 x
4. 크기가 작은 물고기 먹을 수 있음
5. 크기가 같은 물고기는 지나갈 수만 있음
--

이동 결정
-- check_fish : 먹을 수 있는 물고기의 좌표와 거리 return, 0이면 False return
1. 더 이상 먹을 수 있는 물고기가 없으면 엄마상어에게 도움 요청
2. 먹을 수 있는 물고기가 1마리면, 먹으러 감
3. 먹을 수 있는 물고기가 1마리보다 많으면 가장 가까운 거 먹으러 감
--
    - 거리는 지나가야 하는 칸의 최솟값
    - 거리가 가까운 물고기가 많으면 가장 위에 있는 물고기
    - 그런 물고기가 여러마리라면 가장 왼쪽에 있는 물고기

-- check배열에서 넘겨 받은 값으로 이동, 거리 바로 더해서 넣어주기

4. 물고기는 이동과 동시에 먹음 - 이동하는 초만 계산
5. 물고기 먹으면 그 칸은 빈 칸
6. 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기 1 증가
    - 크기가 2인 상어는 2마리 먹어야 크기 3이 됨

아기상어가 몇 초 동안 엄마상어에게 도움을 요청하지 않고 물고기를 먹는지 출력
"""

# 상어 찾기
def find_shark():
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 9:
                return [i, j]

# 범위 체크
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
# 맵에 있는 물고기 모두 넣어 놓기
def check_fish():
    fish_dict = {}
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and arr[i][j] != 9:
                fish_dict[arr[i][j]] = fish_dict.get(arr[i][j], [])
                fish_dict[arr[i][j]].append([i, j])

    if not fish_dict: # 1. 먹을 수 있는 물고기 없을 때
        return False

    else: # 2. 먹을 수 있는 물고기 1마리 이상일 때, 지금 먹어야 하는 것만 return
        pass
        # fish_arr.sort(key = lambda x: [x[0], x[1]])
        # return fish_arr[0]

n = int(input())
arr = [list(map(int, input().split()))]
shark = find_shark()


