import sys
input = lambda : sys.stdin.readline().strip()

arr = [-1]

cnt = 1
x = 1

tmp = set()
while cnt <= 1000000:

    flag = True
    nx = x
    while nx > 0:
        a = nx % 10
        
        if a in tmp:
            flag = False
            break
        
        tmp.add(a)
        nx //= 10
        
    if flag:
        arr.append(x)
        cnt += 1
    
    x += 1
    tmp.clear()
    
while 1:
    n = int(input())
    
    if n == 0: break
    
    print(arr[n])