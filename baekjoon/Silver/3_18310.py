import sys

input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = sorted(list(map(int, input().split(' '))))

print(arr[n // 2] if n % 2 else arr[n // 2 - 1])