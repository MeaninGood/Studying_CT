import sys
input = sys.stdin.readline

a, b = map(int, input().split())

ans = 0
for i in range(a, b + 1):
    # 소수의 개수 구하기
    x = i
    cnt = 0
    for j in range(2, i + 1):
        if j * j > i:
            break
        
        while x % j == 0:
            cnt += 1
            x //= j
    
    if x != 1:
        cnt += 1
    # print(i, cnt)
    # 소수 판정하기
    tmp = 0
    for k in range(2, cnt + 1):
        if k * k > cnt:
            break
        
        if cnt % k == 0:
            tmp += 1
            
    if cnt > 1 and tmp == 0:
        ans += 1
        
print(ans)
    