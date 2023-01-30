import sys
input = lambda : sys.stdin.readline().strip()


alpha = ['a', 'e', 'i', 'o', 'u']
def check(x):
    cnt1 = 0
    cnt2 = 0
    for ae in x:
        if ae in alpha:
            cnt1 += 1
        else:
            cnt2 += 1
        
    return cnt1 >= 1 and cnt2 >= 2
    
def recur(cur, tmp):
    if cur == n:
        if check(tmp):
            print(tmp)
        return

    for i in range(m):
        if len(tmp) > 0 and ord(tmp[-1]) >= ord(arr[i]):
            continue
        
        recur(cur + 1, tmp + arr[i])
            
        


n, m = map(int, input().split())
arr = input().split()

arr.sort()
recur(0, '')