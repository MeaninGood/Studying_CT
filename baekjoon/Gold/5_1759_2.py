import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = sorted(list(input().split()))

print(arr)
target = ["a", "e", "i", "o", "u"]

res = ["" for _ in range(n)]


def recur(cur):
    if cur == n:
        flag = False
        for i in res:
            if i in target:
                flag = True

        if flag:
            print("".join(res))

        return

    for i in range(m):
        if cur == 0 and res[cur] >= arr[i]:
            continue

        if cur > 0 and res[cur - 1] >= arr[i]:
            continue

        res[cur] = arr[i]
        recur(cur + 1)
        res[cur] = "#"


recur(0)

print("" > "a")
print("" < "a")
