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

(입력 - \n기준) 6 but i wont hesitate i more
(출력) i but more wont hesitate

'''



n = int(input())
li = []

for i in range(n) :
    li.append(input())
    li.sort(key=len)

li.sort()

print(li)