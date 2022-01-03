# 10951번_A + B - 4

## 여러 개의 테스트 케이스 입력됨
## While문으로 쓸 것

while 1 :
    try :
        A, B = map(int, input().split())
        0 < A & B < 10
        print(A+B)
        
    except :
        break
    
## try - except-else-finally 구문 이용하기 (공부 더 할 것!)
## 시작하고 끝나는 지점이 없기 때문에 try - except 써주지 않으면 무한루프
## 조건에서 벗어날 때(혹은 에러일 때) except 구문으로 탈출하게끔 하는 것


# for문을 이용한 구문은 아래와 같다
import sys
for line in sys.stdin :
    A, B = map(int, line.split())
    print(a+b)
## sys.stdin은 ^Z를 입력받으면 종료됨.