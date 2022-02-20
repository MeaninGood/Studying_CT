dx = [0, -1, 0, -1]
dy = [-1, 0, 1, 0]

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for i in range(100)]
    
    # print(arr)
    
    idx = 0
    for i in range(100):
        if arr[99][i] == 2 :
            idx = i
            break

    print(idx)
    
x = 99
y = idx
d = 1
while x > 0 :
    
    for i in range(1, 4, 2):