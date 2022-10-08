import sys

input = lambda : sys.stdin.readline()

def recur(cur, tmp):
    global mx, mn
    if cur == n:
        if int(tmp) > int(mx):
            mx = tmp

        if int(tmp) < int(mn):
            mn = tmp
        return

    for i in range(10):
        if len(tmp) == 0:
            tmp += str(i)
            recur(cur, tmp)
            tmp = ''

        else:
            if arr[cur] == '<' and str(i) not in tmp:
                if int(tmp[-1]) < i:
                    tmp += str(i)
                    recur(cur + 1, tmp)
                    tmp = tmp[:-1]
                

            elif arr[cur] == '>' and str(i) not in tmp:
                if int(tmp[-1]) > i:
                    tmp += str(i)
                    recur(cur + 1, tmp)
                    tmp = tmp[:-1]
        

n = int(input())
arr = list(input().split())
mn = '9' * (n + 1)
mx = '0' * (n + 1)
recur(0, '')
print(mx)
print(mn)