# a, b = map(int, input().split())
#
# A, B = a, b
# while a % b != 0:
#     a, b = b, a % b
#
# print(b)            #최대공약수
# print(A * B // b)   #최소공배수


# import sys
# input = sys.stdin.readline

# T = int(input())
# for tc in range(T):
#     arr = list(map(int, input().split()))
#     arr.sort(reverse=True)
    
#     d = len(arr)
#     mx = -1 << 20
#     for i in range(d):
#         for j in range(i + 1, d):
#             a, b = arr[i], arr[j]
            
#             while a % b != 0:
#                 a, b = b, a % b
            
#             mx = max(mx, b)

#     print(mx)
    
    
import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
for _ in range(n):
    arr = list(map(int, input().split(' ')))
    arr.sort(reverse=True)
    
    m = len(arr)
    mx = -1 << 31
    for i in range(m):
        for j in range(i + 1, m):
            a, b = arr[i], arr[j]
            
            while a % b != 0:
                a, b = b, a % b
                
            mx = max(mx, b)
            
    print(mx)