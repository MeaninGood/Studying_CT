import sys
input = lambda : sys.stdin.readline().strip()


arr = list(input())

n = len(arr)
st = []
answer = 0
for i in range(n):
    if arr[i] == '(':
        st.append(arr[i])

    else:
        if arr[i - 1] == '(':
            st.pop()
            answer += len(st)

        else:
            st.pop()
            answer += 1

print(answer)