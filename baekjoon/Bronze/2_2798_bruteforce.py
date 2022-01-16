# 2798번_블랙잭_brute force

## N장의 카드 중에 3장의 카드를 고름
## 고른 카드의 합이 M을 넘지 않으면서 M과 최대한 가깝게 만들기
## N장의 카드에 써져 있는 숫자가 주어짐

'''
# 첫째 줄에 카드의 개수 N과 M이 주어짐
# 둘째 줄에 카드에 쓰여 있는 수가 주어짐
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 주어짐

## M을 넘지 않으면서 M에 최대한 가까운 3장의 합 출력
'''


import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
cards.sort() 

# 카드를 오름차순으로 정렬.
# 밑에 break문을 써주었으므로, 마지막에 인덱스가
# 012, 013, 014 이런 식으로 돌아야 하는데
# 012에서 m보다 값이 커지면 k for문이 돌지 않음

# 정렬을 안 쓰려면 아래 break 대신 continue 써줄 것
# 단 continue를 쓰면 시간복잡도 O(n^3)을 다 돌게 되는데,
# 정렬한 후 break를 걸면 m 이상인 수가 된 순간부터 뒷부분 돌지 않아서
# 시간 복잡도 감소함

cards_li = [] # 3장의 카드 합을 담는 리스트입니다


for i in range(n-2) : # 맨 첫장부터 n-2까지 도는 거
    # sum_3cards = 0
    for j in range(i+1, n-1) : # 그 다음장부터 n-1까지 도는 거  
        for k in range(j+1, n) : # 3번째 장부터 마지막장까지 도는 거
            sum_3cards = cards[i]+cards[j]+cards[k]
            if sum_3cards > m : # 카드 합이 m을 넘어서면 멈춤
                break
            cards_li.append(sum_3cards) # m보다 작은 3장의 합들만 리스트에 추가


print(max(cards_li)) # 리스트 중 max값 출력

''' 출력

for i in range(n-2) :
    for j in range(1, n-1) :
        for k in range(2, n) :
            으로 했을 때 
[18, 19, 20, 19, 20, 21, 20, 21, 22, 19, 20, 
21, 20, 21, 22, 21, 22, 23, 20, 21, 22, 21, 22, 
23, 22, 23, 24]

이렇게 뜸

반복문 시작하는 자리가 고정 되어 있기 때문에 코드가 이상하게 돔

5+6+7 = 18, 5+6+8 = 19, 5+6+9=20, 5+7+7 = 19, 5+7+8 = 20으로 쓰이며
5+7+7이 다시 나옴

그러므로, 시작하는 자리를 0,1,2로 고정해두지 말고
0, i+1, j+1로 바꿔줄 것 


'''





''' 다른 코드 1 -  def 이용
def check_plus(a):
    if a <= in_put[1]:
        answer.append(a)
 
in_put = input()
in_put = in_put.split(" ")
in_put = list(map(int, in_put)) #처음 입력값을 받아 N과 M을 분리
# N = in_put[0]  , M = in_put[1]
 
card = input()
card = card.split(" ")
card = list(map(int, card)) #각 카드의 값을 리스트화
 
 
answer = [] # M을 넘지 않는 각 카드의 합
for i in card:
    compare = card[:] #lits card의 값이 사라지면 곤란하므로
    m_answer = 0
    m_answer += i
    f_num = m_answer
    compare.remove(i) #첫번째 카드를 더하고, 리스트에서 제거
    for j in compare:
        m_num = f_num # 첫 카드를 뽑은 값으로 돌아오기 위함.
        m_num += j
        compare.remove(j)
        for k in compare:
            l_num = m_num #두번째 카드까지의 합으로 돌아오기 위함.
            l_num += k
            check_plus(l_num)
 
print(max(answer))

'''




''' 다른 코드 2
import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

result = 9999999 # result에 결과에 영향이 가지 않는 무관한 값 입력
for i in range(n-2) : # 맨 첫장부터 n-2까지 도는 거
    # sum_3cards = 0
    for j in range(i+1, n-1) : # 그 다음장부터 n-1까지 도는 거
        for k in range(j+1, n) : # 3번째 장부터 마지막장까지 도는 거
            sum_3cards = cards[i]+cards[j]+cards[k]
            if m - sum_3cards <= result and m>=sum_3cards:
                # m이 3카드의 합보다 크다면
                result = m - sum_3cards # result를 m에서 sum_3cards를 뺀 값으로 대체
print(m-result) # m에서 차이값 뺀 것(result에 저장됨) 출력

'''




''' 다른 코드 3 -  set으로 중복 제거
n, m = map(int, input().split())

inputNumList = list(map(int,input().split())) #입력을 받아 리스트에 저장
sumSet = set() #중복을 허용하지 않는 set자료형 선언(입력받은 숫자 중 3개의 숫자 합을 저장하기 위해)
sumArray = [] #m보다 작거나 같은 원소만 저장하기 위한 리스트 선언


#반복문을 돌면서 3가지 숫자의 합을 구해야하는데 i==j 이거나 j==k이거나 i==k 일때는 중복이므로
#if문을 걸어 그 경우의 수를 제외시켜 준다.
for i in inputNumList: #입력받은 숫자에 접근
    for j in inputNumList[1:]: #입력받은 숫자의 맨앞원소의 바로 뒤에있는 원소부터 접근
        if i == j: #3개의 숫자중 첫번째 원소와 두번째 원소가 같을 때의 경우수는 반복문을 돌지 않는다.
            break
        for k in inputNumList[2:]: #입력받은 숫자의 맨앞원소의 다음 2번째 에있는 원소부터 접근
            if k == j or k == i: #3개의 숫자중 두번째 원소와 세번째 원소가 같을 때 혹은 첫번째와 세번째가 같은 경우수는 반복문을 돌지 않는다.
                break
            sumSet.add(i + j + k) #3가지 숫자의 합을 집합자료형에 대입하면 같은 수는 중복을 제거해준다.

for i in sumSet: #집합자료형을 돌면서
    if i <= m: #만약 원소가 m보다 작거나 같다면
        sumArray.append(i) #리스트에 그값들을 대입해준다.
print(max(sumArray)) #그 중에서 가장 큰 값을 출력

'''


''' 다른 코드 4 - 파이썬 내장 함수 combinations

from itertools import combinations

n, m = map(int, input().split())
card_list = list(map(int, input().split()))
result = 0 #결과값을 저장하기 위한 변수

for i in combinations(card_list, 3): #combinations 함수를 이용하면 파이썬에서 중복을 허용하지 않고 3개를 뽑아준다.
    if sum(i) <= m: #만약 그 3개의 합이 m보다 작거나 같다면
        result = max(result, sum(i)) #그 값을 result값에다 대입하는데 기존에 있던 result값이 크다면 대입하지 않는다.


print(result)
'''