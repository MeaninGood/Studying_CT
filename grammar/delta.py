# 5x5 배열 


arr = [list(map(int, input().split())) for i in range(5)]


for i in range(5):
    for j in range(5) :
        if arr[i][j] < arr[i]