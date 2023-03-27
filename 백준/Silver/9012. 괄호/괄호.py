import sys
input = lambda : sys.stdin.readline().strip()

T = int(input())
for tc in range(T):
    arr = list(input())
    n = len(arr)
    
    st = []
    for i in range(n):
        if st and st[-1] == '(' and arr[i] == ')':
            st.pop()
            
        else:
            st.append(arr[i])
            
    if st:
        print('NO')
    else:
        print('YES')