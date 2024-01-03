import sys
input = lambda : sys.stdin.readline().strip()

'''
양 한마리 사료 a그램
염소 한마리 사료 b그램
전체 양+염소 n마리
전체 소비된 사료 w그램

ax + b(n-x) = w

'''

a, b, n, w = map(int, input().split(' '))
ans = []
for i in range(1, n + 1 // 2):
    if (a * i) + b * (n - i) == w:
        ans.append([i, n - i])
    
if len(ans) > 1 or len(ans) == 0:
    print(-1)
else:
    print(*ans[0])
