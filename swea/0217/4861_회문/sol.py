# 열 기준으로 배열 만들어줄 함수
def c_arr(arr):
    c_arr = []
    temp = []
    for i in range(8):
        for j in range(8):
            temp.append(arr[j][i])  # 열 인덱스 기준으로 새로운 배열 생성
        if len(temp) == 8:
            c_arr.append(temp)
            temp = []
    return c_arr

# 펠린드롬인지 체크해줄 함수
def is_Pal(arr):
    s = 0  # 시작 인덱스
    e = n  # 끝 인덱스
    i = 0  # 행
    cnt = 0  # 펠린트롬 카운트
    while i != 8:  # i가 7일 때 까지만 체크
        if arr[i][s:e] == arr[i][s:e][::-1]:  # i행의 arr[s:e]가 뒤집은 것과 같으면
            cnt += 1  # 카운트 +1
            s += 1  # 시작 인덱스 +1
            e += 1  # 끝 인덱스 +1
        elif arr[i][s:e] != arr[i][s:e][::-1]:  # 뒤집은 것과 다르면
            s += 1  # 카운트 하지 않고 시작, 끝 인덱스만 +1
            e += 1

        if s == 9 - n:  # 한 행을 다 확인하면
            s = 0  # 다음 행의 처음부터 탐색하기 위해 0으로 초기화
            e = n  # e도 n으로 초기화
            i += 1  # 행 +1

    return cnt


t = 10
for tc in range(1, t + 1):
    n = int(input())
    li = []
    for _ in range(8):
        li.append(list(input()))

    new = c_arr(li)
    print(f'#{tc} {is_Pal(new) + is_Pal(li)}')

    # print(arr[0][1:5], arr[0][1:5][::-1])
