'''
최소값, 최대값 -> 최적화 문제 optimization
OX(되냐 안 되냐) -> 결정 문제 decision
정답 -> 답 찾는 문제

parametric search -> 최적화 문제를 결정문제로 바꿔서 푼다

'''


'''
# 2666
1. 최적화
2. n제한이 20이야 -> 좀 작네!
3. 그럼 완탐이 되지 않을까?


왼쪽 문의 왼쪽에 있는 애들 / 오른쪽 문의 오른쪽에 있는 애들은
그쪽으로 땡겨주면 되는데
사이에 있는 애들이 애매함

'''
# 2666
## 메모이제이션 안 한 재귀함수 - 완전탐색
n = int(input())
x, y = map(int, input().split())
m = int(input())
arr = [int(input()) for i in range(m)]
# arr에 든 게 cur // 왼쪽 x, 오른쪽 y

def recur(cur, a, b):
    if cur == m: # cur이 m까지 왔으면 (몇 번째를 보고 있냐!)
        return 0
    
    if arr[cur] <= a: # a보다 왼쪽 걸 연다면
        # cur + 1을 열어야 하고, arr[cur]과 b가 열려 있는 상태
        # a - arr[cur]
        # 3번이 열려 있고 1번을 열어야 한다면 2칸 이동해야 된다
        recur(cur + 1, arr[cur], b) + a - arr[cur]
        
    elif arr[cur] >=b:
        # b보다 arr[cur]이 뒤에 있으니까 arr[cur] - b
        recur(cur + 1, a, a, arr[cur]) + arr[cur] - b
        
    else:
        return min(recur(cur + 1, arr[cur], b) + arr[cur] - a, recur(cur + 1, a, arr[cur]) + b - arr[cur])
    
print(recur(0, min(x, y), max(x, y)))


## 메모이제이션
## 2 3 7
## 일 때 2번을 옮기려고 하면 return 값은 항상 일정함
## cur, a, b 범위 다 20이니까 대충 30으로 잡기


n = int(input())
x, y = map(int, input().split())
m = int(input())
arr = [int(input()) for i in range(m)]
# arr에 든 게 cur // 왼쪽 x, 오른쪽 y
dp = [[[-1 for i in range(30)] for j in range(30)] for k in range(30)]
# dp[cur][a][b]가 다 똑같으면 리턴
# 3개 있으니까 3차원으로 만들기


def recur(cur, a, b):
    if cur == m:
        return 0
    
    if dp[cur][a][b] != -1:
        return dp[cur][a][b]
        
    if arr[cur] <= a:
        ret = recur(cur + 1, arr[cur], b) + a - arr[cur]
        
    elif arr[cur] >=b:
        ret = recur(cur + 1, a, a, arr[cur]) + arr[cur] - b
        
    else:
        ret = min(recur(cur + 1, arr[cur], b) + arr[cur] - a, recur(cur + 1, a, arr[cur]) + b - arr[cur])
        
    dp[cur][a][b] = ret
    
print(recur(0, min(x, y), max(x, y)))



''''
1. 재귀로 리턴하도록 풀이
2. 재귀함수 인자가 동일한 상황에 동일한 리턴을 하는지 -> 이게 되면 메모이제이션 적용 가능
3. 안 되면 메모이제이션 불가능
4. 재귀함수 인자 개수만큼의 차원으로 dp테이블 생성!
5. 기저 바로 아래쪽에 if -1이 아니면 return
6. 함수 마지막 부분에서 리턴 직전 dp에 저장

'''



# 돌다리건너기


s = input()
arr = [input() for i in range(2)]
# arr[0], arr[1]

# r -> g -> s가 cur , 시작 위치 알아야 함
# r, g, s을 밟았을 때 내가 지금 어디 있나? 현재 위치 알아야 함
# r, g, s 중 뭘 밟아야 하는지 알아야 함

# 방법의 수 리턴
def recur(cur, x, y):
    ret = 0
    
    if cur == len(s):
        return 1 # 방법 한가지 찾았음!
    
    # 현재 위치가 밑의 g라면 다음 밟을 거는
    # 위의 g + 1부터 n까지임
    for i in range(y, len(arr[0])):
        # 일단 아랫줄의 g를 밟았다고 치면
        # if s[cur] == arr[x - 1][i]:
        #     ret += recur(cur + 1, x - 1, i + 1)
            
        if s[cur] == arr[x ^ 1][i]:
            ret += recur(cur + 1, x ^ 1, i + 1)
            
    return ret
    
# 윗줄에서 시작했을 때 + 아랫줄에서 시작했을 때 더하면 답
print(recur(0, 0, 0) + recur(0, 1, 0))    
    
    
    
# 메모이제이션

s = input()
arr = [input() for i in range(2)]
dp = [[[-1 for i in range(110)] for j in range(3)] for k in range(30)]

def recur(cur, x, y):
    ret = 0
    
    if cur == len(s):
        return 1

    if dp[cur][x][y] != -1:
        return dp[cur][x][y]
    
    for i in range(y, len(arr[0])):

        if s[cur] == arr[x ^ 1][i]:
            ret += recur(cur + 1, x ^ 1, i + 1)
            
    dp[cur][x][y] = ret
    
    return ret

print(recur(0, 0, 0) + recur(0, 1, 0))






'''
123 더하기
퇴사
제곱수의합
가장 긴 증가하는 큰 증가하는 부분수열

'''