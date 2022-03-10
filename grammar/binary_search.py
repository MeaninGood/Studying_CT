# 이진탐색

'''
병뚜껑 게임 27 찾기
1~50까지의 수

[1, 50]
25 : 업 -- 확실한 건 1부터 25까지는 답이 아니다

[26, 50]

37 : 다운

[26, 36]


# 코드

ans = 27

s = 1
e = 50
while s <= e:
    mid = (s + e) // 2
    
    if mid == ans:
        print(ans)
        
    elif mid < ans:
        s = mid + 1
        
    else:
        e = mid - 1

'''     
        
        
        
# 10815

'''
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10


(정렬)
5
-10 2 3 6 10
s    mid   e
s   e
    s e

'''

# n = int(input())
# arr = sorted(list(map(int, input().split())))
# m = int(input())
# arr2 = list(map(int, input().split()))

# for i in arr2:
#     ans = 0 
    
#     s = 0
#     e = n - 1
    
#     while s <= e:
#         mid = (s + e) // 2
        
#         if arr[mid] == i:
#             print(1)
            
#         elif arr[mid] < i:
#             s = mid + 1
        
#         else:
#             e = mid - 1
            
#     print(ans, end=' ')



'''
# 이진 탐색 응용

우리가 원하는 수 x, 이거보다 작은 거 l, 큰 거 r이라고 하면
l l l l l l l l x x x x x r r r r r r r 

x중 제일 왼쪽 인덱스?
x중 제일 오른쪽 인덱스?

# 제일 왼쪽 인덱스 찾을 때
if mid == l:
  s = mid + 1
elif mid == r:
  e = mid - 1
elif mid == x:
  ans = mid (저장하고)
  e = mid - 1 (e를 줄이기)
  s = mid + 1 (제일 오른쪽 거 찾을 때)
  
  
개수 : r의 가장 왼쪽 인덱스 - x의 가장 왼쪽 인덱스 + 1


'''

'''
# 10816

n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    idx = 0
    
    s = 0
    e = n - 1
    while s <= e:
        mid = (s + e) // 2
        
        if arr[mid] == i:
            idx = mid
            e = mid - 1
            
        elif arr[mid] < i:
            s = mid + 1
        
        else:
            e = mid - 1
            
    idx2 = 1 # 어차피 x가 있으면 얘는 바뀔 거고, x가 없으면 프린트에서 0이 출력되어야 하니까
            # 1로 바꿔주면 됨
    s = 0
    e = n - 1
    while s <= e:
        mid = s(s + e) // 2
        
        if arr[mid] == i:
            idx2 = mid
        elif arr[mid] < i:
            s = mid + 1
        else:
            e = mid - 1
            
    print(idx2 - idx + 1, end=' ')
    
'''

'''
이진탐색(binary search) B(O) = log(N)
100만 = > 20번
10억 => 30번 안에 탐색 가능
1. 정확히 어떤 수를 찾는다.
2. 어떤 수의 인덱스 중 가장 왼쪽, 오른쪽 인덱스를 찾는다.


x x x x x x x x x x x x o o o o o o o o o o
이중에 제일 왼쪽
o o o o o o o o o o x x x x x x x x x
이중에 제일 오른쪽
'''



'''
매개변수 탐색(parametric search)
l l l l l l l l x x x x x r r r r r r r

x가 존재한다는 가정하에
x중에서 가장 왼쪽 찾기 = x보다 큰 애들 중에 가장 왼쪽 찾기( 같은 말 )


while s <= e:
    mid = (s + e) // 2
    
    if arr[mid] >= x :
        ans = mid
        e = mid - 1
    else:
        s = mid + 1
'''


# 2805 나무자르기
'''
4 7
20 15 10 17

0   1   2   3   4   ... 15  16  17  18  19  20
62  58  54  50  46  ... 7   5   3   2   1   0


0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
o o o o o o o o o o  o  o  o  o  o  o  x  x  x  x  x

'''
# def check(x):
#     total = 0
    
