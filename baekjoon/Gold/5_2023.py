def is_prime(x):
    if x == 1:
        return False
    
    for i in range(2, x):
        if i * i > x:
            break
        
        if x % i == 0:
            return False
            
    return True

def recur(cur, total):
    if cur == n:
        print(total)
        return
    
    for i in range(1, 10):
        tmp = (total * 10) + i
        
        if is_prime(tmp):
            recur(cur + 1, tmp)

n = int(input())

recur(0, 0)
