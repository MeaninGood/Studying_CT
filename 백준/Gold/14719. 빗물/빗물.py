import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [arr[0] for _ in range(m)]
for i in range(1, m):
    if arr[i] < prefix[i - 1]:
        prefix[i] = prefix[i - 1]

    else:
        prefix[i] = arr[i]

suffix = [arr[-1] for _ in range(m)]
for i in range(0, m - 1)[::-1]:
    if arr[i] < suffix[i + 1]:
        suffix[i] = suffix[i + 1]

    else:
        suffix[i] = arr[i]


answer = 0
for i in range(m):
    answer += min(prefix[i], suffix[i]) - arr[i]

print(answer)