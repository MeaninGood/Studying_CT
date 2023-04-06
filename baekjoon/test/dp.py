n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 퇴사

ans = 0
# 가지치기가 없기 때문에 백트래킹은 아니고, dfs라고 볼 수 있는데
# 이 둘을 구분하는 건 별 의미 없다
# n = 15, 즉, 15일까지밖에 없다.
# 고르든 안 고르든, 하루마다 고를 수 있는 것은 2갈래씩
# 2^n인 2^15가지의 경우의 수 = 시간복잡도
# 2^20이 100만이니까 1초 안에 충분히 돌아감
def recur(cur , total):
    global ans
    
    if cur > n: # cur이 n보다 크다면 잘못한 것
        return
    
    if cur == n: # 딱 n이 됐을 때
        ans = max(ans, total)
        return
    
    recur(cur + arr[cur][0], total + arr[cur][1])
    recur(cur + 1, total)
    
    
recur(0, 0)


# 퇴사2 = n이 150만. 즉, 2^150
# 이정도면 가지치기로도 안 된다. O(n)에 풀라는 뜻
# 오늘 할 내용 중 가장 어렵다
# 위의 내용은, 하나를 들어갈 때마다 total에 누적한 후, 끝까지 다 돌았을 때
# 이제까지 누적한 것중 가장 큰 것을 ans라는 글로벌 변수에 담아줬었음

# 얘는 뭘 할 거면, 앞으로 고르는 것들 중에서 가장 많은 돈을 return하는 것
"""
예를 들어, recur(5)에 도착했다면, 5일을 한다면 5~7일 이틀간 15원을 벎
5일을 안 한다면, 6일 못하니까 넘어가고 7일 못하니까 넘어가서 0원을 돈다

5일에 딱 도착했을 때를 기준으로, 앞으로 벌 수 있는 최대 돈은 15원 = 15원을 리턴
"""
def recur(cur): # 정의 : cur번째 날짜부터 일을 잘 골라서 얻을 수 있는 최대 돈
    # 비정상적인 케이스니까 돈을 음수만큼 벌었다
    if cur > n: # cur이 n보다 크다면 돈을 못 번다. 못버는 정도가 아니라
        return -100000000   # 얘는 잘못한 거기 때문에 아주 작은 수를 리턴
    
    # 정상적인 케이스인데 돈을 앞으로 벌 수 없다
    if cur == n: # 제대로 왔고, 벌 수 있는 돈이 0원(마지막 날)
        return 0 # 이게 return 0
    
    # 일을 한다
    # cur + arr[cur][0]만큼 뒤로 가서 벌 수 있는 돈 + 지금 벌 수 있는 돈
    # 뒤에서부터 쌓아서 앞으로 돌아오는 것.
    recur(cur + arr[cur][0]) + arr[cur][1]
    # 그렇지 않다면 cur + 1의 돈을 벌게 됨. 이번 걸 포기했으니까
    recur(cur + 1)
    
    # 이 둘 중에서 큰 게 return 값 = 이번에 벌 수 있는 최대 돈
    return max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
    
    
    
    
recur(0)

# 위에 recur과 밑의 recur은 동치
# 위의 것을 아래로 바꾸는 연습을 해야 함. = 그때부터 엄청 많은 dp문제가 아주 쉽게 풀림
# dp문제를 백트래킹처럼 바꿔버리는 치트키

