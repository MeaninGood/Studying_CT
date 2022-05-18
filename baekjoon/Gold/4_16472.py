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


# n = int(input())
# arr = input()

# m = len(arr)

# tmp = arr[0]
# idx = 0

# cnt = 0
# total = 0
# ans = 0
# for i in range(1, m):
#     if cnt > n:
#         cnt = 0
#         tmp = arr[i]
#         total -= (i - idx)
#         ans = max(total, ans)
        
#     if tmp != arr[i]:
#         cnt += 1
#         idx = i
#         tmp = arr[i]
        
#     elif tmp == arr[i]:
#         total += 1
    
# print(ans)




import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(str, input().rstrip()))


s = 0
e = 0
cnt = 1
ans = -10000
li = [arr[0]]
tmp = 1
d = len(arr)
while s <= e and li and e < d - 1:
    print(f's는 {s} e는 {e}, tmp는 {tmp}, {li}, ans는 {ans}')
    if cnt <= n:
        e += 1
        if arr[e] not in li:
            li.append(arr[e])
            cnt += 1
            ans = max(ans, tmp)
            if len(li) <= n:
                tmp += 1
            
        else:
            e += 1
            tmp += 1
            ans = max(ans, tmp)
            
    else:
        li.pop(0)
        s += 1
        tmp -= 1
        cnt -= 1
        
print(ans)
        


