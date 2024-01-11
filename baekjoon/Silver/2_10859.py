import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

reverse_nums = {"0": "0", "1": "1", "2": "2", "5": "5", "6": "9", "8": "8", "9": "6"}

exclude_nums = ["3", "4", "7"]

new_n, reverse_n = list(str(n)), list(str(n))[::-1]

for i in range(len(new_n)):
    if new_n[i] in exclude_nums or reverse_n[i] in exclude_nums:
        print("no")
        exit()

    else:
        reverse_n[i] = reverse_nums[reverse_n[i]]


new_n, reverse_n = int("".join(new_n)), int("".join(reverse_n))
for i in range(2, n):
    if i * i > n:
        break

    if new_n % i == 0 or reverse_n % i == 0:
        print("no")
        exit()

if n == 1:
    print("no")
else:
    print("yes")
