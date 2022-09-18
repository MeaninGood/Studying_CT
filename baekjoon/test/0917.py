# 1.
'''
import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
answer = 0
for i in range(n):
    a, b, c = map(int, input().split())

    if a == (b + c):
        tmp = (a * (b + c)) * 2

    else:
        tmp = a * (b + c)


    if tmp > answer:
        answer = tmp

print(answer)
'''



# 2.
'''
import sys
input = lambda : sys.stdin.readline().strip()


n = int(input())
par = {}
for i in range(n - 1):
    a, b = input().split()

    par[a] = b

a, b = input().split()
x, y = a, b

answer = 0
while 1:
    try:
        tmp = par[x]
        if tmp == b:
            answer = 1
            break

        else:
            x = par[x]

    except:
        break

while 1:
    try:
        tmp = par[y]
        if tmp == a:
            answer = 1
            break

        else:
            y = par[y]

    except:
        break

print(answer)

'''



# 9.
# import sys
# input = lambda : sys.stdin.readline().strip()

# def recur(cur):
#     global answer

#     if cur == n:
#         tmp, total = 0, 0
#         for i in check:
#             total = max(total + i, i)
#             tmp = max(tmp, total)

#         answer = max(answer, tmp)
#         return

#     for i in range(n):
#         if visited[i]:
#             continue

#         for j in range(m):
#             check[m * cur + j] = arr[i][j]
#         visited[i] = True
#         recur(cur + 1)
#         visited[i] = False


# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [False for _ in range(n)]
# check = [0 for _ in range(n * m)]
# answer = 0

# recur(0)

# print(answer)


# 9.
'''
import sys
input = lambda : sys.stdin.readline().strip()

def get_max(arr):
    ret = 0
    total = 0
    for i in arr:
        total = max(total + i, i)
        ret = max(ret, total)

    return ret

def get_lft(arr):
    ret = 0
    total = 0
    for i in arr:
        total += i
        ret = max(ret, total)

    return ret

def merge(a, b):
    return [max(a[0], b[0], a[3] + b[2]), a[1] + b[1], max(a[2], a[1] + b[2]), max(b[3], b[1] + a[3])]

def recur(cur, info):
    global answer

    if cur == n:
        answer = max(answer, info[0])
        return

    for i in range(n):
        if visited[i]:
            continue

        visited[i] = True
        recur(cur + 1, merge(info, lst[i]))
        visited[i] = False


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for i in range(n)]
lst = [[0 for i in range(4)] for j in range(n)]
visited = [False for i in range(n)]
answer = 0

for i in range(n):
    lst[i][0] = get_max(arr[i])
    lst[i][1] = sum(arr[i])
    lst[i][2] = get_lft(arr[i])
    lst[i][3] = get_lft(arr[i][::-1])

recur(0, [0, 0, 0, 0])

print(answer) 
                                               

'''

# 3.
import sys
input = lambda : sys.stdin.readline().strip()

def recur(cur, total, cans):
    global answer
    if cur == (m * 2):
        answer = max(answer, total)
        return

    for i in range(n):
        if cans[i] == 0:
            continue

        ntotal = total + arr[cur][i]
        cans[i] -= 1
        recur(cur + 1, ntotal, cans)
        cans[i] += 1

n, m = map(int, input().split())
cans = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(m * 2)]

answer = 0
recur(0, 0, cans)
print(answer)