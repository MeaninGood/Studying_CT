# 1009번_분산처리

## 테스트 케이스 T가 주어지고, 총 데이터의 개수는 a**b의 형태
## 1번 데이터 - 1번 컴퓨터, 2번 데이터 - 2번 컴퓨터, 11번 데이터 - 1번 컴퓨터 ...
## 마지막 데이터가 처리될 컴퓨터의 번호 출력


# 코드1 - 시간 초과
### T = int(input())

### for i in range(T) :
    ### a, b = map(int, input().split())
    ### print(a**b%10)


# 코드2 - 분산 처리

## 제곱 수의 끝자리 구하기 
## [1 : 1], [2 : 2, 4, 8, 6], [3 : 3, 9, 7, 1], [4 : 4, 6], [5 : 5], [6 : 6],
## [7 : 7, 9, 3, 1], [8 : 8, 4, 2, 6], [9 : 9, 1]

T = int(input())

for i in range(T) :
    a, b = map(int, input().split())
    num = a % 10
    
    if num == 0 :
        print(10)
    elif num == 1 or num == 5 or num == 6 :
        print(num)
    elif num == 4 or num == 9 :
        if b%2 == 0 :
            print(num**2%10)
        else :
            print(num)
    else :
        if b%4 == 0 :
            print(num**4%10)
        else :
            print(num**(b%4)%10)