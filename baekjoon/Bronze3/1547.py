# 1547번_공

## 컵 3개 중 1번 컵 아래에 공 넣어 놓고 컵 위치 바꾸기
## 공의 위치는 변하지 않음, 컵만 바꾸기
## 컵의 위치 M번 바꾼 후 공이 들어있는 컵의 번호 구하기

M = int(input())

cups = [1, 2, 3] #컵이 3개라고 정의되어 있으므로 순서대로 1번컵, 2번컵, 3번컵

for i in range(M) :
    X, Y = map(int, input().split()) 
    
    cups_X = cups.index(X) #입력된 x와 y 값을 cups 리스트의 인덱스 번호로 지정
    cups_Y = cups.index(Y)
    
    cups[cups_X], cups[cups_Y] = cups[cups_Y], cups[cups_X] #컵 위치 바꾸기
    
print(cups[0])
    
    
    