# 1259번_팰린드롬수

## 어떤 단어를 뒤에서부터 읽어도 똑같다면 팰린드롬.
## 숫자 입력 시 팰린드롬이면 yes, 아니면 no 출력.
## 입력의 마지막 줄에는 0이 주어지며, 문제에 포함되지 않음.
## 121 -> yes, 1231 -> no, 10 -> no

while True : #0이 입력될 때까지 계속 입력창이 생성되어야 하므로 while True 씀
    num = input() #정수형x, 문자형 그대로 받기
    if num == '0' : 
        break #0이 입력되면 중지

    if num == num[::-1] : #입력된 수를 뒤에서부터 입력한 것과 같다면
        print('yes') #'yes' 출력
    
    else :
        print('no') #다르면 'no' 출력