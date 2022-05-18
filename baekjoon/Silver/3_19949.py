def recur(cur, prv1, prv2, total):
    global ans
    
    if cur == 10:
        if total >= 5:
            ans += 1
        return
    
    for i in range(1, 6):
        if prv1 == i and prv2 == i:
            continue
        
        if arr[cur] == i:
            recur(cur + 1, prv2, i, total + 1)
        
        else:
            recur(cur + 1, prv2, i, total)

arr = list(map(int, input().split()))
ans = 0
recur(0, 0, 0, 0)
print(ans)