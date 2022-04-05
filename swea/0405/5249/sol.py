# def find_(x):
#     if par[x] == x:
#         return x
    
#     else:
#         return find_(par[x])
    
# def union_(a, b):
#     a = find_(a)
#     b = find_(b)
    
#     if a == b:
#         return
    
#     par[a] = b


# T = int(input())
# for tc in range(1, T + 1):
#     n, m = map(int, input().split())
#     v = [list(map(int, input().split())) for _ in range(m)]
#     par = [i for i in range(n + 1)]

#     v.sort(key = lambda x: x[2])

#     ans = 0
#     for i in range(m):
#         x, y = v[i][0], v[i][1]
        
#         if find_(x) == find_(y):
#             continue
        
#         union_(x, y)
#         ans += v[i][2]
        
#     print(f'#{tc} {ans}')




def find_(x):
    if par[x] == x:
        return x
    
    else:
        return find_(par[x])
    
def union_(a, b):
    a = find_(a)
    b = find_(b)
    
    if a == b:
        return
    
    par[a] = b
    
n, m = map(int,  input().split())
v = [list(map(int, input().split())) for _ in range(m)]
par = [i for i in range(n + 1)]

v.sort(key = lambda x: x[2])

ans = 0
for i in range(m):
    x, y = v[i][0], v[i][1]
    
    if find_(x) == find_(y):
        continue
    
    union_(x, y)
    ans += v[i][2]