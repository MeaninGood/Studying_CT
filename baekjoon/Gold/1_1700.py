import sys
input = lambda : sys.stdin.readline().strip()


n, m = map(int, input().split())
arr = list(map(int, input().split()))

d = {}
for i in range(m):
    d[arr[i]] = d.get(arr[i], [])
    d[arr[i]].append(i)

answer = 0
idx = [0 for _ in range(n)]
for i in range(m):
    # 이미 끼워져 있는 콘센트라면 건너띄기
    if arr[i] in idx:
        d[arr[i]].pop(0)
        continue

    check = False
    # 빈 콘센트가 있다면 끼우고 건너띄기
    for j in range(n):
        if idx[j] == 0:
            idx[j] = arr[i]
            check = True
            d[arr[i]].pop(0)
            break

    if check:
        continue

    # 빈 콘센트가 없다면, 뺄 콘센트 찾기
    # 1. 더 이상 끼우지 않는 콘센트가 있으면 빼고 새 콘센트를 끼움
    tmp = 0
    check2 = False
    for k in range(n):
        if d[idx[k]] == []:
            idx[k] = arr[i]
            check2 = True
            break
        
    
    if not check2:
        del_key, del_val = -1, -1
        # 2. 제일 나중에 끼울 콘센트를 찾아서 뽑고 새 콘센트 끼움
        for key in idx:
            if len(d[key]) > 0 and d[key][0] > del_val:
                del_key = key
                del_val = d[key][0]

        for k in range(n):
            if idx[k] == del_key:
                idx[k] = arr[i]
                break

    d[arr[i]].pop(0)
    
    answer += 1

print(answer)


"""
2 7
2 3 2 3 1 2 7
1 2 3 4 5 6 7

2 3
2 : 6
3 : 
1 : 5
7 : 7


3 14
1 4 3 2 5 4 3 2 5 3 4 2 3 4

1   4   3
[2] 4   3  # 3
[5] 4   3  # 4
 5 [2]  3  # 7
[4] 2   3  # 10

3 13
2 3 4 2 3 4 1 5 5 5 2 3 2

2 11
1 2 3 4 5 1 1 1 2 2 2



4 20
1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5

2 10
1 1 2 1 1 2 1 1 2 1

3 100
56 71 70 25 52 77 76 8 68 71 51 65 13 23 7 16 19 54 95 18 86 74 29 76 61 93 44 96 32 72 64 19 50 49 22 14 7 64 24 83 6 3 2 76 99 7 76 100 60 60 6 50 90 49 27 51 37 61 16 84 89 51 73 28 90 77 73 39 78 96 78 13 92 54 70 69 62 78 7 75 30 67 97 98 19 86 90 90 2 39 41 58 57 84 19 8 52 39 26 7
"""