# v, a, b, c = list(map(int, input().split()))

# arr = [a, b, c]

# i = 0
# while 1:
#     v -= arr[i % 3]
    
#     if v < 0:
#         if i % 3 == 0:
#             print("F")
#             break
        
#         elif i % 3 == 1:
#             print("M")
#             break
        
#         elif i % 3 == 2:
#             print('T')
#             break
        
#     elif v == 0:
#         if i % 3 == 0:
#             print("M")
#             break
        
#         elif i % 3 == 1:
#             print("T")
#             break
        
#         elif i % 3 == 2:
#             print('F')
#             break

#     i += 1
    
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# cnt = 0
# for i in range(n):
#     if a[i] == b[i]:
#         cnt += 1

# ans = 0
# for i in range(n):
#     for j in range(n):
#         if a[i] == b[j] and i != j:
#             ans += 1

# print(cnt)
# print(ans)
        


# n = int(input())
# arr = [list(map(int, input().split())) for i in range(n)]
# s = input()

# for i in range(n - 1):
#     if s[i] == 'R':
#         for j in range(1, n):
#             if arr[i][1] == arr[j][1] and s[j-1] == 'L':
#                 print("Yes")
#                 break
                
#     elif s[i] == 'L':
#         for j in range(1, n):
#             if arr[i][1] == arr[j][1] and s[j-1] == 'R':
#                 print('Yes')
#                 break
                      
                      
                 
# n = int(input())
# arr = [list(map(int, input().split())) for i in range(n)]
# s = input()

# li = set()
# for i in range(n - 1):
#     for j in range(1, n):
#         if arr[i][1] == arr[j][1]:
#             li.add(s[i])
#             li.add(s[j])
#             if len(li) == 2:
#                 print('Yes')
#                 exit()      
                      
# if len(li) == 1:
#     print('No')

# cnt = 0
# def dfs(cur):
#     global cnt
#     visited[cur] = True
    
#     for nxt in arr[cur]:
#         if visited[nxt]:
#             continue
#         cnt += 1
#         dfs(nxt)
    
# n, m = map(int, input().split())
# arr = [[] for i in range(310)]
# visited = [False for i in range(310)]

# for i in range(m):
#     a, b, c = map(int, input().split())
#     arr[a].append(b)
#     arr[b].append(a)
    
# dfs(n)
# print(cnt)




# 1
a, b, c, d = map(int, input().split())
n = a
arr = [b, c, d]

idx = 0
while n >= arr[idx]:
    n -= arr[idx]
    idx = (idx + 1) % 3
    
ans = 'FMT'
print(ans[idx])




# 2
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

x, y = 0
for i in range(n):
    for j in range(n):
        if a[i] == b[j]:
            if i == j:
                x += 1
            else:
                y += 1
                
print(x)
print(y)


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

idx = {}

for i in range(n):
    idx[a[i]] = i
    
x, y = 0, 0
for i in range(n):
    t = idx.get(b[i], -1)
    
    if t == i:
        x += 1
    elif t != -1:
        y += 1
        
        
# 3
# 1. y 값 같은 것들끼리 뭉침
# 2. x축 기준으로 정렬
# 3. 다른 애가 나오는지 체크

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
s = input()

for i in range(n):
    arr[i].append(s[i])
'''
2 3 R
1 1 R
4 1 L
형태로 붙임
'''

arr.append([0, 2000000000, 0])
arr.sort(key=lambda x: (x[1], x[0]))


idx = 0
for i in range(1, n + 1):
    if arr[i][1] != arr[i - 1][1]:
        flag = False
        
        while idx < i:
            if arr[idx][2] == 'R':
                flag = True
            
            elif flag:
                print('Yes')
                exit()
                
            idx += 1
            
print('no')
'''
? 1 d
? 1 d
? 1 d
? 3 d
? 3 d
? 5 d
? 10 d

'''




# 4
'''
U앞에 나오는 R과 L은 U로 상쇄가 됨
U앞에 R이랑 L 다 지우고 시작
UUUURLRLRLRRR 형태로 남음
쓸 데 없는 연산 하지 않음

'''

n, x = map(int, input().split())
s = input()

st = []

for i in s:
    if len(st) > 0 and st[-1] != 'U' and i == 'U':
        st.pop()
    else:
        st.append(i)
        
for i in st:
    if i == 'U':
        x //= 2
        
    elif i == 'L':
        x *= 2
        
    else:
        x = 2 * x + 1