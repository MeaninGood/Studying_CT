# 1051번_숫자 정사각형

## NN×M크기의 직사각형
## 각 칸에는 한 자리 숫자가 적혀 있음
## 꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램
## 이때, 정사각형은 행 또는 열에 평행


'''
# 첫째 줄에 N과 M
# N과 M은 50보다 작거나 같은 자연수
# 둘째 줄부터 N개의 줄에 수가 주어짐
## 첫째 줄에 정답 정사각형의 크기를 출력


(입력)
3 5
42101
22100
22101

(출력) 
9

'''
def square(d):
    while d > 1:
        for i in range(n-d+1):
            for j in range(m-d+1):
                x1, y1, x2, y2 = i, j, i+d-1, j+d-1
                
                if arr[x1][y1] == arr[x1][y2] == arr[x2][y1] == arr[x2][y2]:
                    return d**2
        d -= 1
    return 1
        
n, m = map(int, input().split())
arr = [list(map(int, input())) for i in range(n)]

d = min(n, m)
print(square(d))