# 시간을 어떻게 줄이느냐?
# 위의 쟤가 왜 오래 걸리는지를 알면 시간을 어떻게 줄일지 보임
"""
지금이 3일이고, 이걸 고른다면 4일차부터 얻을 수 있는 돈 + 10원을 벌겠다
고르지 않는다면, 4일차부터 얻을 수 있는 돈만큼만 벌겠다 라고 가겠죠 3일차 기준
아까 짠 함수대로라면

4일차부터 받을 수 있는 돈이라는 값은 1~3일차를 어떻게 골랐는지와는 상관이 없다
즉, 4일차라고 고정이 되는 순간부터 리턴값이 정해져 있는 것과 마찬가지
이거를 계속 구하고 있으니 문제가 되는 것.
2^n이라고 아까 말했는데, 
1. 3일에서 4일로 넘어갈 때 한번 구해보고
2. 3일에서 4일로 넘어갈 때 3일을 안 고르고 넘어가는 것도 한번 구해보고
같은 값을 계속 구하기 때문에 문제.
즉, 4일에서 벌 수 있는 돈은 고정이 되어 있는데, 이걸 계속 구하는 것이 문제



"""


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [-1 for i in range(1500010)] # 150만개가 입력으로 들어오니까 -1로 초기화하는 걸 150만개 만들겠다


def recur(cur):

    if cur > n: # 여기서 아주 작은 값을 리턴하는 이유는, 0을 넣으면 얘도 정상적인 케이스로 인식하기 때문
        return -100000000 # 7일차부터 
    
    if cur == n:
        return 0

    # 설명 3. -1로 초기화해놨잖아, 만약에 dp[cur]이 -1이 아니면 바로 리턴만 하겠다
    # 처음 들어왔을 때는 -1일 테니까 구하러 들어가서 dp에 저장을 해줄거고
    # 나중에 같은 위치를 구하러 다시 또 들어온다면, 여기에 걸려서 바로 return을 해줄 것

    if dp[cur] != -1:
        return dp[cur]
    
    # return max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
    
    # 위에 코드 짠 후 dp 설명한 후 설명1. 여기서 바로 리턴하는 것이 아니라,
    # dp[cur]에다가 리턴하기 전에 저장을 해놔요
    # cur이 4였다면 dp[4], cur이 5였다면 dp[5]
    # 그니까 5일부터 얼만큼 벌 수 있냐 = 고정된 값이기 때문에 
    
    dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
    
    # 설명2. recur(5)에 다시 들어온다면, 이때 구해놨던 걸 리턴하면 됨. 다시 구할 것 없이 
    return dp[cur]
    
print(recur(0))


# 메모이제이션 별 거 없음
# 1. 처음에 dp테이블 만들고
# 2. 리턴하기 전에 원래 리턴하던 걸 dp테이블에 저장해서 리턴하는 걸로 바꾸고
# 3. dp값이 초기값이 아니면 리턴하겠다
## 이렇게 셋만 추가하면 메모이제이션 완료
# 이 세가지 단계는 계속 고정으로 갈 거고, 우리가 신경 쓸 것은 재귀함수를 바꾸는 과정임
# 이렇게 바꾸면 시간복잡도가 O(n)이 됨
"""
왜 O(n)이냐? 생각해 보면
dp테이블이 n개 있는데, 
dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
이 줄이 몇 번 실행되는지를 생각해볼게

    if cur > n:
        return -100000000
    
    if cur == n:
        return 0

    if dp[cur] != -1:
        return dp[cur]
    
위 세 줄은 어차피 O(1)
dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
이 줄 몇 번 실행됨?
이 줄 총 n번 실행 됨. 전체적으로 봤을 때 n번밖에 실행 안 됨
return dp[cur] : n번 실행될 거고

dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
이 줄 차제의 실행은 O(1)인데, 이게 총 n번 실행될 거기 때문에
전체적으로는 O(n)이 됨

그래서 결국 dp테이블을 한번씩 다 채워 보면, 어차피 끝나는 거니까 O(n)이다.
"""

###
# 1. 일단 백트래킹으로 짬
# 2. 하향식 설계로 바꿈
# 3. 리턴하기 전에, 리턴하는 게 아니라 dp[cur]에다 저장하고,
# 4. 이걸 구하기 직전에 dp[cur] != -1 조건을 추가하면 끝


# 1, 2, 3 더하기

