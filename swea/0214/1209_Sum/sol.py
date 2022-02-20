import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    ans = 0
    # 행의 합 구하기
    for i in range(100):
        temp1 = 0
        for j in range(100):
            temp1 += arr[i][j]

            if temp1 > ans :
                ans = temp1

    # 열의 합 구하기
    for j in range(100):
        temp2 = 0
        for i in range(100):
            temp2 += arr[i][j]

            if temp2 > ans:
                ans = temp2

    # 대각선 우하향 합 구하기
    temp3 = 0
    for i in range(100):
        temp3 += arr[i][i]

    if temp3 > ans:
        ans = temp3

    # 대각선 좌하향 합 구하기

    temp4 = 0
    for i in range(100):
        for j in range(0, 100, -1):
            temp4 += arr[i][j]

    if temp4 > ans:
        ans = temp4

    print(f'#{tc} {ans}')