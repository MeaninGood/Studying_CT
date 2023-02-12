import sys
input = lambda : sys.stdin.readline().strip()

T = int(input())
for tc in range(T):
    AB = input()
    n = int(input())
    arr = eval(input())

    rev = False
    ldcnt = 0
    rdcnt = 0
    for rd in AB:
        if rd == 'R':
            rev = not rev
        else:
            if ldcnt + rdcnt >= n or n == 0:
                print('error')
                break

            if not rev:
                ldcnt += 1
            
            elif rev:
                rdcnt += 1
        
    else:
        tmp = []
        for i in range(ldcnt, n - rdcnt):
            tmp.append(arr[i])

        tmp = tmp[::-1] if rev else tmp
        print('[' + ','.join(map(str, tmp)) + ']')