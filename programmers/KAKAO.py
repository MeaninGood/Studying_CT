
    for i in range(len(privacies)):
        a, b, c, d = privacies[i[:4]], privacies[i[5:7]], privacies[i[8:10]], privacies[i[-1]]
        a, b, c = int(a), int(b), int(c)

        x, y, z = 0, 0, 0
        if c - 1 < 1:
            z = 28
            b -= 1
        
        if c - 1 > 1:
            z = c - 1
            
        if b - dt[d] < 1:
            tmp1 = dt[d] - b
            y = 12 - tmp1
            a -= 1

        """
        1 -> -2 : 11월 12월 - 1
        1 -> -3 : 10월 12월 - 2
        5 -> -11 : 6 12월 - 월
        11 - 5에서 12 - 6
        4 -> -7 : 9월  12월 - 3월
        7 - 4에서 12 - 3

        """

        if b - 1 > 1:
            y = b - 1

        x = a - 1

        tmp3 = today.split(".")
        print(tmp3)
        idx = tmp3[0] + tmp3[1] + tmp3[2]
        print(idx)
        # if int(a + b + c) < idx:
        #     answer.append()


# tmp = int(a + b + c)
        # tmp2 = tmp + ((28 * dt[d]) - 1)
        # tmp2 = str(tmp2)
        # a, b, c = int(tmp2[:4]), int(tmp2[4:6]), int(tmp2[6:])
        # print(a, b, c)
        # x, y, z = 0, 0, 0
        # z1, z = ((c - 1) // 28), ((c - 1) % 28) + 1
        # print(z)
        # y1, y = ((z1 + b) // 12), ((z1 + b) % 28) + 1

        # x = a - (y1 // 12)

        # print(x, y, z)

        # if idx > tmp2:
        #     answer.append(i + 1)
        # print(idx, tmp2)









from collections import deque
import heapq

def solution(n, m, x, y, r, c, k):
    global total
    answer = 'impossible'
    """
    x좌표, y좌표, 개수, 경로
    """

    total = set()
    
    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m

    # 우, 하, 좌, 상, r, d, l, u
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    def bfs(x, y, cnt, tmp):

        que = deque()
        visited = set()
        que.append([x, y, cnt, tmp])
        while que:
            size = len(que)

            for _ in range(size):
                x, y, cnt, tmp = que.popleft()
                # print(x, y, cnt, tmp, visited)

                if cnt > k:
                    continue

                if arr[x][y] == "E" and cnt == k:
                    if tmp not in total:
                        total.add(tmp)
                        break

                for d in range(4):
                    nx = x + dx[d]
                    ny = y + dy[d]

                    if not in_range(nx, ny):
                        continue
                    # r, d, l, u
                    dirt = '#'
                    if d == 0:
                        dirt = 'r'

                    elif d == 1:
                        dirt = 'd'

                    elif d == 2:
                        dirt = 'l'

                    else:
                        dirt = 'u'
                    tmp2 = tmp + dirt
                    
                    if cnt + 1 > k:
                        continue

                    que.append([nx, ny, cnt + 1, tmp2])
                    # visited.add(tmp2)
                        


    arr = [['.' for _ in range(50)] for _ in range(50)]
    visited = [[False for i in range(50)] for j in range(50)]

    arr[x - 1][y - 1] = 'S'
    arr[r - 1][c - 1] = 'E'

    bfs(x - 1, y - 1, 0, "")

    # print(total)

    tmp = sorted(list(total))
    
    if len(tmp) > 0:
        answer = tmp[0]
    return answer






    # total = cap
    # arr = []
    # for i in range(n)[::-1]:

    #     total -= deliveries[i]
    #     total += pickups[i]
    #     print(total, deliveries[i], pickups[i])
    #     if total > cap:
    #         arr.append(i + 1)
    #         total = cap
    #         total -= deliveries[i]
    #         total += pickups[i]

    # print(arr)

 tmp_del = deliveries[:]
    tmp_pick = pickups[:]
    for i in range(cap + 1):
        total = i
        mx = 0
        while total <= i:
            idx = 1
            for j in range(n):
                total -= delievers[j]
                total += pickups[j]
                
                if total > i:
                    idx = j
                    break

            mx = max(mx, )

















