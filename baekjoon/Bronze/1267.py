# 1267번_핸드폰요금

## 영식 요금제 : 30초마다 10원씩 청구
## 만식 요금제 : 60초마다 15원씩 청구
## 통화 시간 목록이 주어지면 어느 요금제를 사용하는 것이 저렴한지 출력


N = int(input())
call = list(map(int, input().split()))

Y = [] #각 시간별로 따로따로 요금을 계산해야 하기 때문에 리스트 만들어 줌
M = []
for i in range(N) :
    Y.append(((call[i]//30)+1)*10) #리스트에 계산한 값 추가하기
    M.append(((call[i]//60)+1)*15)

if sum(Y) < sum(M) : #리스트별 합의 대소 비교로 원하는 값 출력
    print("Y %d"%sum(Y))
elif sum(Y) == sum(M) :
    print("Y M %d"%sum(M))
else :
    print("M %d"%sum(M))
    


