# n = 16


# # [True, True, True, True, True, True, True, True, True, True, True]

# sieve = [True] * (n + 1)
# # print(sieve)
# i = 2
# while i * i <= n:
#     if not sieve[i]: # False면 continue
#         i += 1
#         continue
#         # pass
#     for j in range(i * i, n + 1, i): # 2*2, 11, 2 // 2간격으로 다 지우기 -> 3*3, 11, 3 // 3간격으로 다 지우기
#         sieve[j] = False # 다 False로 바꿔줌
#     i += 1 # i 1씩 증가시킴
#     print(i)


# li = [i for i in range(2, n+1) if sieve[i] == True]
# # print(sieve)
# print(li)
      
n = 16
i = 2
sieve = [True] * (n + 1)   
for i in range(2, n + 1):
    if i * i > n:
        break
    
    if not sieve[i]:
        continue

    for j in range(i * i, n + 1, i):
        sieve[j] = False
      
li = [k for k in range(2, n+1) if sieve[k] == True]

print(li)