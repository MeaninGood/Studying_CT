n, m = map(int, input().split())
x = y = d = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# d + 1 좌회전
# d + 3 우회전 
# d + 2 는 무조건 뒤 도는 것!

for i in range(m):
    a, b = map(str, input().split())
    b = int(b)
    
    
    if a == 'MOVE':
        x += b * dx[d]
        y += b * dy[d]
    
    else:
        if b == 0:
            d = (d + 1) % 4
        else:
            d = (d + 3) % 4


            


