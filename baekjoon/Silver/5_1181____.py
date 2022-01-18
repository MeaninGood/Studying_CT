# 1181번_단어 정렬

## 알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래의 조건에 따라 정렬
## 1. 길이가 짧은 것부터
## 2. 길이가 같으면 사전 순으로


'''
# 첫째 줄에 단어의 개수 N
# 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가
# 한 줄에 하나씩 주어짐.
## 조건에 따라 정렬하여 단어들 출력. 단, 같은 단어가 여러 번 입력된 경우
## 한 번씩만 출력

(입력 - \n 기준) 6 but i wont hesitate i more
(출력) i but more wont hesitate

'''


# 800ms

# n = int(input()) # 단어 개수 n개

# li = [] # 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어짐
# for i in range(n) :
#     li.append(input()) # li 리스트에 추가해 줌

# liset = set(li)
# lst = list(liset)
# lst.sort()
# lst.sort(key=len)


# print(*lst)

'''
sort로 문자 정렬하는 문제

< 정렬 순서 주의할 것 !!! >
상위 조건 A와 하위 조건 B가 있으면
먼저 B로 정렬 후 A로 정렬해야 함!!

위 문제에서 정렬 조건
1. 길이가 짧은 것부터 (A)
2. 길이 같으면 사전순 (B)
3. 중복 제거
이므로 

중복제거 먼저 할 것!
단, set은 sort를 사용할 수 없으므로
set -> list 과정 한 번 거쳐야 함

사전순(B) -> 길이 짧은 것(A)
순으로 sort 사용

'''


# 860ms

# n = int(input()) 
# li = []

# for i in range(n) :
#     li.append(input())

# liset = set(li)
# lst = list(liset)
# lst.sort()
# lst.sort(key=len)


# for i in lst :
#     print(i, end = ' ')


### 104ms ---> 미쳤넹 고냥 ###
import sys

n = int(sys.stdin.readline()) 
li = []

for i in range(n) :
    li.append(sys.stdin.readline().strip()) # 한 줄 씩 입력받을 때 .strip()

liset = set(li)
lst = list(liset)
lst.sort()
lst.sort(key=len)


for i in lst :
    print(i, end = ' ')