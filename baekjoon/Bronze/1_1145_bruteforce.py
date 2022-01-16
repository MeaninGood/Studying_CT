# 1145번_적어도 대부분의 배수(brute force)

## 적어도 대부분의 배수는 5개의 자연수 중 적어도 세 개로 나누어지는 가장 작은 자연수
## 서로 다른 다섯 개의 자연수 주어질 때, 적어도 대부분의 배수 출력
## 30 42 70 35 90 => 210


N = list(map(int, input().split()))

min_num = min(N) #1부터 볼 필요x, N의 최소값에서 부터 1씩 증가시키며 확인할 것

while True :
    count = 0 #초기 카운트 0
    for i in range(5) :
        if min_num % N[i] == 0 : #min_num에서 N의 값들 중 나누어 떨어지는 것이 있다면
            count += 1 #카운트를 1씩 증가시켜 줌
    
    if count > 2 : #카운트가 2를 초과하면 min_num값 출력하고 멈춤
        print(min_num)
        break

    min_num += 1 #min_num을 1씩 증가시킴