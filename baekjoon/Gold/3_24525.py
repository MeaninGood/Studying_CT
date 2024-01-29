import sys

input = lambda: sys.stdin.readline().strip()


def check(a, b):
    return a != 0 and b != 0


arr = list(input())
n = len(arr)

prefixs = [0 for _ in range(n)]
prefixs[0] += arr[0] == "S"
prefixk = [0 for _ in range(n)]
prefixk[0] += arr[0] == "K"
for i in range(1, n):
    prefixs[i] = prefixs[i - 1] + (arr[i] == "S")
    prefixk[i] = prefixk[i - 1] + (arr[i] == "K")

suffixs = [0 for _ in range(n)]
suffixs[-1] += arr[-1] == "S"
suffixk = [0 for _ in range(n)]
suffixk[-1] += arr[-1] == "K"
for i in range(n - 1)[::-1]:
    suffixs[i] = suffixs[i + 1] + (arr[i] == "S")
    suffixk[i] = suffixk[i + 1] + (arr[i] == "K")


mx = -1
for i in range(n):
    a, b = prefixs[i], prefixk[i]
    if check(a, b) and a * 2 == b:
        mx = max(mx, i + 1)

for i in range(n - 1):
    a, b = suffixs[i], suffixk[i]
    if check(a, b) and a * 2 == b:
        mx = max(mx, n - i)

print(mx)
