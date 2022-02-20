import sys

arr = [[0]*10 for i in range(10)]

def cur(r1, c1, r2, c2, clr):
    cnt = 0 # 보라색 칸 카운트할 변수
    for i in range(r1, r2+1): # x 좌표의 범위
        for j in range(c1, c2+1): # y 좌표의 범위
            arr[i][j] += clr # 색상(숫자) 추가
            if arr[i][j] == 3: # 보라색이면
                cnt += 1 # 개수 카운트
    return cnt

sys.stdin = open('input.txt')
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    ans = 0 # ans 여기서 초기화해줘야 누적이 적용됨
    for i in range(n):
        r1, c1, r2, c2, clr = map(int, input().split())
        ans += cur(r1, c1, r2, c2, clr) # 보라색 생길 때마다 개수 누적

    print(f'#{tc} {ans}')
    arr = [[0] * 10 for i in range(10)] # 배열 초기화
