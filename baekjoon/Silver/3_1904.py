'''
n = 0 // 0 : 0
n = 1 // 1 : 1
n = 2 // 11 00 : 2
n = 3 // 111 100 001 : 3
n = 4 // 1111 1100 0011 1001 0000 : 5
n = 5 // 00001 00100 10000 11001 10011 00111 11111 11100 : 8

'''
n = int(input())

if n == 1:
    print(1)
if n == 2:
    print(2)
if n == 3:
    print(3)
if n > 3:
    print(n - 1 + n - 2)
