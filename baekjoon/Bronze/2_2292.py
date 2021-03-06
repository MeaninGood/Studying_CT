# 2292번_다이얼

## 육각형의 벌집에서 중앙의 방이 1, 이웃하는 방에 돌아가면서
## 1씩 증가하는 번호를 주소로 매김.
## 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때
## 몇 개의 방을 지나가는지 계산하는 프로그램 작성

# 1씩 증가 / 1 = 1 / 6개씩 증가
# 2 = 2 ~ 7 (6개)
# 3 = 8 ~ 19 (12개)
# 4 = 18개

n = int(input())

room = 1 # 벌집(방) 갯수
cnt = 1 # 카운트는 1부터 시작

while n > room : # n이 벌집 갯수보다 클 때만 반복, 1일 때는 반복 x
    room += (cnt * 6) # 벌집 개수가 6의 배수로 증가함
    cnt += 1 # 벌집 6의 배수로 개수가 증가할 때의 로테이션 카운트

print(cnt)
