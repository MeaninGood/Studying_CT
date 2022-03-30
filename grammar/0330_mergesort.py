'''
3
7
1 1 2 0 0 1 0
0 1 1 0 0 1 0
0 0 0 0 0 2 0
0 1 1 0 0 1 0
0 0 2 0 0 2 0
0 3 1 0 1 0 0
0 1 1 0 1 0 0
5
1 1 0 0 0
2 1 0 0 0
0 0 0 0 1
0 0 0 1 1
0 0 0 1 1
8
0 0 0 0 0 0 0 3
0 4 4 3 5 0 0 4
0 0 4 1 1 0 0 2
0 0 2 0 0 0 0 1
0 0 0 0 0 0 0 2
0 0 4 3 3 1 0 2
0 1 2 1 1 0 0 0
0 0 0 0 0 4 3 2
'''


# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# def dfs(x, y):
#     ret = [1, arr[x][y]]
#     visited[x][y] = True
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if not (0 <= nx < n and 0 <= ny < n) or visited[nx][ny] or arr[nx][ny] == 0:
#             continue
#
#         li = dfs(nx, ny)
#
#         ret[0] += li[0]
#         ret[1] += li[1]
#
#     return ret
#
# T = int(input())
# for t in range(1, T + 1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for i in range(n)]
#     visited = [[False for i in range(n)] for j in range(n)]
#
#     ans = [-1, -1]
#     for i in range(n):
#         for j in range(n):
#             if arr[i][j] != 0 and not visited[i][j]:
#                 ret = dfs(i, j)
#
#                 if ans[0] < ret[0]:
#                     ans = ret
#                 elif ans[0] == ret[0] and ans[1] > ret[1]:
#                     ans = ret
#
#     print('#' + str(t) + ' ' + str(ans[0]) + ' ' + str(ans[1]))








'''
투포인터로 정렬된 두 배열을 합치는것을 O(n)에 할 수 있다.

1   3   4   4   6   8
        s1
2   5   5   6   6   7
    s2

1   2   3


1   2   3   4   4   5   5   6   6   6   7   8
'''

# arr1 = [1, 3, 4, 4, 6, 8]
# arr2 = [2, 5, 5, 6, 6, 7]
# arr3 = []
#
# s1 = 0
# s2 = 0
# while s1 < len(arr1) and s2 < len(arr2):
#     if arr1[s1] < arr2[s2]:
#         arr3.append(arr1[s1])
#         s1 += 1
#     else:
#         arr3.append(arr2[s2])
#         s2 += 1
#
# while s1 < len(arr1):
#     arr3.append(arr1[s1])
#     s1 += 1
#
# while s2 < len(arr2):
#     arr3.append(arr2[s2])
#     s2 += 1

# 1   2   3   4   4   5   5   6   6   6   7   8
arr = [5, 4, 2, 3, 4, 5, 6, 7, 8, 6, 6, 1]

def merge_sort(s, e):
    global arr

    if s >= e:
        return

    mid = (s + e) // 2

    merge_sort(s, mid)
    merge_sort(mid + 1, e)

    arr2 = []
    s1 = s
    s2 = mid + 1
    while s1 <= mid and s2 <= e:
        if arr[s1] <= arr[s2]:
            arr2.append(arr[s1])
            s1 += 1
        else:
            arr2.append(arr[s2])
            s2 += 1

    while s1 <= mid:
        arr2.append(arr[s1])
        s1 += 1

    while s2 <= e:
        arr2.append(arr[s2])
        s2 += 1

    for i in range(len(arr2)):
        arr[i + s] = arr2[i]

merge_sort(0, len(arr) - 1)

print(arr)