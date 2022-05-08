n = int(input())

for i in range(n):
    arr = input()

    s = 0
    e = len(arr) - 1
    cnt = 0
    flag = False
    while s <= e:
        if arr[s] == arr[e]:
            s += 1
            e -= 1
            
        elif arr[s] != arr[e]:
            if arr[s+1:e+1] == arr[s+1:e+1][::-1]:
                flag = True
                break
            
            elif arr[s:e] == arr[s:e][::-1]:
                flag = True
                break
            
            else:
                cnt += 10000000
                break
            
            # if arr[s + 1] == arr[e]:
            #     flag = True
            #     s += 1
            #     cnt += 1
                
            # elif arr[s] == arr[e - 1]:
            #     flag = True
            #     e -= 1
            #     cnt += 1
                
            # else:
            #     flag = True
            #     s += 1
            #     e -= 1
            #     no += 1
            #     cnt += 1
                
        # elif flag and arr[s] != arr[e]:
        #     no += 1
        #     break
                
    if cnt == 0 and not flag:
        print(0)

    elif cnt == 0 and flag:
        print(1)

    elif cnt >= 10000000:
        print(2)    