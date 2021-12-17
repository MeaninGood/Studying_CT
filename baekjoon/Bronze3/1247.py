# 1047번_부호

## N개의 정수가 주어지면, 이 정수들의 합 S의 부호 출력.
## 총 3개의 테스트 셋, 첫째줄 N, S=0이면 "0", S>0이면 "+", S<0이면 "-" 출력


# 코드 1 - 시간 초과
## for i in range(3) :
    ## N = int(input())
    ## test_set = 0
    ## for i in range(N) :
        ## sum_value = int(input())
        ## test_set += sum_value
        
    ## if test_set == 0 :
        ## print("0")
    ## elif test_set > 0 :
        ## print("+")
    ## else :
        ## print("-")
        

# 코드2 - stdin.readline으로 입력 빠르게 받아오기

from sys import stdin

for i in range(3) :
    N = int(stdin.readline())
    test_set = 0 #초기 테스트셋 합 0으로 초기화
    for i in range(N) :
        sum_value = int(stdin.readline()) #정수 N에 따라 입력창 생성
        test_set += sum_value #테스트셋에 입력된 값 반복해서 더해줌
        
    if test_set == 0 :
        print("0")
    elif test_set > 0 :
        print("+")
    else :
        print("-")
    