# 1번 템플릿 써봤으면 어느정도 이해 갈 것
def recur(cur, total, tmp):
    if total > n:
        return 
    
    if total == n: # 합이 n이 된다면 return
        cnt += 1
        return
    
    for i in range(1, 4):
        recur(cur + 1, total + i, tmp + str(i))


## 사실 tmp 필요 없다
# cur도 필요가 없다
# 지우면 깔끔한 코드 완성, total만 가지고 옴
def recur(total):
    global cnt # 밑에 cnt 쓰고 global cnt 해주면 답은 나올 것.
                # global은 전역변수 선언, java static? 같은 개념
    
    if total > n:
        return 
    
    if total == n:
        cnt += 1
        return
    
    for i in range(1, 4):
        recur(total + i)
# 1번 템플릿으로 짠 다음에 필요없는 변수만 지운 것

T = int(input())

for tc in range(T):
    n = int(input())

    cnt = 0
    recur(0)
    print(cnt) # 이게 완탐임.


# return하는 식으로 바꾸기
def recur(total):
    ret = 0 # 3. 변수 하나 만들어 놓고
    if total > n: # 1. 경우의 수를 구하는 거니까 0을 리턴
        return 0 # 위에서 cnt 안 더한 거고,
    
    if total == n: # 2. 한가지 경우를 찾은 것
        return 1 # 여기서 위의 cnt += 1 해준 것과 동치
    
    for i in range(1, 4):
        ret += recur(total + i) # 4. 1을 채웠을 때의 경우의수, 2, 3을 채웠을 때의 경우의 수 다 더해서
        
    return ret # 5. 리턴해주면 됨
# cnt, global cnt 사라지고    

T = int(input())

for tc in range(T):
    n = int(input())

    print(recur(0))
    

## 이렇게만 해줘도 위의 문제들은 풀림


### 1, 2, 3 더하기 3
# n제한 100만임 -> 위에 식은 완탐이기 때문에 이거 안 풀릴 것
# 경우의수 문제기 때문에, 경우의 수는 0일 수는 있어도 음수일 수는 없다
# 그렇기 때문에 dp 테이블 -1로 채워줌

# n전체 제한보다 크기만 하면 됨
dp = [-1 for i in range(1000010)]
def recur(total):
    ret = 0
    if total > n:
        return 0
    
    if total == n:
        return 1
    
    # 3. 함수 돌기 전에 조건 걸어주면 끝
    if dp[total] != -1:
        return dp[total]
    
    for i in range(1, 4):
        ret += recur(total + i)
    
    # 1. 리턴하기 전에 dp[total]에 저장하고
    dp[total] = ret
    
    # 2. 저장한 dp[total]을 리턴하고
    return dp[total]

# 이러면 메모이제이션 적용한 것
T = int(input())

for tc in range(T):
    n = int(input())

    print(recur(0))

### 근데 이 식은 처음부터 설계가 잘못됐다
# dp테이블이 n에 종속적인데, n이 4일 때의 dp[0]과 n이 7일 때의 dp[0]이 다름
# 그때마다 dp를 만들어주면 시간이 너무 오래 걸리니까,
# total을 줄여나가는 방식으로 짜볼게요 
# 0에서 n까지 더해가면서 가는 거랑, n에서 0까지 줄여가면서 가는 게 똑같잖아요


dp = [-1 for i in range(1000010)]
def recur(total):
    ret = 0
    if total < n: # 2. 0보다 작으면으로 가고
        return 0
    
    if total == 0: # 3. 얘가 0에 도착했으면으로 가고
        return 1
    
    if dp[total] != -1:
        return dp[total]
    
    for i in range(1, 4):
        ret += recur(total - i) # 4. -로 가고
    
    dp[total] = ret
    
    return dp[total]

# 0부터 출발해서 n을 넘으면 0리턴, n이면 1리턴 이거랑
# n부터 출발해서 0에 도착했으면 1리턴, 마이너스로 가면 0리턴이랑 똑같음
# 이렇게 하면 이제 n에 종속적이지 않음

