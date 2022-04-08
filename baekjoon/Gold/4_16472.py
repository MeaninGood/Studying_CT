# 16472번_고냥이

## 문자열을 주면 그 중에서 최대 N개의 종류의 알파벳을 가진 연속된 문자열만 인식
## 번역기가 인식할 수 있는 최대 문자열의 길이 출력

'''
# 첫째 줄에는 인식할 수 있는 알파벳의 종류의 최대 개수 N이 입력된다. (1 < N ≤ 26)
# 둘째 줄에는 문자열이 주어진다. (1 ≤ 문자열의 길이 ≤ 100,000)
# 단, 문자열에는 알파벳 소문자만이 포함
## 첫째 줄에 번역기가 인식할 수 있는 문자열의 최대길이를 출력

(입력)
2
abbcaccba

(출력)
4

'''

# n = int(input())
# arr = input()

# a = len(arr)

# s = 0
# e = 0
# cnt = 0
# total = 1
# mx = -1000000
# li = []
# while s < a and e < a:
#     if arr[s] not in li:
#         li.append(arr[s])
#     print(arr[e])
#     print(li)
#     print(total)
    
#     if cnt > n or len(li) > n:
#         li.pop(0)
#         s += 1
#         total = 1
    
#     elif arr[e] in li:
#         e += 1
#         total += 1
#         mx = max(mx, total)
    
#     elif arr[e] not in li and len(li) == n:
#         li.pop(0)
#         e += 1
#         s += 1
#         total = 1
    
#     elif arr[e] not in li and len(li) < n:
#         li.append(arr[e])
#         e += 1
#         cnt += 1
#         total += 1
#         mx = max(mx, total)
        
# print(mx)


n = int(input())
arr = input()
sz = len(arr)

s = 0
e = 0
total = 0
check = []
while s < d and e < d:
    check.append(arr[s])
    
    if arr[e] in check:
        
        