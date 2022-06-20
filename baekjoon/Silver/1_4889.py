import sys
input = lambda: sys.stdin.readline().rstrip()

tc = 1
while 1:
    arr = list(map(str, input()))
    if '-' in arr:
        break

    st = []
    for i in range(len(arr)):
        if arr[i] == '{':
            st.append(arr[i])
        
        elif arr[i] == '}' and len(st) > 0 and st[-1] == '{':
            st.pop()
        
        else:
            st.append(arr[i])
            
    cnt = 0
    for i in range(0, len(st)):
        if i % 2 == 1 and st[i] == '{':
            cnt += 1
        elif i % 2 == 0 and st[i] == '}':
            cnt += 1

    print(f'{tc}. {cnt}')
    tc += 1