T = int(input())

for tc in range(T):
    n = int(input())

    print(recur(n)) # 1. n부터 출발해가지고
    
"""
이게 종속적이지 않은 이유는, 아까는 종료 조건에 n이 들어있었다
지금은 n이 안 들어있고, 출발지에 n이 들어있음
그렇기 때문에 n에 종속적이지 않은 것
이거는 문제가 좀 독특해서 그런데, 한 번만 들어오는 거였으면 어떻게 짜든 상관 없음

dp가 전역변수고, 종료 조건이 n이었기 때문에 똑같은 recur(0)이어도
n이 바뀌면 값이 달라졌던 것

하다보면 익숙해짐. 별로 안 어려워요
이제 시작한 거니까 너무 어렵다고 생각 안 해도 된다
이제 2문제 푼 것. 당연히 어려움. 아직까지는

계속 연습을 해볼게요

지금 사실 조금 어려운 게 맞는 게, 이 문제들을 정석보다 어렵게 풀고 있어요
정석은 반복문으로 푸는데, 이건 재귀를 돌아요
일부러 그런게
골드 문제 풀면서 느끼겠지만 똑같이 풀려요
골드 정도 수준의 문제까지를
그니까 실버부터 골드까지의 문제를 다 똑같이 풀기 위해서 지금 이 방법을 쓰는 것
난이도 평준화를 위해서

한가지 스킬만 익히면 되게 많은 문제를 풀 수 있게 만들어 놨음
"""



### 제곱수의 합
# 우선 처음에는 완탐으로 시작할 거예요
# n을 제곱수의 합으로 표현하는 문제

n = int(input())

"""
이제 뭐부터 해볼 수 있을까요?
우리가 7이라는 걸 나타낸다고 칠때
1+1+1+1+1+1+1
1   1   1   1   1   1   1
아니면 맨 앞자리에 4 넣어볼 수도 있는 거고
4   1   1   1
아니면 9는 못 넣어보죠?
1   1   1   4 이런 거 넣어볼 수도 있는 거고

이렇게 생각을 했을 때, 결국은 일반 백트래킹이랑 똑같아요
그니까 백트래킹으로 만들어볼 수 있어요
1   1   1   4를 봤으면 4    1   1   1은 볼 필요가 없긴 한데 이건 무시하고
백트래킹으로 만들어볼 수 있겠죠 아까 1, 2, 3더하기랑 똑같이 구성을 해볼 수 있음
맨 첫 1 위치에 1을 넣어볼 거냐, 4를 넣어볼 거냐, 9를 넣어볼 거냐
해보고 다음 거로 넘어가고
백트래킹으로 짜면 똑같다는 얘기예요

"""

ans  = 10000 # 6. ans 10000 같은 거 해놓고
def recur(cur, total, tmp):
    global ans
    
    if total == n: # 1. 만약에 total이 n이 된다면은 된거고
        # cur이 개수니까
        ans = min(ans, cur)
        return

    # 2. 그렇지 않다면
    for i in range(1, n + 1):
        if i * i > n - total: # 3. 만약 i * i가 n - total보다 크다면
            break # 4. 얘는 넣으면 안 되는 숫자
        # 만약 남은 수가 5인데, 9같은 거 넣으려 하면 안 되는 거다
        
        # 5. cur 하나 넘어가고, total에 i * i 넣어주고, tmp에도 넣어주고
        # 이러면 우리가 배웠던 백트래킹 1번 템플릿 완탐이에요
        # tmp는 필요 없으니까 지울게요
        recur(cur + 1, total + i * i, tmp + str(i * i))
        
        recur(cur + 1, total + i * i)
        
    
recur(0, 0)
print(ans)


# 이게 일단 기본 백트래킹으로 짠 거고, n제한이 크기 때문에 안 돌아요
# 그래서 리턴하는 식으로 바꿔볼게요

