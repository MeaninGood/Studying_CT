import sys
input = lambda : sys.stdin.readline().strip()


n = int(input())
arr = list(map(int, input().split()))
m = int(input())

arr.append(0)
arr.append(1001)

arr.sort()

ans = 0
for k in range(1, n + 2):
    cnt = 0
    for i in range(arr[k - 1] + 1, arr[k]):
        for j in range(arr[k - 1] + 1, arr[k]):
            if i < j and (i <= m <= j):
                cnt += 1

    ans = max(ans, cnt)

print(ans)