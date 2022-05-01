import sys
sys.setrecursionlimit(10010)
input = sys.stdin.readline

def recur(cur):
    ret = cur
        
    if cur == n:
        return ret
    

    ret *= recur(cur + 1)
    
    return ret

    


while True:
    try:
        n = int(input())
        
        if n == 0:
            print(f'{n:5} -> 1')

        else:
            ans = recur(1)
            while 1:
                tmp = ans % 10
                if tmp:
                    break
                
                ans //= 10
            
            print(f'{n:5} -> {tmp}')
    except:
        break