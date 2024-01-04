import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split(' '))
arr = [list(map(int, input().split(' '))) for _ in range(n)]

st1, st2, st3 = [], [], []
for a, b, c in arr:
    st1.append(a)
    st2.append(b)
    st3.append(c)

ans = 1 << 31
for i in range(n):
    for j in range(n):
        for k in range(n):
            a, b, c = st1[i], st2[j], st3[k]
            
            cnt = 0
            for x, y, z in arr:
                
                if a >= x and b >= y and c >= z:
                    cnt += 1
            
                if cnt >= m:
                    ans = min(a + b + c, ans)
                    break

print(ans)