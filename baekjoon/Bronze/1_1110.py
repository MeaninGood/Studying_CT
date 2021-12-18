# 1110번_더하기 사이클

## 0 < N < 99의 정수, 사이클 길이 출력
## 26으로 시작한다면 2+6 = 8, 새로운 수 68
## 68은 다시 6+8=14, 새로운 수 84
## 84는 다시 8+4=12, 새로운 수 42
## 42는 다시 4+2=6, 새로운 수 26
## 위 예는 4번 만에 원래 수로 돌아옴. 사이클 길이 4


N = int(input())

cycle_len = 0
cycle = 0
new_num = 0

while True :
    cycle = (N//10) + (N%10)
    new_num = ((N%10)*10) + (cycle%10)
    cycle_len += 1

    if new_num == N :
        break

print(cycle_len)