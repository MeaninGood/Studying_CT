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

# from sys import stdin
# n = int(stdin.readline())

'''리스트로 저장하니까 
[<map object at 0x000002A87DF64E50>, <map object at 0x000002A87DF64DF0>]
이런 에러가 뜸

li = []
for i in range(n) :
    li.append(list(map(str, stdin.readline().split())))

'''
# from sys import stdin
# n = int(stdin.readline())

# age = []
# name = []
# for i in range(n) :
#     member = list(map(str, stdin.readline().split()))
    # for j in range(1) :
    #     a = int(name[i][j])
    #     age.append(a)
    #     b = name[i][j+1]
    #     name.append(b) ### IndexError: list index out of range
        
        
# print(name)
# print(age)

# dict_sort ={}
# for _ in range(N):
#   age, name = input().split()
#   if dict_sort.get(age):
#     dict_sort[age].append(name)
#   else:
#     dict_sort[age] = [name]
    
 
 
import sys
N = int(sys.stdin.readline())

    
dict_sort = {}
for i in range(N) :
    age, name = sys.stdin.readline().split()
    if dict_sort.get(name) :
        dict_sort[name].append(age)
    else :
        dict_sort[name] = age

result = sorted(dict_sort.items(), reverse = True)
for i in range(N) :
    print(result[i][1], result[i][0])


# 딕셔너리로 받아서
# 나이순으로만 정렬 -> 가입순 자동으로 맞춰짐




# 나중에 lambda 를 활용한 정렬 방식도 한번 활용해보세용!

#   if dict_sort.get(age):
#         dict_sort[age].append(name)
#   else:
#     dict_sort[age] = [name]
    
# key값이 없으면 value 에 리스트형태로 대입
# key 값이 있으면 value 에 append 해주는 형태로하면
# 나이: 이름 으로 할 수 있어용!




################## 0120 무조건 보기!!!!!!
import sys

N = int(sys.stdin.readline())

dict_sort = {}
for _ in range(N):
    age, name = sys.stdin.readline().split()
    if dict_sort.get(int(age)):
        ## 키값이 있으면 append 로 value를 추가한다.
        dict_sort[int(age)].append(name)
    else:
        ## 키값이 없으면 key:value 를 추가해 key값을 넣는다.
        dict_sort[int(age)] = [name]
result = sorted(dict_sort.keys())
# print(dict_sort)
for k in result:
    tmp = dict_sort[k]
    for t in tmp:
        print(k,t)
        
        
        
N = int(input())
arr = []
for _ in range(N):
    arr.append(input().split())
arr.sort(key = lambda x: int(x[0]))
for a in arr:
    print(*a)