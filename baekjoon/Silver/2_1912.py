# 1912번_연속합

## n개의 정수로 이루어진 임의의 수열이 주어짐
## 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 함
## 단, 수는 한 개 이상 선택해야 함


'''
# 첫째 줄에 정수 n(1 ≤ n ≤ 100,000)
# 둘째 줄에는 n개의 정수로 이루어진 수열이 주어짐
# 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수
## 첫째 줄에 답을 출력

(입력)
10
10 -4 3 1 5 6 -35 12 21 -1

(출력)
33

'''

# def recur(cur):
#     if cur == n:
#         return
    
#     recur(cur) + arr[cur]
#     recur(cur + 1)

# n = int(input())
# arr = [0] + list(map(int, input().split()))





# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# prefix = [0 for i in range(n)]
# prefix[0] = arr[0]
# mn = 1000000
# idx = 0
# mx = arr[0]
# for i in range(1, n):
#     prefix[i] = prefix[i - 1] + arr[i]
    
#     if mn > prefix[i]:
#         mn = prefix[i]
#         idx = i
        
#     if mx < prefix[i]:
#         mx = prefix[i]
#         print(f'${mx}')
        
# print(prefix)
# print(mn)
# print(idx)

# if idx != n - 1:
#     prefix[idx + 1] = arr[idx + 1]
#     mx2 = mn
#     for i in range(idx + 2, n):
#         prefix[i] = prefix[i - 1] + arr[i]
        
#         if mx2 < prefix[i]:
#             mx2 = prefix[i]
            
#     print(prefix)
#     print(max(mx, mx2))

# else:
#     print(mx)





# import sys
# input = sys.stdin.readline

# n = int(input())
# arr = list(map(int, input().split()))

# prefix = [0 for i in range(n)]
# prefix[0] = arr[0]
# mn = arr[0]
# idx = 0
# mx = arr[0]
# mx3 = arr[0]
# for i in range(1, n):
#     prefix[i] = prefix[i - 1] + arr[i]
    
#     if mn > prefix[i]:
#         mn = prefix[i]
#         idx = i
        
#     if mx < prefix[i]:
#         mx = prefix[i]
    
#     if arr[i] > mx3:
#         mx3 = arr[i]
        
# print(prefix)
# print(f'idx는 {idx}')
# if idx < n - 2:
#     prefix[idx + 1] = arr[idx + 1]
#     mx2 = mn
#     for i in range(idx + 2, n):
#         prefix[i] = prefix[i - 1] + arr[i]
        
#         if mx2 < prefix[i]:
#             mx2 = prefix[i]
            
#     tmp = max(mx, mx2)
#     print(max(tmp, mx3))

# elif idx == n - 2:
#     prefix[idx + 1] = arr[idx + 1]

#     tmp = max(mx, prefix[idx + 1])
#     print(max(tmp, mx3))
    
# elif idx == n - 1:
#     print(max(mx, mx3))
    
# elif idx == 0:
#     prefix[idx + 1] = arr[idx + 1]
#     mx2 = mn
#     for i in range(idx + 2, n):
#         prefix[i] = prefix[i - 1] + arr[i]
        
#         if mx2 < prefix[i]:
#             mx2 = prefix[i]
            
#     tmp = max(mx, mx2)
#     print(max(tmp, mx3))

'''
7
2 -1 3 -2 4 -3 7

'''



import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

prefix = [0 for i in range(n)]
prefix[0] = arr[0]

mx = arr[0]
for i in range(1, n):
    prefix[i] = max(prefix[i - 1] + arr[i], arr[i])
    
    if mx < prefix[i]:
        mx = prefix[i]

print(mx)