n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]

nums = []
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or i == k:
                continue
            
            nums.append([str(i), str(j), str(k)])

ans = nums[:]
for target, stk, ball in arr:
    tmp = list(str(target))
    
    for num in nums:
        nstk, nball = 0, 0
        
        for i in range(3):
            if num[i] == tmp[i]:
                nstk += 1
            elif tmp[i] in num:
                nball += 1
                
        if (nstk != stk or nball != ball) and num in ans:
            ans.remove(num)

print(len(ans))