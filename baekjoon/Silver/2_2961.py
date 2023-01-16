import sys
input = lambda : sys.stdin.readline().strip()


def recur(cur, multi, plus, cnt):
    ret = 1000000000    

    if cur == n:

        if cnt > 0:
            ret = abs(multi - plus)
            
        return ret
    
    ret = min(recur(cur + 1, multi * arr[cur][0], plus + arr[cur][1], cnt + 1), recur(cur + 1, multi, plus, cnt))
    
    return ret
    

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

print(recur(0, 1, 0, 0))




'''
# if cnt > 0 and multi * arr[cur][0] >= plus + arr[cur][1]:
#     ret = min(multi * arr[cur][0] - plus + arr[cur][1], multi - plus)
    
# if cnt > 0 and plus + arr[cur][1] > multi * arr[cur][0]:
#     ret = min(plus + arr[cur][1] - multi * arr[cur][0], plus - multi)
# if cnt > 0 and multi >= plus:
#     ret = multi - plus

# if cnt > 0 and plus> multi:
#     ret = plus - multi

'''