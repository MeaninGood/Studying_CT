import sys
input = sys.stdin.readline

def recur(cur, total):
    global ans
    if cur == n:
        if total > 0:
            ans[total] += 1
        return
    
    recur(cur + 1, total + arr[cur])
    recur(cur + 1, total)


n = int(input())
arr = list(map(int, input().split()))

ans = [0 for _ in range(2000010)]
recur(0, 0)

for i in range(1, 2000010):
    if not ans[i]:
        print(i)
        break