""


# 1
def solution(today, terms, privacies):
    answer = []

    dt = {}
    for i in terms:
        a, b = i.split(" ")
        dt[a] = int(b)

    n = len(privacies)
    idx = today.split(".")

    for i in range(n):
        a, b, c, d = privacies[i][:4], privacies[i][5:7], privacies[i][8:10], privacies[i][-1]
        x, y, z = (int(a) * 28 * 12), (int(b) * 28), int(c)
        tmp = (x + y + z) + (28 * dt[d]) - 1

        x1, y1, z1 = (int(idx[0]) * 28 * 12), (int(idx[1]) * 28), int(idx[2])
        tmp2 = x1 + y1 + z1

        if tmp < tmp2:
            answer.append(i + 1)


    return answer


# 2
def solution(cap, n, deliveries, pickups):
    answer = -1

    arr = [0 for i in range(n)]
    visited = [False for i in range(n)]
    for i in range(n):
        arr[i] = pickups[i] - deliveries[i]

    tmp = [n]
    present = cap
    truck = 0
    for i in range(n)[::-1]:
        if arr[i] < 0:
            if present - arr[i] > 0:
                present -= arr[i]

        if arr[i] > 0:
            truck += arr[i]
            
        elif 

        

    return answer


# 3
from itertools import combinations


def solution(users, emoticons):
    global comb
    answer = []

    n = len(users)
    m = len(emoticons)

    arr = [0 for i in range(m)]
    comb = []
    def recur(cur):
        global comb
        if cur == m:
            tmp = arr[:]
            comb.append(tmp)
            return

        for i in [90, 80, 70, 60]:
            arr[cur] = i
            recur(cur + 1)

    recur(0)

    def get_discnt(emo, com):
        for i in range(len(emo)):
            emo[i] = emo[i] * com[i] // 100

        return emo

    total = 0
    cnt = 0
    li = []
    for i in range(len(comb)):
        emo = emoticons[:]
        tmp = get_discnt(emo, comb[i])

        tmp_total = 0
        tmp_cnt = 0

        for j in range(len(users)):
            discnt, money = users[j]
            j_total = 0
            j_cnt = 0

            for k in range(len(tmp)):      
                if discnt <= (100 - comb[i][k]):
                    j_total += tmp[k]

                if j_total >= money:
                    j_cnt = 1
                    j_total = 0
                    break

            tmp_total += j_total
            tmp_cnt += j_cnt

        li.append([tmp_cnt, tmp_total])

    li = sorted(li, key = lambda x: (-x[0], -x[1]))
    answer = li[0]

    return answer



# 6
from collections import deque
import heapq

def solution(n, m, x, y, r, c, k):
    global answer
    answer = 'impossible'

    # total = set()
    
    # def in_range(x, y):
    #     return 0 <= x < n and 0 <= y < m

    # dx = [0, 1, 0, -1]
    # dy = [1, 0, -1, 0]
    # def bfs(x, y, cnt, tmp):

    #     pq = []
    #     heapq.heappush(pq, [tmp, x, y, cnt])
    #     while pq:
    #         tmp, x, y, cnt = heapq.heappop(pq)

    #         if cnt > k:
    #             continue

    #         if x == (r - 1) and (y == c - 1) and cnt == k:
    #             return tmp

    #         for d in range(4):
    #             nx = x + dx[d]
    #             ny = y + dy[d]

    #             if not in_range(nx, ny):
    #                 continue
    #             # r, d, l, u
    #             dirt = '#'
    #             if d == 0:
    #                 dirt = 'r'

    #             elif d == 1:
    #                 dirt = 'd'

    #             elif d == 2:
    #                 dirt = 'l'

    #             else:
    #                 dirt = 'u'
    #             tmp2 = tmp + dirt
                
    #             if cnt + 1 > k:
    #                 continue

    #             heapq.heappush(pq, [tmp2, nx, ny, cnt + 1])

    #     return 'impossible'

    # answer = bfs(x - 1, y - 1, 0, "")

    a = r - x
    b = c - y

    # a : + d, - : u
    # b : + r, - : l

    print(a, b)

    

    return answer