#     for i in arr:
#         if i >= x:
#             total += i - x
    
#     return total >= m

# 위 식을 더 예쁘게 짜기
def check(x):
    total = 0
    
    for i in arr:
        total += max(0, i - x) # i - x를 더해라, 음수면 0 더해라
    
    return total >= m # True, False return

        
n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
s = 0
e = 1000000000
while s <= e:
    mid = (s + e) // 2
    
    if check(mid):
        ans = mid
        s = mid + 1
        
    else:
        e = mid - 1
        
print(ans)


# 이동 방향 찾아주고, check만 바꾸기


# 1654번 랜선 자르기
'''
출력해야 할 게 탐색 범위임
아까는 자를 위치, 이번에는 랜선의 최대 길이

11개
길이
1   2   3   4   5   6   7   8   9   10  11
o   o   o   o   o   o   x   x   x   x   x


'''


def check(x):
    total = 0
    
    for i in arr:
        total += i // x
    
    return total >= m

n, m = map(int, input().split())
arr = [int(input()) for i in range(n)]

s = 1
e = 1000000000000
while s <= e:
    mid = (s + e) // 2
    
    if check(mid):
        ans = mid
        s = mid + 1
        
    else:
        e = mid - 1
        
print(ans)



# 2792 보석 상자
# 최대값을 최소화해라 (제일 큰 거를 최대한 작게 만들어 봐라)
# 혹은 최소값을 최대화 (제일 작은 거를 최대한 크게 만들어 봐라)
# 어지간하면 이진탐색
# o o o o o o x x x x x x x x x x 이런 형태가 되냐 안 되냐

## 어떤 위치에서 체크하는 걸 만들 수 있냐 + 단조성이 있냐

'''
질투심
1   2   3   4   5   6   7   8   9 ...
x   x   o   o   o   o   o   o   o ...

'''

def check(x):
    total= 0
    
    for i in arr:
        if i % x == 0 :
            total += i // x

        else:
            total += i // x + 1
            
    return total <= m

## 숏코딩

# def check(x):
#     total= 0

#     for i in arr:
#         total += i // x + (i % x != 0) # True면1, False면 0임
            
#     return total <= m


m, n = map(int, input().split())
arr = [int(input()) for i in range(n)]

s = 0
e = 100000000000
while s <= e :
    mid = (s + e) // 2
    
    if check(mid):
        ans = mid
        e = mid - 1
        
    else:
        s = mid + 1
        
print(ans)



# 1300 K번째 수

'''
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25


1 2 3
2 4 6
3 6 9

1 2 2 3 3 4 6 6 9

7번째 수 : 6이 답임

n x n 배열 만들지 말고 k번째 수만 찾아라

1   2   3   4   5   6   7   8   9
위의 숫자보다 작거나 같은 게 몇 개냐?
1   3   5   6   6   8   8   8   9
7번째 수 : 나 포함해서, 나보다 작거나 같은 게 7개 이상
x   x   x   x   x   o   o   o   o

? ? ? ? ? ? 6 6 // 5보다 작거나 같은 게 뭔진 몰겠지만 앞에 6개 있다
6보다 작거나 같은 걸 적으니까 8개가 됐다 = 6이 2개가 있다


mid = 140
1   2   3   4   5   6   ...     100 // 100개 있음
2   4   6   8   10  ...         200 // 70개 있음
3   6   9   12  15 ...          300 // 46개 있음

...

100 200 300                     10000


'''

def check(x):
    total = 0
    
    for i in range(1, n+1):
        total += min(n, x // i) #많아도 n개를 넘기지 마라
        
    return total >= m
        
    
n = int(input())
m = int(input())

ans = 0
s = 1
e = n * n
while s <= e:
    mid = (s + e) // 2
    
    if check(mid):
        ans  = mid
        e = mid - 1
        
    else:
        s = mid + 1
        
print(ans)



