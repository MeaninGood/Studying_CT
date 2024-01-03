import sys
input = lambda : sys.stdin.readline().strip()

arr = sorted(list(input()))
n = len(arr)

d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1

tmp = ''
is_odd = ''
for key in d.keys():
    if is_odd != '' and d[key] % 2:
        print("I'm Sorry Hansoo")
        exit()

    elif is_odd == '' and d[key] % 2:
        is_odd = key
    
    d[key] //= 2
    tmp += key * d[key]

print(tmp + is_odd + tmp[::-1])