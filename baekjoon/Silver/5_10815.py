import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))
arr = sorted(nums)

ans = [0 for _ in range(m)]
for i in range(m):
    s, e = 0, n - 1
    target = cards[i]
    while s <= e:
        mid = (s + e) // 2

        if arr[mid] == target:
            ans[i] = 1
            break

        elif arr[mid] < target:
            s = mid + 1

        else:
            e = mid - 1

print(*ans)
