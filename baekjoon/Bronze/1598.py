# 1598번_꼬리를 무는 숫자 나열

## 4줄짜리 표에 왼쪽부터 수를 아래로 1부터 순서대로 적어 나감
## 두 자연수 간 직각거리 구하기
## 11과 33은 직각거리 8


N1, N2 = map(int, input().split())

width = 0
length = 0

if N1%4 == 0 :
    width = 4
else :
    width = N1%4
    
for i in range(N2) :