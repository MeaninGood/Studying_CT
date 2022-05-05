import sys
input = sys.stdin.readline

arr = []

n = int(input())
for i in range(n):
    a = int(input())
    
    if a != 0:
        arr.append(a)
    elif a == 0:
        arr.pop()
        
print(sum(arr))