n, m = map(int, input().split())
li = list(map(int, input().split()))
li.sort()
a = len(li)
arr = [0 for i in range(m)]


def recur(cur, start):
    if cur == m:
        print(*arr)
        return
    
    for i in range(start, a):

        arr[cur] = li[i]
        recur (cur + 1, i + 1)

recur(0, 0)