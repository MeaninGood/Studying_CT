# 중복 있는 n자리 m진수 출력하기


# n, m = map(int, input().split())

# arr = [0 for i in range(n)]

# def recur(cur):
#     if cur == n:
#         print(*arr)
#         return
    
#     for i in range(m):
#         arr[cur] = i
#         recur(cur + 1)
        
# recur(1)


# 중복 없는 n자리 m진수 출력

# n, m = map(int, input().split())
# arr = [0 for i in range(n)]
# visited = [False for i in range(m)]

# def recur(cur):
#     if cur == n:
#         print(*arr)
#         return
    
#     for i in range(m):
#         if visited[i]:
#             continue
        
#         arr[cur] = i
#         visited[i] = True
#         recur(cur + 1)
#         visited[i] = False

# recur(0)


# 중복 싹~~~ 제거

# n, m = map(int, input().split())
# arr = [0 for i in range(n)]

# def recur(cur, start):
#     if cur == n:
#         print(*arr)
#         return
    
#     for i  in range(start, m):
#         arr[cur] = i
#         recur(cur + 1, i + 1)

# recur(0, 0)





# m, n = map(int, input().split())

# arr = [1 for i in range(n)]
# visited = [False for i in range(m + 1)]
# def recur(cur):
#     if cur == n:
#         print(*arr)
#         return
    
#     for i in range(1, m + 1):
#         if visited[i]:
#             continue
        
#         arr[cur] = i
#         visited[i] = True
#         recur(cur + 1)
#         visited[i] = False
        
# recur(0)


# m, n = map(int, input().split())
# arr = [0 for i in range(n)]

# def recur(cur, start):
#     if cur == n:
#         print(*arr)
#         return
    
#     for i in range(start, m + 1):
#         arr[cur] = i
#         recur(cur + 1, i + 1)

# recur(0, 1)


m, n = map(int, input().split())
arr = [0 for i in range(n)]

def recur(cur):
    if cur == n:
        print(*arr)
        return
    
    for i in range(1, m + 1):
        arr[cur] = i
        recur(cur + 1)
        
recur(0)