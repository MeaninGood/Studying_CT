## 배열을 이동한 코드 스킬

### 1. 조건문 - > 배열화 코드 정의

```python
if x = 1:
    print('aaa')
elif x = 2:
    print('bbb')
elif x = 3:
    print('ccc')
...
```

+ 해당 코드를 배열화 한다면 아래와 같다.

```python
arr = [0,'aaa','bbb','ccc',...]

print(arr[x])
```



예시문제 1) <img src="https://d2gd6pc034wcta.cloudfront.net/tier/3.svg" width="20" height="20">[[1284] 집주소](https://www.acmicpc.net/problem/1284)

```python
while True: # 해당 코드는 0 이 나올 때까지 반복한다.
    N = input() # 주소판으로 사용할 숫자 input
    
    if N == '0': # 0 이 나올 경우, 반복 종료
        break
    
	answer = len(N) + 1 # 간격은 양 옆 공백(2cm) 문자사이의 간격사이 (len(N)-1cm)
    
    if N[i] == '0': # 0 일 때, 4cm
        answer += 4
    if N[i] == '1': # 1 일 때, 2cm
        answer += 2
    else: # 그 외의 경우, 3cm
        answer += 3
    
    print(answer)
```

+ 해당코드를 배열화를 활용한다면 얻을 수 있는 장점
  1. 코드가 더 짧아진다.
  2. 코드가 직관적이게 된다.

```python
# 배열화 하여, 해당 코드의 cm 를 index 접근한다.
arr = [4,2,3,3,3,3,3,3,3,3]

while True: # 해당 코드는 0 이 나올 때까지 반복한다.
    N = input() # 주소판으로 사용할 숫자 input
    
    if N == '0': # 0 이 나올 경우, 반복 종료
        break
    
    answer = len(N) + 1 # 간격은 양 옆 공백(2cm) 문자사이의 간격사이 (len(N)-1cm)
    
    for i in N: # 문자열을 한개씩 보면서, arr에 저장된 배열의 값을 answer 에 더해준다.
        answer += arr[int(i)]

    print(answer)
```

+ 이러한 알고리즘 풀이 방식 -> 데이터와 로직을 분리한다고 한다.
+ Why? 코드가 간결해지고, 디버깅도 꽤 편해지기 때문에!



### 2. 조건문 -> 배열화 예시 문제 리스트

| 문제번호 | 풀이 |
| ------------------------------------------------------------ | ---- |
| 1. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/1.svg" width="20" height="20"> [[3003] 킹, 퀸, 룩, 비숍, 나이트, 폰](https://www.acmicpc.net/problem/3003)                                                      | [이동](#3003-킹-퀸-룩-비숍-나이트-폰) |
| 2. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/3.svg" width="20" height="20">[[1284] 집주소](https://www.acmicpc.net/problem/1284) | [이동](#1284-집주소) |
| 3. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/2.svg" width="20" height="20">[[17362] 수학은 체육과목 입니다 2](https://www.acmicpc.net/problem/17362) | [이동](#17362-수학은-체육과목-입니다) |
| 4. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/3.svg" width="20" height="20">[[1864] 문어 숫자](https://www.acmicpc.net/problem/1864) | [이동](#1864-문어-숫자) |
| 5. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/3.svg" width="20" height="20"> [[2490] 윷놀이](https://www.acmicpc.net/problem/2490) | [이동](#2490-윷놀이) |
| 6. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[1264] 모음의 개수](https://www.acmicpc.net/problem/1264) | [이동](#1264-모음의-개수) |
| 7. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[2037] 문자메시지](https://www.acmicpc.net/problem/2037) | [이동](#2037-문자메시지) |
| 8. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[2520] 팬케이크 사랑](https://www.acmicpc.net/problem/2520) | [이동](#2520-펜케이크-사랑) |
| 9. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[2789] 유학 금지](https://www.acmicpc.net/problem/2789) | [이동](#2789-유학-금지) |
| 10. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[2948] 2009년](https://www.acmicpc.net/problem/2948) | [이동](#2948-2009년) |
| 11. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[2966] 찍기](https://www.acmicpc.net/problem/2966) | [이동](#2966-찍기) |
| 12. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[3154] 알람시계](https://www.acmicpc.net/problem/3154) | [이동](#3154-알람시계]) |
| 13. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[4435] 중간계 전쟁](https://www.acmicpc.net/problem/4435) | [이동](#4435-중간계-전쟁) |
| 14. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[4606] The Seven Percent Solution](https://www.acmicpc.net/problem/4606) | [이동](#4606The-Seven-Percent-Solution) |
| 15. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[5585] 거스름돈](https://www.acmicpc.net/problem/5585) | [이동](#5585-거스름돈) |
| 16. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[5622] 다이얼](https://www.acmicpc.net/problem/5622) | [이동](#5622-다이얼) |
| 17. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/5.svg" width="20" height="20"> [[6368] P,MTHBGWB](https://www.acmicpc.net/problem/6368) | [이동](#6368-PMTHBGWB) |
| 18. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[6750] Rotating letters](https://www.acmicpc.net/problem/6750) | [이동](#6750-Rotating-letters) |
| 19. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/5.svg" width="20" height="20"> [[6765] Icon Scaling](https://www.acmicpc.net/problem/6765) | [이동](#6765-Icon-Scaling) |
| 20. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/3.svg" width="20" height="20"> [[11800] Tawla](https://www.acmicpc.net/problem/11800) | [이동](#11800-Tawla) |
| 21. <img src="https://d2gd6pc034wcta.cloudfront.net/tier/4.svg" width="20" height="20"> [[10551] STROJOPIS](https://www.acmicpc.net/problem/10551) | [이동](#10551-STROJOPIS) |



### 3. 문제 풀이

##### [3003] 킹, 퀸, 룩, 비숍, 나이트, 폰

```python
# 화이트 피스를 숫자로 받는다.
white_piece = list(map(int, input().split()))
# 옳게 된 피스를 받아온다.
correct_piece = [1, 1, 2, 2, 2, 8]
# 피스의 총 길이
n = len(white_piece)
# 출력할 결과값을 받아줄 result
result = []

for i in range(n):
    # 피스의 길이를 돌면서 옳게된 피스 - 입력받은 피스 를 result 에 append 한다.
    result.append(correct_piece[i]-white_piece[i])

# unpacking 을 통해 배열을 문자열로 출력한다.
print(*result)
```



##### [1284] 집주소

```python
# 배열화 하여, 해당 코드의 cm 를 index 접근한다.
arr = [4,2,3,3,3,3,3,3,3,3]

while True: # 해당 코드는 0 이 나올 때까지 반복한다.
    N = input() # 주소판으로 사용할 숫자 input
    
    if N == '0': # 0 이 나올 경우, 반복 종료
        break
    
    answer = len(N) + 1 # 간격은 양 옆 공백(2cm) 문자사이의 간격사이 (len(N)-1cm)
    
    for i in N: # 문자열을 한개씩 보면서, arr에 저장된 배열의 값을 answer 에 더해준다.
        answer += arr[int(i)]

    print(answer)
```



##### [17362] 수학은 체육과목 입니다

```python
# 임의의 자연수 N
N = int(input())

# 손가락 배열 8 을 기준으로 순회하게 된다.
# 1 : 엄지손가락 2: 검지손가락 3: 중지손가락 4: 약지손가락 5: 새끼손가락
arr = [2, 1, 2, 3, 4, 5, 4, 3]

# N에서 남은 나머지를 기준으로, index 접근하면 손가락을 구할 수 있다.
print(arr[N % 8])

```



##### [1864] 문어 숫자

```python
# 딕셔너리를 통해 key(문자) : value(숫자) 형태로 나열하자.
dict_octopus = {
    '-' : 0,
    # \ 는 제대로 입력받기 위해서는 이스케이프 문자를 활용하여야 한다.for
    '\\' : 1,
    '(' : 2,
    '@' : 3,
    '?' : 4,
    '>' : 5,
    '&' : 6,
    '%' : 7,
    '/' : -1,
}

# 해당 구문은 #이 나오기전까지 출력된다. 따라서, while True 로 시작하자
while True:
    # 임의의 특수 문자열 S를 입력받는다.
    S = input()
    # 해당 S가 #이면 반복문을 종료한다.
    if S == '#':
        break
    # 이를 8진법의 숫자로 바꾸어야 한다. 따라서 문자열의 길이가 필요하다.
    n = len(S)

    # 출력할 수를 담을 int 형인 answer 를 선언한다.
    answer = 0

    # 반복문을 통해, 문자열에 접근하여 바꾼 수를 answer 에 더해준다.
    for i in range(n):
        # 형태는 숫자 * 8 ^ (n-1 - i) 형태가 된다.
        answer += dict_octopus[S[i]] * 8 ** (n - 1 - i)
        
    print(answer)

```



##### [2490] 윷놀이

```python
# A : 도 [ 1(배) : 1개, 0(등): 3개 ]
# B : 개 [ 1(배) : 2개, 0(등): 2개 ]
# C : 걸 [ 1(배) : 3개, 0(등): 1개 ]
# D : 윷 [ 1(배) : 4개, 0(등): 0개 ]
# E : 모 [ 1(배) : 0개, 0(등): 4개 ]

# 0 의 갯수에 따른 배열로 접근하자
arr = ['E','A','B','C','D']

# 윷은 총 3번 던진다 3번 출력하자.
N = 3
for _ in range(N):
    # 윷짝들의 상태를 list 로 받자.
    yut = list(map(int,input().split()))
    # 0 의 갯수를 센 뒤, arr 의 index 로 접근하자.
    print(arr[yut.count(0)])

```



##### [1264] 모음의 개수

```python
# 모음을 담고 있는 배열
gather = ['a','e','i','o','u','A','E','I','O','U']

# 입력을 계속 받으며 #이 나오면 출력을 종료한다.
while True:
    S = input()
    if S == '#':
        break

    # 모음의 갯수를 출력할 숫자형 answer 를 할당한다.
    answer = 0

    # 문자열을 돌면서, 모음의 갯수를 count 한다.
    for s in S:
        # 문자열 하나가 모음인지 확인하기 위한 조건문
        if s in gather:
            answer += 1

    # 모음의 개수를 출력한다.
    print(answer)

```



##### [2037]문자메시지

```python
# 알파벳 문자의 위치
arr = [2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,8,8,8,9,9,9,9]
# 알파벳 버튼을 연속으로 누르는 횟수
push = [1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,4,1,2,3,1,2,3,4]

# p : 버튼을 한번 누르는 데 걸리는 시간
# q : 같은 버튼을 연속으로 누를 때 걸리는 시간(C 를 입력하려면, q가 2번)
p, w = map(int,input().split())

# S : 문자 메시지
S = input()

# 걸리는 시간을 담을 int 형 answer
answer = 0

# S 를 반복문을 돌면서 걸리는 시간을 더해준다.
for i in range(len(S)):
    # 공백일 경우, p 의 시간만 추가한다.
    if S[i] == ' ':
        answer += p
    # 이전에 누른 것과 문자열이 같은 휴대폰 자판에 위치할 경우,
    # ord(' ') 은 32 로써, 이를 대입해 배열에 넣을 경우 범위를 초과한다. 따라서 조건문으로 거르자.
    elif i != 0 and S[i-1] !=' ' and arr[ord(S[i])-ord('A')] == arr[ord(S[i-1])-ord('A')]:
        # w 만큼의 지연시간이 생긴다. 동일한 번호에 있으므로
        answer += p * push[ord(S[i])-ord('A')] + w
    # 그 외의 경우, 다른 문자로 넘어가는 경우
    else:
        # 번호 입력만큼 곱하여 더해준다.
        answer += p * push[ord(S[i])-ord('A')]

# 출력할 문자메시지 보내는데 걸리는 시간을 출력한다.
print(answer)

```



##### [2520] 펜케이크 사랑

```python
# 팬케이스 16 x 를 만들기 위해 필요한 반죽 재료의 양
# 우유 8컵, 계란 노른자 8개, 설탕 4스푼, 소금 1스푼, 밀가루 9컵
correct_pan = [8,8,4,1,9]
# 토핑 재료
# 바나나 1개, 딸기, 30그램, 초콜릿 25그램, 호두, 10개
correct_toping = [1,30,25,10]

# 테스트 케이스의 수 T
T = int(input())
for _ in range(T):
    # 테스트 케이스의 구분
    state = input()
    # 팬케이크 반죽 재료 입력 값
    pan = list(map(int,input().split()))
    # 팬케이크 토핑 재료 입력 값
    toping = list(map(int,input().split()))

    # 만든 반죽 갯수
    create_pan = 0xffffff
    for i in range(len(pan)):
        # 해당 재료로 만들 수 있는 반죽 값
        tmp = pan[i]/correct_pan[i]
        # 그 중 최소의 값을 correct_pan 에 대입한다.
        create_pan= min(tmp,create_pan)
    # 16 x 를 만들 수 있으므로 16을 곱해준다.
    create_pan *= 16
    create_toping = 0
    for j in range(len(toping)):
        # 해당 토핑으로 만들 수 있는 팬케이크를 더해주자.
        tmp = toping[j]//correct_toping[j]
        create_toping += tmp

    # 두개의 값중 작은 쪽을 출력하자. 그게 만들어진 팬케이크의 갯수다
    print(int(min(create_pan,create_toping)))

```



##### [2789] 유학 금지

```python
# CAMBRIDGE 를 검열 하기위해, 해당 문자열을 받는 값을 두자.
# university = 'CAMBRIDGE'
# 문자열을 배열에 넣어주자, 검열대상이면 1 아니면 0으루
university = [1,1,1,1,1,0,1,0,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0]

# 값을 입력 받자
S = input()

# 출력할 값을 answer 에 추가해주자
answer = ''

# 문자열을 돌면서, 검열이 안될 경우, 추가해주자.
for s in S:
    # if s not in university:
    #     answer += s
    if not university[ord(s)-ord('A')]:
        answer += s

# 검열이 끝난 단어를 출력해주자.
print(answer)

```



##### [2948] 2009년

```python
# 달을 우선 넣어주자.
month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
# 2009년 1월 1일은 목요일(Thursday) 이다.
# 즉, 나머지가 1일떄는 목요일, 0일떄는 수요일, 6일때는 화요일이 된다.
weekday = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday','Monday', 'Tuesday']

# 첫재쭐에 D와 M이 주어진다.
D, M = map(int,input().split())

# 출력은 요일을 출력해야하므로, 총 날짜를 계산한 후, 그 값의 나머지를 통해 weekday 를 구하자.
# 총 날짜 = M * month[M] + D
date = sum(month[0:M]) + D
# 나머지에 따라 weekday 가 변하게 된다.
print(weekday[date % 7])

```



##### [2966] 찍기

```python
# 각자의 답변을 입력해두자.
# # 1. 3차원 배열 방식
# answer= [['Adrian',['A','B','C']],['Bruno' ,['B','A','B','C']],['Goran',['C','C','A','A','B','B']]]
# # 0 은 상근이, 1 은 현진이, 2 는 창영이
#
# # 최고로 많이 맞춘사람
# answer_human = []
# # 최고로 많이 맞은 갯수
# answer_count = 0
#
# # 답 수 입력 받은 값
# N = int(input())
# # 해답지
# ans = input()
#
# for i in range(3):
#     # 맞은 갯수 임시 저장
#     tmp = 0
#     # 답지 반복
#     for j in range(N):
#         # 답지와 아이들이 찍은 답안지가 일치하면 tmp + 1 을 해준다.
#         if ans[j] == answer[i][1][j % len(answer[i][1])]:
#             tmp += 1
#     # 해당 값이 최댓 값인경우, 맞은 갯수와 아이디를 저장해주자.
#     if answer_count < tmp:
#         answer_count = tmp
#         answer_human = [answer[i][0]]
#     elif answer_count == tmp:
#         answer_human.append(answer[i][0])
#
# # 저장한 값을 출력해주자.
# print(answer_count)
# for a in answer_human:
#     print(a)
# -----------------------------------------------------------------------------------------------------------
# 2. 야옹님 방식
# 답지
ans = ['ABC','BABC','CCAABB']
name = ['Adrian','Bruno','Goran']

# 최고로 많이 맞춘사람
answer_human = []
# 최고로 많이 맞은 갯수
answer_count = 0
# 답 수 입력 받은 값
N = int(input())
# 해답지
answer = input()

# 사람들의 답지를 보자.
for i in range(3):
    # 현재 답을 맞춘 개수
    tmp = 0
    for j in range(N):
        if answer[j] == ans[i][j % len(ans[i])]:
            tmp += 1
    
    # 최고로 많이 맞춘 경우
    if answer_count < tmp:
        answer_count = tmp
        answer_human = [name[i]]
    # 최고로 많이 맞춘경우와 동일한 경우
    elif answer_count == tmp:
        answer_human.append(name[i])

# 많이 맞은 갯수와 사람의 아이디를 출력하자
print(answer_count)
for a in answer_human:
    print(a)

```



##### [3154] 알람시계

```python
# 휴대폰 키보드 위치를 하나의 이차원 배열로 보고, 그 좌표값을 입력해주자.
y = [3,0,0,0,1,1,1,2,2,2]
x = [1,0,1,2,0,1,2,0,1,2]


# effort 를 구해주는 함수
def get_dist(a,b):
    return abs(x[a]-x[b]) + abs(y[a]-y[b])

# 시간과 분을 입력받자 H:M
H, M = map(int,input().split(':'))

# 시간은 99:99를 넘어갈 수 없으므로, 이를 반복문으로 넣어주자
K = 100
# 최소 노력값
efforts = 0xffffff
# 결과 시간과 분
ansH = ansM = 0

for h in range(H,K,24):
    for m in range(M,K,60):
        # 노력값을 구하자.
        tmp = get_dist(h//10,h%10) + get_dist(h%10,m//10) + get_dist(m//10,m%10)

        # 구해진 노력값보다 작으면, 그 값을 넣어주고, 답을 출력해주자.
        if tmp < efforts:
            efforts = tmp
            ansH = h
            ansM = m

# 10 보다 작으면 앞에 0을 붙여서 시를 출력한다.
if ansH<10:
    print('0'+str(ansH),end=':')
else:
    print(ansH,end=':')
# 10보다 작으면 앞에 0을 붙여서 분을 출력한다.
if ansM<10:
    print('0'+str(ansM))
else:
    print(ansM)

```



##### [4435] 중간계 전쟁

```python
# 간달프의 군대 배열
gandalf = [1,2,3,3,4,10]
# 사우론의 군대 배열
sauron = [1,2,2,2,3,5,10]

# 첫줄에 전투의 개수 T
T = int(input())
for t in range(1,T+1):
    # 간달프의 군대
    arr_G = list(map(int,input().split()))
    # 사우론의 군대
    arr_S = list(map(int,input().split()))

    # 간달프의 군대 점수
    score_G = 0
    # 사우론의 군대 점수
    score_S = 0

    for i in range(len(arr_G)):
        # 군대점수에, 해당 배열들의 곱을 더해준다.
        score_G += arr_G[i]*gandalf[i]
    for j in range(len(arr_S)):
        score_S += arr_S[j]*sauron[j]

    # 출력할 문장
    answer =''
    # 간달프의 군대가 이긴 경우
    if score_G > score_S:
        answer = 'Good triumphs over Evil'
    # 무승부인 경우
    elif score_G == score_S:
        answer = 'No victor on this battle field'
    # 사우론의 군대가 이긴 경우
    elif score_G < score_S:
        answer = 'Evil eradicates all trace of Good'

    # 최종 출력
    print(f'Battle {t}: {answer}')

```



##### [4606]The Seven Percent Solution

```python
# 딕셔너리로 풀자. 딕셔너리 key(Character) : value(Encoding)
solution = {
    ' ':'%20',
    '!':'%21',
    '$':'%24',
    '%':'%25',
    '(':'%28',
    ')':'%29',
    '*':'%2a',
}

# '#' 을 만날 때 까지는 계속해서 출력한다.
while True:
    # 문자열을 입력 받자.
    S = input()

    # '#' 을 만나면 종료
    if S == '#':
        break

    # 나중에 출력할 문자열
    answer = ''

    # 문자열을 돌면서, answer 를 추가해주자.
    for s in S:
        # 딕셔너리에 존재하는 값인 경우
        if s in list(solution.keys()):
            answer += solution[s]
        # 존재하는 값이 아닌 경우
        else:
            answer += s
    
    # 최종 출력
    print(answer)


```



##### [5585] 거스름돈

```python
# 잔돈으로 나올수 있는 수를 배열에 넣어두자.
money = [500,100,50,10,5,1]

# 물품의 가격
N = int(input())

# 거슬러 줘야하는 돈
tmp = 1000 - N

# 잔돈의 개수
answer = 0

# 줄 수 있는 잔돈 지폐를 돌면서, 개수를 센다.
for m in money:
    answer += tmp // m
    # 나누고 남은 잔돈을 tmp 에 대입하고 반복문을 반복한다.
    tmp = tmp % m

# 최종 잔돈의 개수를 출력한다.
print(answer)


```



##### [5622] 다이얼

```python
# 알파벳에 따른 걸리는 시간을 배열화
alpha = [3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,8,9,9,9,10,10,10,10]

# 할머니가 입력한 알파벳 대문자
S = input()

# 출력할 최소시간
answer = 0

# 해당 문자열을 반복하면서, 최소시간을 출력한다.
for s in S:
    answer += alpha[ord(s)-ord('A')]

# 걸린 시간을 출력한다.
print(answer)

```



##### [6368] P,MTHBGWB

```python
# 알파벳을 문자열로 접근하자.
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_.,?'
# 모스 부호를 리스트로 접근하자.
mos = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','..--','---.','.-.-','----']

# 알파벳과 모스부호의 index는 동일하다. 우선 답안지를 구하고, 역순으로 해보자

# 테스트케이스의 수 T
T = int(input())
for tc in range(1,T+1):
    # 문자열을 입력받고
    S = input()
    # 인코딩된 모스부호 길이를 저장할 함수 (mos length)
    ml = []
    # 모스부호로 전환한 문자열을 받아줄 tmp
    tmp = ''

    for s in S:
        tmp += mos[alpha.index(s)]
        ml.append(len(mos[alpha.index(s)]))
        # print(s,mos[alpha.index(s)])

    # 답을 출력하자
    answer = ''

    # 현재 인덱스의 위치
    idx = 0
    # 슬라이싱으로 접근하여 decode를 하자.
    for m in ml[::-1]:
        answer += alpha[mos.index(tmp[idx:idx+m])]
        idx += m
    
    # 최종 decode 한 문장 출력
    print(f'{tc}: {answer}')

```



##### [6750] Rotating letters

```python
# 회전해도 그대로인 문자를 문자열에 저장하자
letters = 'IOSHZXN'

# 입력을 받자
S = input()

# 반복하면서, 회전하지 않는 문자가 나오면, NO를 바로 출력하자
for s in S:
    if s not in letters:
        print('NO')
        break
# 모두 회전문자이면 YES 를 출력하자.
else:
    print('YES')

```



#### [6765] Icon Scaling

```python
# 우선 배열에 담아주자
arr = ['*x*',' xx','* *']

# 몇배로 늘릴지 값을 받아주자
K = int(input())
# 우선 모든 길이가 3이니까 3을 변수에 담아주자
n = 3

# 우선 원본 높이을 가져오고
for i in range(n):
    # 높이를 K 배 늘려주자.
    for k in range(K):
        # 원본 길이를 가져오고
        for j in range(n):
            # 길이도 K배 늘려주자.
            for l in range(K):
                # 띄움 없이 print 해주고
                print(arr[i][j],end='')
        # 길이를 출력 끝냈으면 개행 해주자.
        print()

```



##### [11800] Tawla

```python
# 딕셔너리로 우선 주사위 고유별칭을 담아주자.
dice = {1:'Yakk',2:'Doh',3:'Seh',4:'Ghar',5:'Bang',6:'Sheesh'}
double_dice = {1:'Habb Yakk',2:'Dobara',3:'Dousa',4:'Dorgy',5:'Dabash',6:'Dosh'}
# 테스트 케이스의 수는 T 이다.
T = int(input())
for tc in range(1,T+1):
    # 던진 주사위를 리스트로 받고, 이를 내림차순 해주자.
    throw = list(map(int,input().split()))
    throw.sort(reverse=True)

    # 주사위의 눈이 일치할 경우
    if throw[0] == throw[1]:
        print(f'Case {tc}: {double_dice[throw[0]]}')
    # Sheesh Bang 이 나오는 5-6, 6-5 의 경우
    elif throw[0]==6 and throw[1]==5:
        print(f'Case {tc}: Sheesh Beesh')
    # 일치하지 않을 경우,
    else:
        print(f'Case {tc}: {dice[throw[0]]} {dice[throw[1]]}')

```



##### [10551] STROJOPIS

```python
# 1. 알고리즈 바보 방식
# # 일단 손가락 쓴거를 count 할 배열을 만들어주자
# sol = [0,0,0,0,0,0,0,0]
# # 숫자를 눌렀을 경우, 필요한 손가락 번호를 배열로 만들어두자.
# number = [7,0,1,2,3,3,4,4,5,6]
# # 영문자를 눌렀을 경우, 필요한 손가락 번호를 배열로 만들어두자. A 부터 시작
# alpha = [0,3,2,2,2,3,3,4,5,4,5,6,4,4,6,7,0,3,1,3,4,3,1,1,4,0]
# # 그외는 모두 7에다가 넣어주자.
#
# # 문자열을 받는다.
# S = input()
#
# for s in S:
#     # 숫자일 경우, int 형으로 변환하여 sol 에 count 해주자.
#     if '0'<=s<='9':
#         sol[number[int(s)]] += 1
#     # 문자일 경우, ord 를 활용하여 인덱스에 접근하자.
#     elif 'A'<=s<='Z':
#         sol[alpha[ord(s)-ord('A')]] +=1
#     # ',' 일 경우, 5번에 count 해주자.
#     elif s==',':
#         sol[5] +=1
#     # '.' 일 경우, 6번에 count 해주자.
#     elif s=='.':
#         sol[6] +=1
#     # 그 외의 경우는 7번에 모두 넣어주자.
#     else:
#         sol[7] +=1
#
# # 이제 손가락 별로 사용횟수를 출력하자
# for s in sol:
#     print(s)
# --------------------------------------------------------------------
# 2. 알고리즘 폐하 방식
# 배열을 key:value 형태로 매칭하자
key = "`1QAZ2WSX3EDC4RFV5TGB6YHN7UJM8IK,9OL.0P;/-['=]\\"
val = [0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,7,7,7,7,7]
# 출력할 배열
sol = [0]*8

# 문자열을 받자
S = input()

# 반복문을 돌면서 count 해주자.
for s in S:
    sol[val[key.index(s)]] += 1

# 출력 해주자
for s in sol:
    print(s)

```

