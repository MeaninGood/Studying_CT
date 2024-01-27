import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = [input() for _ in range(n)]

pprefix = [0 for _ in range(n)]
pprefix[0] += arr[0] == 'P'
sprefix = [0 for _ in range(n)]
sprefix[0] += arr[0] == 'S'
hprefix = [0 for _ in range(n)]
hprefix[0] += arr[0] == 'H'


for i in range(1, n):
    pprefix[i] = pprefix[i - 1] + (arr[i] == 'P')
    sprefix[i] = sprefix[i - 1] + (arr[i] == 'S')
    hprefix[i] = hprefix[i - 1] + (arr[i] == 'H')
    
psuffix = [0 for _ in range(n)]
psuffix[-1] += arr[-1] == 'P'
ssuffix = [0 for _ in range(n)]
ssuffix[-1] += arr[-1] == 'S'
hsuffix = [0 for _ in range(n)]
hsuffix[-1] += arr[-1] == 'H'

for i in range(n - 1)[::-1]:
    psuffix[i] = psuffix[i + 1] + (arr[i] == 'P')
    ssuffix[i] = ssuffix[i + 1] + (arr[i] == 'S')
    hsuffix[i] = hsuffix[i + 1] + (arr[i] == 'H')

ans = 0
for i in range(n):
    p, s, h = pprefix[i], sprefix[i], hprefix[i]
    mx = max(p, s, h)
    
    if i == n - 1:
        ans = max(ans, mx)
        break
    
    if p == mx:
        tmpmx = max(ssuffix[i + 1], hsuffix[i + 1])
        ans = max(ans, p + tmpmx)
        
    if s == mx:
        tmpmx = max(psuffix[i + 1], hsuffix[i + 1])
        ans = max(ans, s + tmpmx)
        
    if h == mx:
        tmpmx = max(psuffix[i + 1], ssuffix[i + 1])
        ans = max(ans, h + tmpmx)
        
print(ans)