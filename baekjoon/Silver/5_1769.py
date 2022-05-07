n = list(map(str, input()))

total = ''
arr = n
cnt = 0
if len(n) > 1:
    while len(total) != 1:
        tmp = 0
        for i in arr:
            tmp += int(i)
        
        total = str(tmp)
        arr = list(map(str, total))
        cnt += 1
    
    print(cnt)
    print('YES' if int(total) % 3 == 0 else 'NO')

else:
    print(0)
    print('YES' if int(n[0]) % 3 == 0 else 'NO')