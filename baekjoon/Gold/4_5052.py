import sys
input = lambda : sys.stdin.readline().strip()

T = int(input())
for tc in range(T):
    n = int(input())
    arr = [input() for _ in range(n)]

    arr.sort()
    
    d = {}
    check = False
    for num in arr:
        for i in range(len(num)):
            tmp = num[:i + 1]
            if d.get(tmp):
                check = True
                break

        d[num] = d.get(num, 0) + 1 

    if check:
        print('NO')
    
    else:
        print('YES')