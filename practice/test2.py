dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# def dfs(x, y):
#     ret = 1
#     visited[x][y] = True
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 0:
#             continue
        
#         ret += dfs(nx, ny)
        
#     return ret


def dfs(x, y):
    ret = [1, arr[x][y]] # 왼쪽 연결요소 크기, 오른쪽 합
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not in_range(nx, ny) or visited[nx][ny] or arr[nx][ny] == 0:
            continue
        
        li = dfs(nx, ny)
        ret[0] += li[0]
        ret[1] += li[1]
        
    return ret
        
        
T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False for i in range(n)] for j in range(n)]
    
    ans = [-1, -1]
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and not visited[i][j]:
                ret = dfs(i, j)
                
                if ans[0] < ret[0]:
                    # 카피 안 하면 원본 바뀔 때마다 자기가 바뀌니까
                    # 혹시 모르니까 copy!
                    # 어지간하면 리스트 넣을 때는 다 카피 넣는 게 좋다
                    ans =  ret.copy()
                    # ans = ret으로 해도 됨
                    
                elif ans[0] == ret[0] and ans[1] > ret[1]:
                    ans = ret.copy()
                    # ans = ret으로 해도 됨
                    
    print(f'#{tc} {ans[0]} {ans[1]}')
    


'''
투포인터로 정렬된 두 배열을 합치는 것을 O(n)에 할 수 있다.

## 정렬되어 있는 배열이라는 가정이 중요함!

1 3 4 4 6 8
s1
2 5 5 6 6 7
s2

s2가 s1보다 더 크니까 s1을 새로운 배열에 넣고 s1이 뒤로 감

1 2 3 4 4 5 5 6 6 6 7 8
'''

arr1 = [1, 3, 4, 4, 6, 8]
arr2 = [2, 5, 5, 6, 6, 7]
arr3 = []

s1 = 0
s2 = 0
while s1 < len(arr1) and s2 < len(arr2):
    if arr1[s1] < arr2[s2]:
        arr3.append(arr1[s1])
        s1 += 1
        
    else:
        arr3.append(arr2[s2])
        s2 += 1
'''        
if s1 < len(arr1): # s2가 끝났다면
    while s1 < len(arr1):
        arr3.append(arr1[s1])
        s1 += 1
        
if s2 < len(arr2): # s2가 끝났다면
    while s2 < len(arr2):
        arr3.append(arr2[s2])
        s2 += 1
    
'''
    
    
# if s1 < len(arr1): # s2가 끝났다면
while s1 < len(arr1):
    arr3.append(arr1[s1])
    s1 += 1
        
# if s2 < len(arr2): # s2가 끝났다면
while s2 < len(arr2):
    arr3.append(arr2[s2])
    s2 += 1


'''
a b c d e f g h

a b c d

a b 
c d

a
b

c
d

e f g h

e f
g h

e
f

g
h

'''


arr = [5, 4, 2, 3, 4, 5, 6, 7, 8, 6, 6, 1]
# 어디부터 어디까지 정렬할 건지 인자로 넘겨줌
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
           