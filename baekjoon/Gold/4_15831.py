import sys

input = lambda: sys.stdin.readline().strip()

n, b, w = map(int, input().split())
arr = list(input()) + ['#']

s, e = 0, 0
cnt = {'W': arr[s] == 'W', 'B': arr[s] == 'B'}
length = 1
mx = 0
while e < n:
    if cnt['W'] >= w and cnt['B'] <= b:
        mx = max(mx, length)
        e += 1
        cnt['W'] += arr[e] == 'W'
        cnt['B'] += arr[e] == 'B'
        length += 1
        
        
    elif cnt['W'] < w:
        e += 1
        cnt['W'] += arr[e] == 'W'
        cnt['B'] += arr[e] == 'B'
        length += 1
        
    else:
        cnt['W'] -= arr[s] == 'W'
        cnt['B'] -= arr[s] == 'B' 
        s += 1
        length -= 1
    
print(mx)