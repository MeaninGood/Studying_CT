# arr = list(input())
# n = len(arr)
# sarr = [0 for _ in range(n)]
# sarr[0] += arr[0] == 'S'
# for i in range(1, n):
#     sarr[i] = sarr[i - 1] + (arr[i] == 'S')
# sarr + [0]

# karr = [0 for _ in range(n)]
# for i in range(n - 1)[::-1]:
#     karr[i] = karr[i + 1] + (arr[i] == 'K')
    
# s, e = n - 1, 0
# mx = -1
# print(sarr)
# print(karr)
# while s >= 0 and e < n - 1:
#     if sarr[s] != 0 and karr[e] == sarr[s] * 2:
#         tmps = sarr[s]
#         while sarr[s] == tmps and s >= 0:
#             s -= 1
            
#         tmpk = karr[e]
#         while karr[e] == tmpk and e < n - 1:
#             e += 1
#         mx = max(abs(s - e), mx)
        
#     if karr[e] == sarr[s]:
#         tmps = sarr[s]
#         while sarr[s] == tmps and s >= 0:
#             s -= 1
            
#         tmpk = karr[e]
#         while karr[e] == tmpk and e < n - 1:
#             e += 1
            
#     elif sarr[s] > karr[e]:
#         e += 1
        
#     else:
#         s -= 1
    
# print(mx)

# import sys

# input = lambda: sys.stdin.readline().strip()

# def check(a, b):
#     return a != 0 and b != 0


# arr = list(input())
# n = len(arr)

# prefixs = [0 for _ in range(n)]
# prefixs[0] += arr[0] == "S"
# prefixk = [0 for _ in range(n)]
# prefixk[0] += arr[0] == "K"
# for i in range(1, n):
#     prefixs[i] = prefixs[i - 1] + (arr[i] == "S")
#     prefixk[i] = prefixk[i - 1] + (arr[i] == "K")

# suffixs = [0 for _ in range(n)]
# suffixs[-1] += arr[-1] == "S"
# suffixk = [0 for _ in range(n)]
# suffixk[-1] += arr[-1] == "K"
# for i in range(n - 1)[::-1]:
#     suffixs[i] = suffixs[i + 1] + (arr[i] == "S")
#     suffixk[i] = suffixk[i + 1] + (arr[i] == "K")


# mx = -1
# for i in range(n):
#     a, b = prefixs[i], prefixk[i]
#     if check(a, b) and a * 2 == b:
#         mx = max(mx, i + 1)

# for i in range(n - 1):
#     a, b = suffixs[i], suffixk[i]
#     if check(a, b) and a * 2 == b:
#         mx = max(mx, n - i)

# print(mx)


import sys

input = lambda: sys.stdin.readline().strip()

def check(a, b):
    return a != 0 and b != 0

def getScore(a):
    if a == 'S':
        return 2
    
    elif a == 'K':
        return -1
    
    return 0

arr = list(input())
n = len(arr)

prefix = [0 for _ in range(n)]
prefix[0] += getScore(arr[0])
for i in range(1, n):
    tmp = getScore(arr[i])
    prefix[i] = prefix[i - 1] + tmp


suffix = [0 for _ in range(n)]
suffix[-1] += getScore(arr[-1])
for i in range(n - 1)[::-1]:
    tmp = getScore(arr[i])
    suffix[i] = suffix[i + 1] + tmp
    
print(prefix)
print(suffix)