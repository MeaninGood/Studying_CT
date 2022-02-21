T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(100)]
    
    dx = [0, -1, 0, -1]
    dy = [-1, 0, 1, 0]

    idx = 0
    for i in range(100):
        if arr[99][i] == 2:
            idx = i
            break
        
    x = 99
    y = idx

    # while x > 0:
    #     moved = False
    #     while y > 0 and arr[x][y - 1] == 1:
    #         y -= 1
    #         moved = True
    #     while not moved and y < 99 and arr[x][y + 1] == 1:
    #         y += 1
    #     x -= 1
        
    d = 1
    while x > 0:
        for i in range(1, 4, 2):
            nx = x + dx[(d + i) % 4]
            ny = y + dy[(d + i) % 4]
            
            if 0 <= nx < 100 and 0 <= ny < 100 and arr[nx][ny] == 1:
                d = (d + i) % 4
                break
        # nx = x + dx[(d + 1) % 4]
        # ny = y + dy[(d + 1) % 4]
        
        # if arr[nx][ny] == 1:
        #     d = (d + 1) % 4

        # else:
        #     nx = x + dx[(d + 3) % 4]
        #     ny = y + dy[(d + 3) % 4]
            
        #     if arr[nx][ny] == 1:
        #         d = (d + 3) % 4    
        
        x += dx[d]
        y += dy[d]
    print(y)