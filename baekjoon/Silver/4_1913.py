# 1913번_달팽이

## 홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채우기
## N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성
## 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력
## 예를 들어 N=5인 경우 6의 좌표는 (4,3)

'''
# 첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)
# 둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어짐
## N개의 줄에 걸쳐 표를 출력
## 각 줄에 N개의 자연수를 한 칸씩 띄어서 출력, 자릿수를 맞출 필요 x
## N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력

(입력)
7
35

(출력)
49 26 27 28 29 30 31
48 25 10 11 12 13 32
47 24 9 2 3 14 33
46 23 8 1 4 15 34
45 22 7 6 5 16 35
44 21 20 19 18 17 36
43 42 41 40 39 38 37
5 7

'''

n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
num = int(input())


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

x = 0
y = 0
dir = 0
for i in range(1, n * n + 1)[::-1]:
    arr[x][y] = i
        
    nx = x + dx[dir] # 임시로 가보는 애들
    ny = y + dy[dir] # 얘네가 봤을 때 갈 수 있으면
    # 이 조건문에 걸리지 않으면
    if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] != 0:
        dir = (dir + 1) % 4
    # 실제 x 와 y값을 바꿔준다
    x += dx[dir]
    y += dy[dir]

for j in range(n):
    print(*arr[j])
    
for k in range(n):
    for l in range(n):
        if arr[k][l] == num:
            print(k+1, l+1)
print(arr)

# n = int(input())
# arr = [([0]*n) for j in range(n)]
# num = int(input())

# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]

# x = 0
# y = 0
# dir = 0
# for i in range(1, n * n + 1):
#     arr[x][y] = i
    
#     nx = x + dx[dir]
#     ny = y + dy[dir]
    
#     if not (0 <= nx < n and 0 <= ny < n) or arr[nx][ny] != 0 :
        
# print(arr)


