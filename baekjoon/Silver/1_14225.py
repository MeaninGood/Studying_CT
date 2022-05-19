import sys
input = sys.stdin.readline

def recur(cur, total):
    global result
    if cur == n:
        if total > 0:
            result.append(total)
        return
    
    recur(cur + 1, total + arr[cur])
    recur(cur + 1, total)


n = int(input())
arr = list(map(int, input().split()))
result = []

recur(0, 0)
result.sort()

m = result[-1] + 1
for i in range(1, m):
    if i not in result:
        print(i)
        break