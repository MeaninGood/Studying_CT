n = int(input())
arr = [0] + [input() for _ in range(n)]
prefix = [0 for _ in range(n + 1)]
cnt = {}


for i in range(1, n + 1):
    cnt[arr[i]] = cnt.get(arr[i], 0) + 1
    prefix[i] = cnt[arr[i]]


for i in range(1, n + 1):
    pass
print(prefix)

'''

P P H P S P P H H H H H H S S
1 2 1 3 1 4 5 2 3 4 5 6 7 2 3

'''