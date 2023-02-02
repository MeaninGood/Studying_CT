import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
m = int(input())
arr = sorted(list(map(int, input().split())))

prefix = [0 for i in range(n - 1)]
for i in range(n - 1):
    prefix[i] = arr[i + 1] - arr[i]
    
prefix.sort(reverse=True)
print(sum(prefix[m - 1:]))