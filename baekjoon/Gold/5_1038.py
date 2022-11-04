import sys
input = lambda : sys.stdin.readline().strip()


cnt = 0
answer = -1
def recur(cur, tmp, e):
    global cnt, answer
    if cur == e:
        if cnt == n:
            answer = int(tmp)
        
        cnt += 1
        return

    for i in range(10):
        if len(tmp) == 0 or (len(tmp) >= 1 and int(tmp[-1]) > i):
            recur(cur + 1, tmp + str(i), e)


n = int(input())
for i in range(1, 11):
    recur(0, '', i)

print(answer)