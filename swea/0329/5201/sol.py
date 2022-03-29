T = int(input())

for tc in range(1, T + 1):

    n, m = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse = True) # 무게
    t = sorted(list(map(int, input().split())), reverse = True) # 트럭

    total = 0
    for i in range(n):
        if t != []:
            if t[0] >= w[i]:
                t.pop(0)
                total += w[i]
                
    print(f'#{tc} {total}')