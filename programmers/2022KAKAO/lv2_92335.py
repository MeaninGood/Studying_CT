# num = ''

# idx = int(input())
# tmp = idx
# k = 10

# while tmp >= 1:
#     if tmp % k == 0:
#         num += '0'
#         tmp //= k
    
#     elif tmp % k != 0:
#         num += str(tmp % k)
#         tmp //= k

# num = num[::-1].split('0')
# print(num)
# for i in range(len(num)):
#     if num[i] == '':
#         num[i] = 0
    
#     num[i] = int(num[i])
    
# seive = [True for _ in range(max(num) + 1)]
# seive[0] = False
# seive[1] = False

# for i in range(2, max(num) + 1):
#     if not seive[i]:
#         continue
    
#     for j in range(i * i, max(num) + 1, i):
#         seive[j] = False

# cnt = 0

# for i in num:
#     if seive[i]:
#         cnt += 1
        
# print(cnt)



# num = ''

# idx = int(input())
# tmp = idx
# k = 3
# while tmp >= 1:
#     if tmp % k == 0:
#         num += '0'
#         tmp //= k
    
#     elif tmp % k != 0:
#         num += str(tmp % k)
#         tmp //= k

# num = num[::-1].split('0')
# ans = 0
# for i in range(len(num)):
#     if num[i] == '':
#         continue
    
#     num[i] = int(num[i])
    
#     cnt = 0
#     for j in range(2, num[i]):
#         if num[i] % 2 == 0:
#             cnt += 1
#             num //= 2
        
#     if cnt == 0:
#         ans += 1

# print(ans)



# def solution(n, k):
#     num = ''
#     tmp = n
#     while tmp >= 1:
#         if tmp % k == 0:
#             num += '0'
#             tmp //= k

#         elif tmp % k != 0:
#             num += str(tmp % k)
#             tmp //= k

#     num = num[::-1].split('0')
#     ans = 0
#     for i in range(len(num)):
#         if num[i] == '':
#             num[i] = 0
            
#         num[i] = int(num[i])

#         cnt = 0
#         for j in range(2, num[i] + 1):
#             if cnt > 1:
#                 break

#             if num[i] % j == 0:
#                 cnt += 1

#         if cnt == 1:
#             ans += 1
#     answer = ans
#     return answer

# print(solution(110011, 10))


def is_seive(x):
    if x == 1:
        return 0
    
    for i in range(2, x):
        if i * i > x:
            break

        if x % i == 0:
            return 0

    return 1

def solution(n, k):
    num = ''
    tmp = n
    while tmp >= 1:
        if tmp % k == 0:
            num += '0'
            tmp //= k

        elif tmp % k != 0:
            num += str(tmp % k)
            tmp //= k

    num = num[::-1].split('0')
    answer = 0
    for i in range(len(num)):
        if num[i] == '':
            continue
            
        num[i] = int(num[i])

        answer += is_seive(num[i])

    return answer