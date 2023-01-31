import sys
input = lambda: sys.stdin.readline().strip()


li = [1, 5, 10, 50]
def recur(cur, cnt, tmp=[]):
    global arr2
    
    # 4개 다 뽑았을 때
    if cur == 4:
        if cnt == n:
            total = 0
            for i in range(4):
                total += li[i] * tmp[i]
            arr2.add(total)
        return
    
    for i in range(n - cnt + 1):
        recur(cur + 1, cnt + i, tmp+[i])

n = int(input())
arr2 = set()
recur(0, 0)
print(len(arr2))
