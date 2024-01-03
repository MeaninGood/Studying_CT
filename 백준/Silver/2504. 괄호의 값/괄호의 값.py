import sys
input = lambda : sys.stdin.readline().strip()

arr = list(input())

answer = 0

st = []
num = 1
for i in range(len(arr)):
    if arr[i] == '(':
        st.append(arr[i])
        num *= 2

    elif arr[i] == '[':
        st.append(arr[i])
        num *= 3

    elif arr[i] == ')':
        if not st or st[-1] == '[':
            answer = 0
            break

        if arr[i - 1] == '(':
            answer += num

        st.pop()
        num //= 2

    elif arr[i] == ']':
        if not st or st[-1] == '(':
            answer = 0
            break

        if arr[i - 1] == '[':
            answer += num

        st.pop()
        num //= 3

if st:
    answer = 0
print(answer)