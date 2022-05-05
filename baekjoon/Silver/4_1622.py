while True:
    try:
        arr1 = list(map(str, input()))
        arr2 = list(map(str, input()))
        
    except:
        break
    
    n = len(arr1)
    m = len(arr2)

    d1 = {}
    for i in range(n):
        d1[arr1[i]] = d1.get(arr1[i], 0) + 1

    d2 = {}
    for i in range(m):
        d2[arr2[i]] = d2.get(arr2[i], 0) + 1
        
    ans1 = []
    ans2 = []

    for i in d1:
        ans1.append([i, d1[i]])

    for i in d2:
        ans2.append([i, d2[i]])
        
    ans1.sort()
    ans2.sort()
    ans1.sort(key=lambda x: -x[1])
    ans2.sort(key=lambda x: -x[1])

    res = []
    for i in range(len(ans1)):
        for j in range(len(ans2)):
            if ans1[i][0] == ans2[j][0]:
                if ans1[i][1] != ans2[j][1]:
                    res += ans1[i][0] * min(ans1[i][1], ans2[j][1])
                else:
                    res += ans1[i][0] * ans1[i][1]
    res = list(res)
    res.sort()
    print(*res, sep='')