n = int(input())

cnt = 0
for i in range(10000010):     
    if '666' in str(i):
        cnt += 1
        
    if cnt == n:
        print(str(i))
        break
