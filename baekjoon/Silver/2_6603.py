v = [0 for i in range(6)]
def recur(cur, start):
    if cur == 6:
        print(*v)
        return

    for i in range(start, n):
        v[cur] = arr[i]
        recur(cur + 1, i + 1)

while 1:
    arr = list(map(int, input().split()))
    if arr == [0]:
        break
    
    n = arr.pop(0)
    arr.sort()

    recur(0, 0)
    print()