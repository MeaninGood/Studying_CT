# import sys
# input = sys.stdin.readline

# def recur(cur, total):
#     if cur == n:
#         return (total == m)
    
#     return recur(cur + 1, total + arr[cur]) + recur(cur + 1, total)

# n, m = map(int, input().split())
# arr = list(map(int, input().split()))

# print(recur(0, 0) - (m == 0))


import sys
input = sys.stdin.readline

# recur(시작(현재), 합, v의 어디에 넣을 건지, 어디서 끝낼 건지)
def recur(cur, total, idx, e):
    if cur == e:
        v[idx].append(total)
        return
    
    recur(cur + 1, total + arr[cur], idx, e)
    recur(cur + 1, total, idx, e)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
v = [[] for _ in range(2)]

recur(0, 0, 0, n // 2)
recur(n // 2, 0, 1, n)

v[0].sort()
v[1].sort()

# print(v)

s = 0
e = len(v[1]) - 1
cnt = 0
while s < len(v[0]) and e >= 0:
    if v[0][s] + v[1][e] == m:
    
        tmp = v[0][s]
        x = 0
        while s < len(v[0]) and v[0][s] == tmp:
            x += 1
            s += 1
        
        tmp = v[1][e]
        y = 0
        while e >= 0 and v[1][e] == tmp:
            y += 1
            e -= 1
            
        cnt += x * y
    
    elif v[0][s] + v[1][e] < m:
        s += 1
    
    else:
        e -= 1
        
print(cnt - (m == 0))

