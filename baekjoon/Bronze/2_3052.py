# 8958번_OX퀴즈

## "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점
## 정답 시 그 문제까지 연속된 O의 개수가 점수
## OX퀴즈 결과 주어졌을 때, 점수 구하는 프로그램 작성


N = int(input())

for _ in range(N) :
    result = list(input())
    
    count = 0
    score = 0
    for i in result :
        if i == 'O' :
            count += 1
            score += count
        
        else :
            count = 0
        
    print(score)