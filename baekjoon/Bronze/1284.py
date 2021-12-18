# 1284번_집 주소

## 호수판 제작, 각 숫자 사이에는 1cm의 여백이 들어감
## 1은 2cm, 0은 4cm, 나머지 숫자는 모두 3cm의 너비 차지
## 호수판의 경계와 숫자 사이에는 1cm의 여백이 들어가야 함


while True :
    N = input() #int가 아닌 문자열 그대로 들고 옴
    if N == '0' : #N에 0입력 시 수행문 종료
        break
    
    space = len(N)+1 #여백 미리 구해두기
    
    for i in N :
        if i == '0' :
            space += 4 #여백에 값 추가
        elif i == '1' :
            space += 2
        else :
            space += 3
    print(space)