n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# arr.sort(key = lambda x: x[0])
dp = [-1 for _ in range(110)]

print(arr)

def recur(cur):
    ret = 1
    
    for i in range(n):
        if cur <= arr[i][0]:
            ret = max(ret, recur(arr[i][1]) + 1)
            
    return ret

print(recur(0) - 1)
