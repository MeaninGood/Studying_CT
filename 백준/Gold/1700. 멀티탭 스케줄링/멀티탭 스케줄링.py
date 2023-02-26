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
