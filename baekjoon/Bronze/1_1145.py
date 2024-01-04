arr = list(map(int, input().split(' ')))

mn = 1
while 1:
    cnt = 0
    
    for i in range(5):
        if mn % arr[i] == 0:
            cnt += 1
            
    if cnt >= 3:
        print(mn)
        break
    
    mn += 1