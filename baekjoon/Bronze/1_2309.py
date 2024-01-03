arr = [int(input()) for _ in range(9)]

for a in range(9):
    for b in range(a + 1, 9):
        for c in range(b + 1, 9):
            for d in range(c + 1, 9):
                for e in range(d + 1, 9):
                    for f in range(e + 1, 9):
                        for g in range(f + 1, 9):
                            tmp = [arr[a], arr[b] , arr[c] , arr[d] , arr[e] , arr[f] , arr[g]]
                            if sum(tmp) == 100:
                                tmp.sort()
                                                                
                                for k in tmp:
                                    print(k)
                                exit()