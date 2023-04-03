import sys
input = lambda : sys.stdin.readline().strip()

arr = input().replace('()', '*').replace('[]', '*')

print(arr)