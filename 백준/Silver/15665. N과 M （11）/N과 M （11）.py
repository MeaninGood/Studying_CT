import sys
input = lambda : sys.stdin.readline().strip()

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def recur(cur, tmp):
    if cur == m:
        print(tmp)
        return

    num = -1
    for i in range(n):
        if num == arr[i]:
            continue
        
        num = arr[i]
        recur(cur + 1, tmp + str(arr[i]) + ' ')

recur(0, '')