# 11726번_2 x N 타일링

## 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성


'''
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
## 첫째 줄에 2 x n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력

(입력)
2

(출력) 
2

'''

'''
1칸 - 1개 // 홀수 칸일 때 1개
|

2칸 - 2개 // 짝수 칸일 때 
| |
=

3칸 - 3개
| | |
= |
| =

4칸 - 5개
| | | |
= | |
= =
| = |
| | =

5칸 - 8개
| | | | |
= | | |
| = | |
| | = |
| | | =
= = |
= | =
| = =

 1  2  3  4  5
[1, 2, 3, 5, 8]

하나 놓거나
두개 놓거나 // 두개 : 두칸

2 x 1 타일은 무조건 눕혀서 2칸임

'''

dp = [-1 for i in range(1010)]
def recur(cur):
    ret = 1
    if cur < 0:
        return -1000000
    
    if cur == 0:
        return ret

    if dp[cur] != -1:
        return dp[cur]

    ret = max(ret, recur(cur - 1) + recur(cur - 2))
    dp[cur] = ret
    return dp[cur]

n = int(input())
print(recur(n) % 10007)



dp = [-1 for i in range(1010)]
def recur(cur):
    ret = 1
    if cur > n:
        return -1000000
    
    if cur == n:
        return ret

    if dp[cur] != -1:
        return dp[cur]

    ret = max(ret, recur(cur + 1) + recur(cur + 2))
    dp[cur] = ret
    return dp[cur]

n = int(input())
print(recur(0) % 10007)