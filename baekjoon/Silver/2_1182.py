# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
# arr2 = [ 0 for i in range(n)]
# visited = [False for i in range(n)]


# def recur(cur):
#     cnt = 0
#     if cur == n:
#         total = 0
#         for i in range(n):
#             total += arr[arr2[i]]
#             return total
            
#         if total == s:
#             cnt += 1
#         return cnt
    
#     for i in range(n):
#         if visited[i]:
#             continue
        
#         arr2[cur] = i
#         visited[i] = True
#         cnt += recur( cur + 1 )
#         visited[i] = False
    
#     return cnt

# print(recur(0))



# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(10000)

# def recur(cur, total):
#     ret = 0
#     if cur > n:
#         return -100000000000
    
#     if cur == n:
#         return ret
    
#     if total == s:
#         ret += 1

#     recur(cur + 1, total + arr[cur])
#     recur(cur + 1, total)

    

# n, s = map(int, input().split())
# arr = list(map(int, input().split()))



# print(recur(0, 0))




import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def recur(cur, total, cnt = 0):
    global ret

    if cur == n:
        if total == s and cnt > 0:
            ret += 1
        return
    
    recur(cur + 1, total + arr[cur], cnt + 1)
    recur(cur + 1, total, cnt)

    

n, s = map(int, input().split())
arr = list(map(int, input().split()))

ret = 0

recur(0, 0, 0)

print(ret)