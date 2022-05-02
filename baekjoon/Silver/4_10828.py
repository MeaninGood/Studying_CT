import sys
input = sys.stdin.readline

st = []
n = int(input())
for i in range(n):
    tmp = input().split()
    
    if len(tmp) > 1:
        x, y = tmp[0], int(tmp[1])
        
    else:
        x = tmp[0]
    
    if x == 'push':
        st.append(y)
    
    elif x == 'pop':
        if len(st) > 0:
            print(st.pop())
        else:
            print(-1)
    
    elif x == 'size':
        print(len(st))
    
    elif x == 'empty':
        if len(st) > 0:
            print(0)
        else:
            print(1)
    elif x == 'top':
        if len(st) > 0:
            print(st[-1])
        else:
            print(-1)