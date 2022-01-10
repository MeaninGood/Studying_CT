# 4344번_평균은 넘겠지

## 첫째 줄 테스트 케이스 개수 C
## 둘째 줄부터 각 테스트 케이스마다 학생의 수 N이 첫 수로 주어지고,
## 이어서 N명의 점수가 주어짐
## 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율 반올림, 소수점 셋째까지 출력

C = int(input())

for i in range(C) :
    N = list(map(float, input().split()))
    avg_score = sum(N[1:]) / N[0] # 리스트 sum으로 다 더하고 나누기
    
    stu_cnt = 0 # 학생 수 0으로 초기화
    for score in N[1:] :
        if score > avg_score :
            stu_cnt += 1
    
    rate = stu_cnt/N[0] * 100
    print(f'{rate:.3f}%')