# int를 str로 바꿔서 출력하기


# 1. 한 줄 씩 쪼개서 출력하기

# a = list(range(1,11))

# for i in range(a) : # 일단 a에 저장된 값 하나씩 다 돌면서 보기
#     for j in str(a[i]) : # a의 [i]번 값을 문자(str)로 출력
#         print(j)



''' 출력
1
2
3
4
5
6
7
9
1 # 10이 1과 0으로 나눠서 출력됨
0
'''


# 리스트 그대로 출력해보기

# a = list(range(1,11))
# b = str(a)
# print(b[0])



# 입력 받은 숫자를 문자로 쪼개서 더하기
# 75 = 7 + 5 = 12 만들기

# a = 75
# b = map(int, str(a)) # 75를 7과 5로 쪼개고, int로 바꿔서 연산해 줌
# print(sum(b))



# 꼭 map으로 묶어야 하나? 리스트로 묶으면 안 되나? 해서 해 본 코드
a = 75
b = [int(str(a))]
print(sum(b)) # 출력 75




''' 에러 코드 1
a = 75
b = list(int(str(a)))
print(sum(b)) # TypeError : 'int' object is not iterable

'''



''' 에러 코드 2
a = 75
b = int(str(a))
print(sum(b)) # TypeError : 'int' object is not iterable

'''


# a = 75
# b = map(int, str(a))
# print(sum(b)) # 출력 12

