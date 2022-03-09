# T = int(input())

# for tc in range(T):
#     p = input()
#     w = input()
    
#     if w not in p:
#         print('NO')
#         continue
    
#     li = []
#     for i in range(len(p)):
#         if p[i] == w:
#             li.append(i)
    
#     for j in range(len(li)):
#         if li[j] % 2 == 0:
#             print('YES')
#             break
#         elif j == len(li) - 1:
#             print('NO')


# T = int(input())

# for tc in range(T):
#     l, r, a = map(int, input().split())
    
#     # fa(x) = (x // 3) + (x % 3)
#     # l <= x <= r 일 때 최대값 출력
    
#     # for i in range(l, r+1):            
#     #     ans = max(ans, (i // a) + (i % a))
    
#     # print(ans)
#     # print((r-1) // a + (r-1) % a)
    
#     temp = a * ((r // a) - 1) + (a - 1)
#     if l <= temp <= r :
#         print(max(temp // a + temp % a, (r // a) + (r % a)))     
#     else:
#         print(r // a + r % a)
    
    # print((r // a) + (r % a))
    # a * ((r / x) - 1)
    # print(ans)
    
'''
5 10 3이면
나누기 모듈러 더한게
5 / 3 + 5 % 3 = 1 + 2 = 3
으로 시작해서
6은 2
7은 3
8은 4
3
2 3 4
3 4 5
4 5 6
5 6 7

'''





# T = int(input())

# for tc in range(T):
#     n, m = map(int, input().split())
    
#     li = []
#     for i in range(m):
#         x, w = map(int, input().split())
#         li.append((x, w))
        
#         li.sort(key=lambda x: x[0])
#         print(li)
        
        
        
        