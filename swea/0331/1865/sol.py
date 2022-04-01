'''
& => and                비트를 끌 때 사용, 켜져있는지 확인
|   => or                   비트를 킬 때 사용
^ => xor                 비트를 반전시킬 때 사용
~ => not
111010001

000101110 & (1 << 2)
111010011
000000100
111111011
000000000

00000110010
00000000010

3번 위치를 키고 싶다? => visit |= (1 << 3) => 원래 꺼져있든 아니든 하고 나면 켜진다.
3번 위치가 켜져 있나? => visit & (1 << 3) => 0이면 꺼져있다. 0이 아니면(1 << 3이면) 켜져있다.
3번 위치를 끄고 싶다? => visit &= ~(1 << 3) => 3번 위치를 끈다. 원래 켜져 있든 아니든 연산 후에는 꺼진다.
3번 위치가 켜져 있으면 끄고, 꺼져 있으면 키고 싶다? => visit ^= (1 << 3) => 그 비트만 뒤집힌다.

N 제한이 작으면 백트래킹이 됨
N이 15~20으로 나오면 비트마스킹
순열 문제인데 N제한이 15~20개면 비트마스킹 쓰라는 얘기
'''


def recur(cur, visit):
    if cur == n:
        return 1

    if dp[cur][visit] != -1:
        return dp[cur][visit]

    ret = 0
    for i in range(n):
        if (visit & (1 << i)) != 0:
            continue
        # if visited[i]:
        #    continue

        # visit |= 1 << i
        # visited[i] = True
        ret = max(ret, recur(cur + 1, visit | (1 << i)) * arr[cur][i] / 100)
        # visited[i] = False
        # visit &= ~(1 << i)
        # visit ^= 1 << i

    dp[cur][visit] = ret
    return ret


T = int(input())

for t in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    visited = [False for i in range(n)]
    dp = [[-1 for i in range(1 << n)] for j in range(n)]

    print(recur(0, 0) * 100)