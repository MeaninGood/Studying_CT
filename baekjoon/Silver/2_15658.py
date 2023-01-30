import sys
input = lambda : sys.stdin.readline().strip()



calc = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: x * y,
    lambda x, y: x // y if x > 0 else -(abs(x) // y)
]

def recur(cur, total):
    global mn, mx
    
    if cur == n - 1:
        mn = min(mn, total)
        mx = max(mx, total)
        return
    
    for i in range(4):
        if oper[i] > 0:
            oper[i] -= 1
            recur(cur + 1, calc[i](total, arr[cur + 1]))
            oper[i] += 1
        
    

n = int(input())
arr = list(map(int, input().split()))
oper = list(map(int, input().split()))

mn = 10 ** 9 + 1
mx = -(10 ** 9 + 1)

recur(0, arr[0])

print(mx)
print(mn)