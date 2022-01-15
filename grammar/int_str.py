# int를 str로 바꿔서 출력하기


# a = list(range(1,11))

# for i in range(a) : # 일단 number에 저장된 값 하나씩 다 돌면서 보기
#     for j in str(a[i]) : # 각 값을,,,, 쪼개서,, 봐야하는데
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


# 나중에 다시 해보고 정리해놓기 대충 b[0] 하면 [ <- 나옴
# a = list(range(1,11))
# b = int(str(a))
# print(b)



# 75 = 7 + 5 만들기

# a = 75
# b = map(int, str(a))
# print(sum(b))


'''
a = 75
b = [int(str(a))]
print(sum(b)) # 출력 75

'''


'''
a = 75
b = int(str(a))
print(sum(b)) # typeError : 'int' object is not iterable

'''


a = 75
b = map(int, str(a))
print(sum(b)) # 출력 12

