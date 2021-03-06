def in_order(n):
    global ans
    # n이 0에서 노드 개수 사이일 때
    if 0 < n <= v:
        # 방문처리가 되어있지 않다면
        if not visited[n]:
            # 1로 시작해서 2 -> 4 -> 8 ... 순서로 호출
            in_order(n * 2)
            # 방문처리 해주기
            visited[n] = True
            # 문자열 합쳐주기
            ans.append(tree[n])
            # 3 -> 5 -> 9 ... 순서로 호출
            in_order(n * 2 + 1)

T = int(input())
for tc in range(1, T):
    v = int(input())
    ans = []
    tree = [0]
    visited=[False for _ in range(v + 1)]
    for i in range(v):
        tree.append(input().split()[1])

    in_order(1)

    print(f'#{tc} {ans}')