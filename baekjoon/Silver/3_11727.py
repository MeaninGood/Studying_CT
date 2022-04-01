# 11727번_2 x N 타일링 2

## 2×n 직사각형을 1×2, 2×1과 2×2 타일로 채우는 방법의 수를 구하는 프로그램을 작성


'''
# 첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)
## 첫째 줄에 2 x n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력

(입력)
2

(출력) 
2

'''

'''
1칸 - 1개
|

2칸 - 3개
| |
=
ㅁ

3칸 - 5개
| | |
= |
| =
ㅁ |
| ㅁ

4칸 - 11개
| | | |

= | |
= =
| = |
| | =

ㅁ | |
ㅁ ㅁ
| ㅁ |
| | ㅁ

ㅁ =
= ㅁ


 1  2  3  4   5  6
[1, 3, 5, 11, 21, 43]



'''
dp = [-1 for i in range(1010)]
def recur(cur):
    ret = 1
    
    if cur < 0:
        return 0
    
    if cur == 0:
        return ret
    
    if dp[cur] != -1:
        return dp[cur]
    
    ret = recur(cur - 1) + (recur(cur - 2) * 2)
    dp[cur] = ret
    return dp[cur]
    

n = int(input())
print(recur(n))






dp = [-1 for i in range(1010)]
def recur(cur):
    ret = 1
    
    if cur > n:
        return 0
    
    if cur == n:
        return ret
    
    if dp[cur] != -1:
        return dp[cur]
    
    ret = recur(cur + 1) + (recur(cur + 2) * 2)
    dp[cur] = ret
    return dp[cur]
    

n = int(input())
print(recur(0))