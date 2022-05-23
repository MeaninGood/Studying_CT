# a, b = map(int, input().split())
#
# A, B = a, b
# while a % b != 0:
#     a, b = b, a % b
#
# print(b)            #최대공약수
# print(A * B // b)   #최소공배수


import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    
    d = len(arr)
    mx = -1 << 20
    for i in range(d):
        for j in range(i + 1, d):
            a, b = arr[i], arr[j]
            
            while a % b != 0:
                a, b = b, a % b
            
            mx = max(mx, b)

    print(mx)
    