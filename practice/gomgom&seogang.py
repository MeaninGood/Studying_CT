# n = int(input())
# c, m = map(int, input().split())

# tmp = c // 2

# if n >= tmp + m:
#     print(tmp + m)

# else:
#     print(n)



# n = int(input())

# d = {}
# total = 0

# for i in range(n):
#     m = input()
    
#     if m == 'ENTER':
#         d = {}
#         continue
    
#     if m != 'ENTER':
#         d[m] = d.get(m, 0) + 1
        
#         if d[m] > 1:
#             continue
        
#         elif d[m] == 1:
#             total += 1
            
# print(total)





# n, m, k = map(int, input().split())
# ans = (k - 3 + m) % n

# if ans == 0:
#     print(n)

# else:
#     print(ans)
    

'''
1 1 2 2 3 3 4 4
2 * 1
4 * 2
6 * 3
8 * 4

4 * 3 * 2 * 1
12 24
'''

# n = int(input())
# total = 1
# for i in range(1, n + 1)[::-1]:
#     total *= i

# print(total)




# n, m = map(int, input().split())

# arr1 = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))

# ans = 0
# if n == m:
#     for i in range(n):
#         ans = max(-(arr1[i] - arr2[i]), ans)

# if n < m:
#     for i in range(n):
#         ans = max(-(arr1[i] - arr2[i]), ans)
    
#     for j in range(n, m):
#         ans = max(ans, arr2[j])

# else:
#     for i in range(m):
#         ans = max(-(arr1[i] - arr2[i]), ans)
        
# print(ans)



# n = int(input())
# w1 = ''
# w2 = ''

# arr1 = list(input())
# arr2 = list(input())

# d1 = {}
# d2 = {}
# word = ['a', 'e', 'i', 'o', 'u']
# for i in range(n):
#     if arr1[i] not in word:
#         w1 += arr1[i]
        
#     if arr2[i] not in word:
#         w2 += arr2[i]
        
#     d1[arr1[i]] = d1.get(arr1[i], 0) + 1
#     d2[arr2[i]] = d2.get(arr2[i], 0) + 1
    

# if (w1 == w2) and (d1 == d2) and (arr1[0] == arr2[0]) and (arr1[-1] == arr2[-1]):
#     print('YES')

# else:
#     print('NO')



# n, m = map(int, input().split())
# if (n - 1) % (1 + m) == 0:
#     print("Can't win")
# else:
#     print('Can win')


# n = int(input())

# if n < 10:
#     print(1)
#     exit()

# else:
#     total = 0
#     tmp = n
#     for i in range(1, 10)[::-1]:

#         total += (tmp // (i * 2)) * 2

#         tmp %= (i * 2)

#         if tmp < 10:
#             break
        
#     if tmp != 0:
#         total += 1
    
#     print(total)

import sys
sys.setrecursionlimit(100010)
n = int(input())
arr = list(map(int, input().split()))

result = [-1 for i in range(n)]
visited = [False for i in range(n)]

def recur(cur):
    if cur == n:
        print(*result)
        exit()
        
    for i in range(n):
        if not visited[i] and arr[cur] != arr[i]:
            visited[i] = True
            result[cur] = arr[i]
            recur(cur + 1)
            result[cur] = -1
            visited[i] = False


l = (n // 2)

d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1
    
    if d[i] > l:
        print(-1)
        exit()

recur