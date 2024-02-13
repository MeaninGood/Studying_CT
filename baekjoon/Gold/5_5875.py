import sys

input = lambda: sys.stdin.readline().strip()

word = '#' + input()
n = len(word)

count = 0
answer = 0

arr = [0 for _ in range(n)]
prefix = [False for _ in range(n)]
suffix = [False for _ in range(n)]

if (n - 1) % 2 == 1:
    print(0)
    exit()


for i in range(1, n):
    arr[i] = arr[i - 1]

    if word[i] == '(':
        arr[i] += 1
    else:
        arr[i] -= 1

for i in range(1, n):
    prefix[i] = prefix[i - 1]
    if arr[i] < 0:
        prefix[i] = True

for i in range(n - 1)[::-1]:
    suffix[i] = suffix[i + 1]
    if arr[i] < 2:
        suffix[i] = True

for i in range(1, n):
    if word[i] == '(' and not prefix[i] and not suffix[i] and arr[-1] - 2 == 0:
        count += 1
    if word[i] == ')' and not prefix[i - 1] and arr[-1] + 2 == 0 and arr[i] + 2 >= 0:
        count += 1

print(count)