# 1. cur이라는 게, 몇 개 짜리냐 라는 이 값이죠
# 리턴할 거면 이 cur이라는 건 필요없어지고, total만 남아요
def recur(total):
    if total == n: # 만약 total이 n에 도착했으면
        return 0
        # 지금 현재 total일 때, 몇 개의 제곱수가 더 필요하냐라는 식으로 설계해볼게요
        # n에 도착했으면 더이상 필요가 없구요
        
    # 그렇지 않다면
    ret = 100000 # 리턴 값은 아주 큰 걸로 잡아 놓고
    for i in range(1, n + 1):
        if i * i  > n - total: # 이건 안 되는 거니까
            break # break 해주고
        
        # 얼만큼이 더 필요하냐, 이번에 1을 채울 때, 이번에 4를 채울때
        # 이번에 9를 채울 때 등등이니까
        ret = min(ret, recur(total + i * i) + 1)
        # total + i * i만큼의 횟수가 될 텐데,
        # 이자리에다가 지금 i * i를 넣은 거니까 + 1개를 해줌
        # 이 중에서 최소값이 리턴값이 됨
        # 지금 자리에 한개를 넣었다는 뜻의 + 1
        # 15를 만들 거면, 이번 자리에 4를 넣든 9를 넣든 할 건데
        # 6를 넣었다면 앞으로 6을 더 채울 것임
        # recur(total + i * i)에서 6을 만드는 최소 횟수가 리턴이 됨
        # 지금 자리에서 9를 넣었기 때문에 + 1을 해주는 것
        # 이번 자리에 넣은 제곱수 한개까지
        
    return ret # 이렇게 변하는 것. 계속하니까 좀 익숙해짐?

print(recur(0))
"""
+1 의 의미가 뭐냐면

15를 만들 건데
    이제부터 만들 수
1   recur(14)
4   recur(11)
9   recur(6)

10
1   recur(9)
4   recur(5)
9   recur(1) == 여기서 recur(1)을 그대로 리턴해주면 안 됨
왜냐면 1을 만드는 경우의 수는 한개거든
1을 리턴하면 10을 만드는 데도 한개가 된다라는 뜻
10을 만드려면은 1을 만드는 데 필요한 경우의 수 + 9 하나
== 2개가 됨
+1이라는 건 앞에 1, 4, 9 얘네가 하나씩 있으니까 얘네를 의미함
얘네들 중에 최소값 +1개라는 뜻

"""

# 여기서 dp 적용은 아까처럼 똑같이 하면 됨
dp = [-1 for i in range(100010)]
def recur(total):
    if total == n:
        return 0
    
    # 3. 재귀 돌기 전에
    if dp[total] != -1:
        return dp[total]

    ret = 100000
    for i in range(1, n + 1):
        if i * i  > n - total:
            break

        ret = min(ret, recur(total + i * i) + 1)

    # 1. 리턴하기 전에 dp에 저장
    dp[total] = ret
    # 2. 저장한 거 리턴
    return dp[total]

print(recur(0))



### 아까 퇴사문제 다시 보면
"""
첫번째 식에서는 arr[cur][1]번이라는 값을 계속 누적해서 마지막에 max값을 구함

2번에는
return max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))

골랐을 때 여기서 리턴을 받아 와가지고 
arr[cur][1]의 누적을 어디서 하냐면 리턴할 떄 해줌
그니까 쌓아서 들어간 게 아니라, 리턴한 거에 얹어서 들어가는 것
원래는 계속 안으로 들어가서, 계속 안쪽으로 보내서 다음 재귀로 보내고
또 거기서 다음 재귀로 보내서 마지막에 max 값을 리턴하는 식이었는데,

리턴 받은 거에 얹어 보고, 거기서 max를 바로 찾아가지고 보내는 것

첫번쨰 식은 끝났을 때 max값을 리턴하는 거면
이건 계속 리턴을 받아서 쌓아서 가기 때문에 끝났을 때 0을 리턴함
"""


