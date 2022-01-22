# 딕셔너리

# grades = {'john' : 80, 'eric' : 90}

# for student in grades :
    # print(student) # john, eric
    
    # print(student, grades[student]) # john 80, eric 90
    
    
    
# print(grades.keys())
# print(grades.values())
# print(grades.items())

# for name, score in grades.items() :
#     print(name, score) # 앞에가 key, 뒤에가 value
    
    
    

# members = ['민수', '영희', '철수']

# for idx, member in enumerate(members) :
#     print(idx, member)



# seasons = ['spring', 'summer', 'fall', 'winter']
# print(list(enumerate(seasons)))


# print(list(enumerate(seasons, start = 1)))





# members = [
#     		[0, 0, 0],
#     		[0, 0, 0],
#     		[0, 0, 0]
# 			]

# for number in numbers :
#     for num in number :
#         print(num)
        
# # members[0][0] -> members[1][0] -> members[2][0] -> members[0][1] ... 순으로 출력


# numbers = [
#     		{'items' : [1, 2, 3, '철수']}
# 			]

# # '철수' 뽑기
# numbers[0]['items'][?]
# if items == '철수' :
# numbers[리스트][딕셔너리][리스트]



# =========================================

numbers = [
    		{'items' : [1, 2, 3, '철수']},
    		{'items' : [1, 2, 3, '영희']}
			]

for number in numbers :
    print(number) # 딕셔너리 {} 하나씩 나옴
    for key in number :
        print(key) # 키만 따로 나옴
        print(number[key]) # value만 나옴
        for i in number[key] :
            print(i) # value만 하나씩 따로 나옴 1 ~ '철수'
            if i == '철수' : 
                print(i, '정답') # 철수 정답 이라고 나옴 