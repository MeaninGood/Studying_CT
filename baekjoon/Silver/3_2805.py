# 4 7
# 20 15 10 17

# 높이 0에서 절단 -> 62
# 1 -> 58
# 2-> 54 ...
# 15 -> 7
# 16 -> 5

n, m = map(int, input().split())

arr = list(map(int, input().split()))

def check(x):
    total  = 0
    for i in range(n):
        total += max(0, arr[i] - x) # 음수일 때는 0 나오라고 max(0)
         
    # 같은 코드    
    # if arr[i] > x :
    #     total += arr[i]- x
    
    return total >= m # T F 리턴

s = 0
e = 100000000000000 # 0 세 개 더 붙어도 10번 차이라서 충분히 많이 붙여도 됨
ans = 0
while s <= e:
    mid = (s + e) // 2
    
    if check(mid):
        ans = mid
        s = mid + 1
        
    else :
        e = mid - 1
        
print(ans)
