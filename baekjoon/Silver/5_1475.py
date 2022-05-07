arr = list(map(int, input()))

d = {}
total = 0
for i in arr:
    if i == 6 or i == 9:
        total += 1
        
    else:
        d[i] = d.get(i, 0) + 1

mx = -10000    
for i in d:
    mx = max(mx, d[i])
    
tmp = 0
if total % 2:
    tmp = (total // 2) + 1


if total % 2 == 0:
    tmp = total // 2

if tmp > mx:
    print(mx + (tmp - mx))

elif tmp <= mx:
    print(mx)