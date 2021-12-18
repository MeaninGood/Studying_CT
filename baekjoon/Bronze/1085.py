# 1085번_직사각형에서 탈출

## 현수가 있는 좌표 (x, y)
## 왼쪽 아래 꼭짓점 (0, 0)
## 오른쪽 위 꼭짓점 (w, h)
## 직사각형의 경계선까지 가는 거리의 최솟값

x, y, w, h = map(int, input().split())

dist = [(w-x), (h-y), x, y]

print(min(dist))