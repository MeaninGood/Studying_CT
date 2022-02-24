def check(n):
    cnt = 0
    if n == 1:
        return False
    
    if i * i > 0 :
        return False
    
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
            
    return cnt == 2

n = int(input())

def recur(cur, num):
    if cur != 0 and not check(num):
        return
    
    if cur == n:
        print(num)
        return
    
    for i in range(1, 10):
        recur(cur+1, 10*num+i)

recur(0, 0)