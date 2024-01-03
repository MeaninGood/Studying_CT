import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
arr = [int(input()) for _ in range(n)]
numbers = set(arr)


mx = 1
for a in numbers:
    tmp = arr[:]
    
    while a in tmp:
        tmp.remove(a)
                
    m = len(tmp)
    
    cnt = 1
    for i in range(1, m):
        if tmp[i] == tmp[i - 1]:
            cnt += 1
            mx = max(mx, cnt)
            
        else:
            cnt = 1

print(mx)