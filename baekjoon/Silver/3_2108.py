n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()


print(round(sum(arr) / n))
print(arr[n // 2])

d = {}
for i in arr:
    d[i] = d.get(i, 0) + 1

td = list(d.items())
td.sort(key = lambda x: -x[1])

if len(td) > 1:
    if td[0][1] == td[1][1]:
        print(td[1][0])
    else:
        print(td[0][0])
        
elif len(td) == 1:
    print(td[0][0])

# mx = -100000
# for i in d:
#     if d[i] > mx:
#         mx = d[i]

# idx = -1
# for i in d:
#     if d[i] == mx and idx == -1:
#         idx = i
        
#     elif d[i] == mx and idx != -1:
#         idx = i
#         break

# print(idx)
        
print(arr[-1] - arr[0])




# if mx == 1:
#     if len(d) == 1:
#         print(arr[0])
#     elif len(d) > 1:
#         print(arr[1])

# elif mx != 1: