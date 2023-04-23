from collections import deque


T = int(input())

for tc in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    order = []
    que = deque()
    for i in range(n):
        order.append(arr[i])

        if i == m:
            que.append([arr[i], 'target'])
        
        else:
            que.append([arr[i], 'not'])


    order = sorted(order)

    answer = 0
    while que:
        tmp = que.popleft()

        if order[-1] == tmp[0]:
            order.pop()
            answer += 1
            if tmp[1] == 'target':
                print(answer)
                break

        else:
            que.append(tmp)
