# 2138 - 전구와 스위치

"""
1번 스위치를 누르고 시작하는 경우

1번 스위치를 누르지 않고 시작하는 경우

"""

import sys
input = lambda : sys.stdin.readline().strip()

def switch(arr, idx, n, cnt):
    for i in range(1, n - 1):
        if arr[i - 1] != idx[i - 1]:
            cnt += 1
            arr[i - 1] = not arr[i - 1]
            arr[i] = not arr[i]
            arr[i + 1] = not arr[i + 1]

    if arr[n - 1] != idx[n - 1]:
        cnt += 1
        arr[n - 2] = not arr[n - 2]
        arr[n - 1] = not arr[n - 1]
    
    if arr == idx:
        return cnt

    return -1


n = int(input())
arr1 = list(map(int, input()))
idx = list(map(int, input()))

arr2 = arr1[:]

res1 = switch(arr1, idx, n, 0)

for i in range(2):
    arr2[i] = not arr2[i]

res2 = switch(arr2, idx, n, 1)

if res1 != -1 and res2 != -1:
    print(min(res1, res2))
    exit()

elif res1 != -1:
    print(res1)
    exit()

elif res2 != -1:
    print(res2)
    exit()

else:
    print(-1)
print(min(res1, res2) if res1 or res2 else -1)


# cnts = {0 : False, 1 : False}
# cnt1 = 0
# for i in range(1, n - 1):
#     if arr1[i - 1] != idx[i - 1]:
#         cnt1 += 1
#         arr1[i - 1] = not arr1[i - 1]
#         arr1[i] = not arr1[i]
#         arr1[i + 1] = not arr1[i + 1]


# if arr1[n - 1] != idx[n - 1]:
#     cnt1 += 1
#     arr1[n - 2] = not arr1[n - 2]
#     arr1[n - 1] = not arr1[n - 1]

# if arr1 == idx:
#     cnts[0] = True




# cnt2 = 1
# for i in range(1, n - 1):
#     if arr2[i - 1] != idx[i - 1]:
#         cnt2 += 1
#         arr2[i - 1] = not arr2[i - 1]
#         arr2[i] = not arr2[i]
#         arr2[i + 1] = not arr2[i + 1]


# if arr2[n - 1] != idx[n - 1]:
#     cnt2 += 1
#     arr2[n - 2] = not arr2[n - 2]
#     arr2[n - 1] = not arr2[n - 1]

# if arr2 == idx:
#     cnts[1] = True

# print(arr1, arr2, idx, cnts, cnt1, cnt2)

# if cnts[0] and cnts[1]:
#     print(min(cnt1, cnt2))
#     exit()

# elif cnts[0] and not cnts[1]:
#     print(cnt1)
#     exit()

# elif not cnts[0] and cnts[1]:
#     print(cnt2)
#     exit()

# else:
#     print(-1)

"""
8
00000000
11011000

7
1101000
1111111
"""