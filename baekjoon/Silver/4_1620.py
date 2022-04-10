import sys
input = sys.stdin.readline

n, m = map(int, input().split())

d = {}
for i in range(1, n + 1):
    a = input().rstrip()
    d[a] = d.get(a, str(i))

d2 = {}

for key, value in d.items():
    d2[value] = d2.get(value, key)


for j in range(m):
    b = input().rstrip()
    
    if b in d:
        print(d[b])
    
    elif b in d2:
        print(d2[b])
    
    # for key, value in d.items():
    #    if b == key:
    #        print(value)
    #        break
       
    # for key, value in d2.items():
    #     if b == key:
    #         print(value)
    #         break 

# for j in range(m):
#     b = input().rstrip()
    
#     if int(b) == type(int):
#         b = int(b)
#         for key, value in d.items():
#             if b == value:
#                 print(key)
#                 break
#             print(key)
#             print(value)
#             print(f'#{key}, @{value}, %{b}')
    
    # print(b)
    # for key, value in d.items():
    #     # print(key)
    #     # print(value)
    #     # print(f'#{key}, @{value}, %{b}')
    #     if b == key:
    #         print(value)
    #         break
        
        # elif int(b) == value:
        #     print(key)
        #     break


