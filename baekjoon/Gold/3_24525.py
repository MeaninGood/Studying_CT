import sys

input = lambda: sys.stdin.readline().strip()

arr = list(input())
n = len(arr)
sarr = [0 for _ in range(n)]
sarr[0] += arr[0] == 'S'
for i in range(1, n):
    sarr[i] = sarr[i - 1] + (arr[i] == 'S')
sarr + [0]

karr = [0 for _ in range(n)]
for i in range(n - 1)[::-1]:
    karr[i] = karr[i + 1] + (arr[i] == 'K')
    
s, e = n - 1, 0
mx = -1
print(sarr)
print(karr)
while s >= 0 and e < n - 1:
    if sarr[s] != 0 and karr[e] == sarr[s] * 2:
        tmps = sarr[s]
        while sarr[s] == tmps and s >= 0:
            s -= 1
            
        tmpk = karr[e]
        while karr[e] == tmpk and e < n - 1:
            e += 1
        mx = max(abs(s - e), mx)
        
    if karr[e] == sarr[s]:
        tmps = sarr[s]
        while sarr[s] == tmps and s >= 0:
            s -= 1
            
        tmpk = karr[e]
        while karr[e] == tmpk and e < n - 1:
            e += 1
            
    elif sarr[s] > karr[e]:
        e += 1
        
    else:
        s -= 1
    
print(mx)