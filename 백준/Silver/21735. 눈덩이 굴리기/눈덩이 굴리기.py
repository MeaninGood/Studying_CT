import sys
input = lambda : sys.stdin.readline().strip()

# 현재 시간, 눈덩이 크기, 위치
def recur(cur, total, idx):
    global mx
    mx = max(mx, total)
    # 시간 다 끝나면 return
    if cur == m:
        return

    # 시간 + 1, 눈덩이 크기, 이동할 위치
    if idx + 1 <= n:
        recur(cur + 1, total + arr[idx + 1], idx + 1)
        
    if idx + 2 <= n:
        recur(cur + 1, (total // 2) + arr[idx + 2], idx + 2)

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
mx = 0

recur(0, 1, 0)
print(mx)