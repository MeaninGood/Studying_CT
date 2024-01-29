import sys
input = lambda : sys.stdin.readline().split()

cnt = 0
a, b = 10, 10
while a != 0:
    cnt += (a // b)
    a //= b
    
print(cnt)