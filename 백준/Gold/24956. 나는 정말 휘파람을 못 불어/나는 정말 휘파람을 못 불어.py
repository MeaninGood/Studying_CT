import sys

input = lambda: sys.stdin.readline().strip()

def check(w, e):
    if w >= 1 and e >= 2:
        return True
    
    return False

n = int(input())
arr = list(input())

warr = [0 for _ in range(n)]
warr[0] += arr[0] == 'W'

for i in range(1, n):
    warr[i] = warr[i - 1] + (arr[i] == 'W')
    

earr = [0 for _ in range(n)]
earr[-1] += arr[-1] == 'E'
for i in range(n - 1)[::-1]:
    earr[i] = earr[i + 1] + (arr[i] == 'E')
    

ans = 0
for i in range(n):
    if arr[i] != 'H' or not check(warr[i], earr[i]):
        continue
    # h를 기준으로 W와 조합(지금까지 나온 w개수) * e를 2개 이상 고른 개수
    tmp = (2 ** earr[i]) - 1 - earr[i]
    ans += (warr[i] * tmp) % (10 ** 9 + 7)
    
print(ans % (10 ** 9 + 7))
    
