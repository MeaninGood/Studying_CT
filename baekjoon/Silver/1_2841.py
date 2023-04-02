import sys
input = lambda : sys.stdin.readline().strip()

n, p = map(int, input().split())
st = [[] for _ in range(7)]

cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    
    if st[a] and b == st[a][-1]:
        continue

    elif st[a] and b < st[a][-1]:
        while st[a]:
            if st[a][-1] <= b:
                break
            st[a].pop()
            cnt += 1

    if st[a] and b == st[a][-1]:
        continue
    
    else:
        st[a].append(b)
        cnt += 1
        
print(cnt)