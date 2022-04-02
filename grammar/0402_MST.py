'''
union find 최적화 두가지

1. 경로 압축            find 한번의 시간복잡도 amortized O(log n)
2. union by rank
'''



# par = [i for i in range(1000010)]
# rnk = [0 for i in range(1000010)]
# sz = [1 for i in range(1000010)]
#
# def find(x):
#     if par[x] == x:
#         return x
#     else:
#         par[x] = find(par[x])
#         return par[x]
#
# def union_(a, b):
#     a = find(a)
#     b = find(b)
#
#     if a == b:
#         return
#
#     if rnk[a] < rnk[b]:
#         par[a] = b
#         sz[b] += sz[a]
#     elif rnk[a] > rnk[b]:
#         par[b] = a
#         sz[a] += sz[b]
#     else:
#         par[a] = b
#         sz[b] += sz[a]
#         rnk[b] += 1
#
# n, m = map(int, input().split())
# for i in range(m):
#     a, b, c = map(int, input().split())
#
#     if a == 0:
#         union_(b, c)
#     else:
#         if find(b) == find(c):
#             print("YES")
#         else:
#             print("NO")
#
#     x = int(input())
#
#     print(sz[find(x)])


# def find(x):
#     if par[x] == x:
#         return x
#     else:
#         return find(par[x])
#
# def union_(a, b):
#     a = find(a)
#     b = find(b)
#
#     if a == b:
#         return
#
#     par[a] = b
#     arr[b] = min(arr[a], arr[b])
#
# n, m, k = map(int, input().split())
# arr = [0] + list(map(int, input().split()))
# par = [i for i in range(n + 1)]
# visited = [False for i in range(n + 1)]
#
# for i in range(m):
#     a, b = map(int, input().split())
#
#     union_(a, b)
#
# ans = 0
# for i in range(1, n + 1):
#     x = find(i)
#
#     if visited[x]:
#         continue
#
#     ans += arr[x]
#     visited[x] = True
#
# print(ans)

# def find(x):
#     if par[x] == x:
#         return x
#     else:
#         return find(par[x])
#
# def union_(a, b):
#     a = find(a)
#     b = find(b)
#
#     if a == b:
#         return
#
#     par[a] = b
#
# n, m = map(int, input().split())
# v = [list(map(int, input().split())) for i in range(m)]
# s, e = map(int, input().split())
# par = [i for i in range(100010)]
#
# v.sort(key=lambda x:-x[2])
#
# for i in range(m):
#     union_(v[i][0], v[i][1])
#
#     if find(s) == find(e):
#         print(v[i][2])
#         exit()


# def find(x):
#     if par[x] == x:
#         return x
#     else:
#         return find(par[x])

# def union_(a, b):
#     a = find(a)
#     b = find(b)

#     if a == b:
#         return

#     par[a] = b

# n, m = map(int, input().split())
# v = [list(map(int, input().split())) for i in range(m)]
# par = [i for i in range(n + 1)]

# v.sort(key=lambda x:x[2])

# ans = 0
# cnt = 0
# for i in range(m):
#     x, y = v[i][0], v[i][1]

#     if find(x) == find(y):
#         continue

#     union_(x, y)
#     ans += v[i][2]
#     cnt += 1

# print(ans)


