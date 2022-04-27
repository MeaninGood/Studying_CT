# import sys
# input = sys.stdin.readline

# def gcd(m, n):
#     if m < n:
#         m, n = n, m
    
#     if n == 0:
#         return m
    
#     if m % n == 0:
#         return n
    
#     else:
#         return gcd(n, m % n)

# a, k = map(int, input().split())

# d = [-1 for i in range(1000010)]

# d[1] = a
# for i in range(2, 1000010):
#     d[i] = d[i - 1] + k


# n = int(input())
# for _ in range(n):
#     a, b, c = map(int, input().split())
    
#     if a == 1:
#         print(sum(d[b : c + 1]))
        
#     elif a == 2:
#         if d[i] == 1:
#             print(1)
#             break
    
#         else:
#             for i in range(b, c + 1):
#                 cnt = 0
#                 for j in range(1, d[i + 1]):
#                     if j * j > d[i]:
#                         break
                    
#                     if d[i] % j == 0:
#                         cnt += 1
                        
#                 if cnt == 1:
#                     print(1)
#                     break
            
#             else:
#                 tmp = d[b]
#                 for i in range(b + 1, c + 1):
#                     tmp = gcd(tmp, d[i])
                            
#                 print(tmp)





# def gcd(m, n):
#     if m < n:
#         m, n = n, m
    
#     if n == 0:
#         return m
    
#     if m % n == 0:
#         return n
    
#     else:
#         return gcd(n, m % n)

# a, k = map(int, input().split())

# d = [-1 for i in range(1000010)]
# prefix = [-1 for i in range(1000010)]

# d[1] = a
# prefix[1] = a
# for i in range(2, 1000010):
#     d[i] = d[i - 1] + k
#     prefix[i] = prefix[i - 1] + d[i]

# n = int(input())
# for _ in range(n):
#     a, b, c = map(int, input().split())

#     if a == 1:
#         if b == 1:
#             print(prefix[c])
#         else:
#             print(prefix[c] - prefix[b - 1])
        
        
#     # elif a == 2:
#         # tmp = d[b]
#         # for i in range(b + 1, c + 1):
#         #     k = d[i]
#         #     while k % tmp != 0:
#         #          k, tmp = tmp, k % tmp
        
#     else:
#         tmp = d[b]
#         for i in range(b + 1, c + 1):
#             tmp = gcd(tmp, d[i])
                    
#         print(tmp)




def gcd(m, n):
    if m < n:
        m, n = n, m
    
    if n == 0:
        return m
    
    if m % n == 0:
        return n
    
    else:
        return gcd(n, m % n)



# d = [-1 for i in range(1000010)]

# d[1] = a

# for i in range(2, 1000010):
#     d[i] = d[i - 1] + k


a, d = map(int, input().split())
n = int(input())
for _ in range(n):
    qry, b, c = map(int, input().split())

    if qry == 1:
        sb = ((b - 1) * (2 * a + (b - 2) * d)) // 2
        sc = (c * (2 * a + (c - 1) * d)) // 2
        print(sc - sb)

    else:
        if b == c:
            print(a + (b - 1) * d)
        tmp = gcd(a, d)
                    
        print(tmp)
