d = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


# arr = [[] for _ in range(8)]
# for i in range(8):
#     for j in range(1, 9):
#         tmp = chr(65 + i) + str(j)
#         arr[i].append(tmp)
    
k, a, n = map(str, input().split())
y1, x1 = k[0], int(k[1])
y2, x2 = a[0], int(a[1])

for i in range(int(n)):
    move = input()

    for j in range(8):
        if move == d[j]:
            if not (65 <= ord(y1) + dy[j] <= 72 and 1 <= x1 + dx[j] <= 8):
                continue
            
            nx1 = x1 + dx[j]
            ny1 = chr(ord(y1) + dy[j])
            
            if nx1 == x2 and ny1 == y2:
                if not (65 <= ord(y2) + dy[j] <= 72 and 1 <= x2 + dx[j] <= 8):
                    continue
                
                x2 = x2 + dx[j]
                y2 = chr(ord(y2) + dy[j])
                
            x1 = nx1
            y1 = ny1
              
print(y1+str(x1), y2+str(x2), sep = '\n')
