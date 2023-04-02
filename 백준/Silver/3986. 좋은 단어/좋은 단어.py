import sys
input = lambda : sys.stdin.readline().strip()

T = int(input())
answer = 0
for tc in range(T):
    arr = list(input())
    
    st = []
    for i in range(len(arr)):
        if st and st[-1] == arr[i]:
            st.pop()

        else:
            st.append(arr[i])
            
    if not st:
        answer += 1
        
print(answer)