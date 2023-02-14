import sys
input = lambda : sys.stdin.readline().strip()

def recur(cur, asum, bsum, csum, dsum, total, tmp):
    global answer, nums
    if cur == n + 1:
        if asum >= a and bsum >= b and csum >= c and dsum >= d:
            if answer > total and tmp != []:
                answer = total
                nums = [tmp]
            elif answer == total and tmp != []:
                nums.append(tmp)
        
        return
    
    # 고르는 경우
    recur(cur + 1, asum + arr[cur][0], bsum + arr[cur][1], csum + arr[cur][2],
          dsum + arr[cur][3], total + arr[cur][4], tmp + [cur])
    # 안 고르는 경우
    recur(cur + 1, asum, bsum, csum, dsum, total, tmp)

n = int(input())
a, b, c, d = list(map(int, input().split()))
arr = [['#']] + [list(map(int, input().split())) for _ in range(n)]

nums = []
answer = 0
for i in range(1, n + 1):
    answer += arr[i][4]

check = recur(1, 0, 0, 0, 0, 0, [])

if len(nums) > 0:
    print(answer)
    nums.sort()
    print(*nums[0])

else:
    print(-1)