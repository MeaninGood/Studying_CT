# 10814번_나이순 정렬

## 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서

'''
# 첫째 줄에 개수 N
# 둘째 줄부터 N개의 줄에 각 회원의 나이와 이름이 공백으로 구분되어 주어짐
# 입력은 가입한 순서대로
## 첫째 줄부터 총 N개의 줄에 걸쳐 나이순으로, 나이가 같으면 가입한 순으로
## 한 줄에 한 명씩 나이와 이름을 공백으로 구분해 출력

(입력)
3
21 Junkyu
21 Dohyun
20 Sunyoung

(출력)
20 Sunyoung
21 Junkyu
21 Dohyun  

'''


'''
정렬 순서
나이순(A) -> 나이가 같으면 가입한 순(B)

B -> A 순으로 정렬

'''

from sys import stdin
n = int(stdin.readline())

'''리스트로 저장하니까 
[<map object at 0x000002A87DF64E50>, <map object at 0x000002A87DF64DF0>]
이런 에러가 뜸

li = []
for i in range(n) :
    li.append(list(map(str, stdin.readline().split())))

'''
print(li)