### 1, 2, 3더하기 바텀업 코드
"""
1을 만드는 방법의 수
1       1가지
2       2가지 (1+1, 2)
3       4가지(1+1+1, 1+2, 2+1, 3)
4       7
결론만 말하면 7개인데, 
맨 앞에 1을 채웠으면
1 + dp[3]이 됨 // 3을 만드는 경우의 수

맨 앞에 2를 채웠다면
2 + dp[2]가 됨 // 2를 만드는 경우의 수

맨 앞에 3을 채웠다면
3 + dp[1]

그렇기 때문에
dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 3]
이라는 깔끔한 식이 나옴

== 점화식을 세운 것
"""



dp = [0 for _ in range(1000010)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000010):
    dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % 1000000009

T = int(input())
for tc in range(T):
    n = int(input())
    
    print(dp[n])
    
"""
이렇게 풀 수 있음.
아까 재귀로 푸는 게 어려웠다는 얘기

골드 문제들은 아까처럼 재귀로 풀면 날먹이 됨
이걸로 골드 3정도의 난이도까지 날먹할 수 있음
나중에 다시 공부 해보시고 쉬운 바텀업부터 해보셔도 됨
좀 어려운 문제들이 바텀업이 어렵다
어려운 문제 쉽게 푸는 거였음
근데 사실 아까처럼 재귀식으로 풀다 보면 점화식이 도출이 됨
그래서 사실은 이렇게 짠 다음에, 이게 시간초과가 나면
바텀업으로 짜면 됨
"""

## 1, 2, 3더하기 바텀업 코드

dp = [-1 for i in range(1000010)]
def recur(total):
    ret = 0
    if total < n: 
        return 0
    
    if total == 0:
        return 1
    
    if dp[total] != -1:
        return dp[total]
    
    for i in range(1, 4):
        ret += recur(total - i) # 2. dp[total]에 total - i 이게 뭐냐?
        # 3. dp[total - 1] + dp[total - 2] + dp[total - 3]이라는 뜻
        # 4. 이게 dp에 들어가는 거니까, 점화식이 나온 것
    
    # 1. dp[total]에 어떤 값이 들어가는지 보면 쉬운데
    dp[total] = ret
    
    return dp[total]

## 결국 같은 점화식을 재귀로 짜냐, 반복문으로 짜냐임



## 퇴사문제
def recur(cur):
  
    if cur > n:
        return -100000000
    
    if cur == n:
        return 0

    if dp[cur] != -1:
        return dp[cur]

    # 1. dp[cur]에 뭐가 들어가는지 보면 
    # recur뭐시기가 사실 dp죠
    # dp[cur] = dp[cur + arr[cur][0]] + arr[cur][1], dp[cur + 1]
    # 하면서 큰 게 들어가면 됨
    # dp[cur] = max(dp[cur + arr[cur][0]] + arr[cur][1], dp[cur + 1])
    # 이렇게 할 거면 뒤에서부터 채워서, dp[0]에 있는 게 답이다 하면 됨
    dp[cur] = max(recur(cur + arr[cur][0]) + arr[cur][1], recur(cur + 1))
    
    return dp[cur]
    
print(recur(0))



### 3. 제곱수의 합
"""
16 만들겠다
1 + ?
4 + ?
9 + ?
16 + ?
인데

1 + dp[15]
4 + dp[12]
9 + dp[7]
16 + dp[0]
중에 작은 게 정답
"""

n = int(input())
dp = [100000 for i in range(n + 1)]

dp[0] = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 1. i기준으로 i가 16이었다 치면
        # 1, 4, 9, 16 얘네들을 봐야되니까 
        if j * j > i:
            break
        
        # j가 이제 1, 2, 3, 4가 되면서 얘네들만 봐줄 거임
        dp[i] = min(dp[i], dp[i - j * j] + 1)
        
print(dp[n])