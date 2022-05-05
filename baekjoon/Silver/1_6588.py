sieve = [True for i in range(1000010)]
sieve[0] = False
sieve[1] = False
for i in range(2, 1000010):
    if not sieve[i]:
        continue
    
    for j in range(i * i, 1000010, i):
        sieve[j] = False

while 1:
    n = int(input())

    if n == 0:
        break

    a = 0
    b = 0    
    for i in range(2, n + 1):
        if sieve[i] and sieve[n - i]:
            a = i
            b = n - i
            break

    if a == 0 and b == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(f'{n} = {a} + {b}')












# while 1:
#     n = int(input())

#     if n == 0:
#         break
    
#     sieve = [True for i in range(n + 1)]
#     sieve[0] = False
#     sieve[1] = False
#     for i in range(2, n + 1):
#         if not sieve[i]:
#             continue
        
#         for j in range(i * i, n + 1, i):
#             sieve[j] = False

#     a = 0
#     b = 0    
#     for i in range(2, (n + 1) // 2):
#         if sieve[i] and sieve[n - i]:
#             a = i
#             b = n - i
#             break

#     if a == 0 and b == 0:
#         print("Goldbach's conjecture is wrong.")
#     else:
#         print(f'{n} = {a} + {b}')