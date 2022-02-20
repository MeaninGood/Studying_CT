import sys

def recur(s, e, p):
    # 중간 페이지
    m = (s+e) // 2
    # 중간 페이지 = 찾으려는 페이지
    if m == p:
        return 1 # 1 리턴

    # 중간 페이지가 찾으려는 페이지보다 작으면
    elif m < p:
        # 예를 들어 100페이지가 아닌 걸 알았으면
        # 1~99를 탐색해야지 왜 100을 다시 추가하는지는 모르겠으나
        # 문제대로 그냥 그대로 하였읍니다
        # cnt 값을 따로 받지 않고 +1씩 해주기
        return recur(m, e, p) + 1

    else:
        return recur(s, m, p) + 1

sys.stdin = open('input.txt')

n = int(input())
for tc in range(1, n + 1):
    page, pa, pb = map(int, input().split())

    a = recur(1, page, pa)

    b = recur(1, page, pb)

    if a > b :
        print(f'#{tc} B')
    elif a == b:
        print(f'#{tc} 0')
    else :
        print(f'#{tc} A')