import sys
<<<<<<< HEAD
=======

>>>>>>> 95d4d62deb7b7e8eeb97d9b665731a90f2865bdc
input = lambda : sys.stdin.readline().strip()

n, k = map(int, input().split())
arr = list(map(int, input().split()))
<<<<<<< HEAD

s, e = 0, 0
total = arr[0]
cnt = 1
mn = 1 << 31

while e < n:
    if total < k:
        cnt += 1
        e += 1
        total += arr[e]

    elif total >= k:
        mn = min(cnt, mn)
        
=======
arr += [0]

s, e = 0, 0 
total = arr[s]
length = 1
cnt = 0
ans = 1 << 31
while e < n:
    if total >= k:
        cnt += 1
        ans = min(length, ans)
        total -= arr[s]
        s += 1
        length -= 1
        
    else:
        e += 1
        total += arr[e]
        length += 1
        

print(ans if cnt else 0)
>>>>>>> 95d4d62deb7b7e8eeb97d9b665731a90f2865bdc
