# 4673번_셀프넘버

## 셀프넘버 : 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수
## d(75) = 75 + 7 + 5 = 87
## n이 d(n)의 생성자, 생성자가 없는 숫자를 셀프넘버로 정함

## 입력 없음
## 10,000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 증가하는 순서로 출력

'''
100보다 작은 셀프 넘버 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97
1 => 셀프 넘버
2 => 생성자 : 1 // 1 + 0 + 1 
3 => 셀프 넘버
4 => 생성자 : 2 // 2 + 0  + 2
5 => 셀프 넘버
6 => 생성자 : 3 // 3 + 0 + 3
7 => 셀프 넘버
8 => 생성자 : 4 // 4 + 0 + 4
9=> 셀프 넘버 
10 = > 생성자 : 5 // 5 + 0 + 5
11 => 생성자 : 10 // 10 + 1 + 0
12 => 생성자 : 6
13 => 생성자 : 11 // 11 + 1 + 1
'''


'''
# d(75) = 75 + 7 + 5 = 87 
# 이렇게 하려면 int로 받고 str로 쓰기?

a = int(input())
b = str(a)
print(b[0])

# 입력 : 867
# 출력 : 8
'''

# number =list(range(1, 11)) # 1부터 11까지 숫자가 적힌 리스트
# snumber = [] # 셀프넘버 저장할 공간

# for i in range(len(number)) : # 일단 number에 저장된 값 하나씩 다 돌면서 보기
#     for j in str(number[i]) : # 각 값을,,,, 쪼개서,, 생성자 찾기
        
# ## 생성자를 찾으라고 함
# ## d(75) = 75 + 7 + 5 = 87
# ## 이걸 함수로 만들어야 함

def d(n) : # 셀프넘버 생성해주는 함수 만들기
    n = n + sum(map(int, str(n))) 
    # 이것저것 해보다가 sum(map(int, str(n)))이 된다는 것 찾음
    # 위 식을 해석하면, d(75) = 75 + (7 + 5) = 87이라는 뜻
    return n # 문제의 설명대로 n에 저장하고 return 
        
        
numbers = list(range(1, 10001)) # 1부터 10,000까지의 숫자
 
Snumbers = [] # 생성자가 들어갈 리스트
 
for i in range(len(numbers)) : # numbers 변수에서
     Snumbers.append(d(i)) # d(n)함수를 이용해 생성자를 찾아서 Snumbers에 추가

for j in range(len(numbers)) : 
    # Snumbers 출력해보면 10035까지 나오는데
    # 우리가 알고 싶은 건 10,000까지니까 10,000까지만 지정
    # 직관적으로 보이기 위해 range(1, 10001)이 아니라 그냥 len(numbers)라고 함
    if j not in Snumbers : # 1~10,000까지의 숫자 중 Snumbers에 없는 숫자
        # 즉, 생성자가 아닌 숫자 = 셀프넘버
        print(j) # 출력
        
        
        
        
        
        
        
        
        

''' 다른 코드 1
visited = [False for i in range(10010)]

def nxt(x):
    ret = x
    while x > 0:
        ret += x % 10
        x //= 10

    return ret

for i in range(1, 10000):
    x = nxt(i)

    while x <= 10000 and not visited[x]:
        visited[x] = True
        x = nxt(x)

for i in range(1, 10001):
    if not visited[i]:
        print(i)

'''


''' 다른 코드 2
lst = set([i for i in range(1,10001)])
notSelf = set()
sum = 0

for i in lst:
    for j in str(i):
        sum += int(j)
    if sum+i in lst:
        notSelf.add(sum+i)
    sum = 0

for k in sorted(lst - notSelf):
    print(k)

'''


''' 다른 코드 3
not_self = [True]*10001

for i in range(1,10001):
    tmp = i
    s = str(i)
    for j in range(len(s)):
        tmp += int(s[j])
    if tmp<=10000:
        not_self[tmp]=False
        
for i in range(1,10001):
    if not_self[i]:
        print(i)

'''

