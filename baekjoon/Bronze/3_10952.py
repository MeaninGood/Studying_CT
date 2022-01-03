# 10952번_A + B - 5

## 여러 개의 테스트 케이스 입력됨, 입력의 마지막에는 0 두개 들어옴
## While문으로 쓸 것



#C = [A+B while A&B != 0 if A&B == 0 break]

#print(*C)


while 1 :
    A, B = map(int, input().split())
    if A == 0 & B == 0 :
        break
    print(A+B)