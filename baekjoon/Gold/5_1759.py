def recur(cur):
    ret = ''
    
    recur(ret + arr[cur + 1])
    recur()


n, m = map(int, input().split())
arr = list(map(str, input().split()))

ae = ['a', 'e', 'i', 'o', 'u']

ans = []