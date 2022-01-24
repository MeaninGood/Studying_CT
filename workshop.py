
# 1
def get_dict_avg(sub) :
    
    li = []
    for i in sub :
        li.append(i)    
    
    total = 0
    for j in li :
        total += sub[j]
        
    return total / len(li)


get_dict_avg({
    'python' : 80,
    'algorithm' : 90,
    'django' : 89,
    'web' : 83,
})


''' 다른 코드 1
def get_dict_avg(my_dict):
    total = 0 
    for key in my_dict:
        total += my_dict[key]
    my_average = total / len(my_dict)
    return my_average 

'''

''' 다른 코드 2
def get_dict_avg(grade):
    sum_ = 0
    for value in grade.values():
        sum_ += value
    
    avg = sum_/len(grade)
    return avg

'''

''' 다른 코드 3
def get_dict_avg(subjects):
    total = 0
    length = 0
    for subject in subjects:
        length += 1
        total += subjects[subject]
    return total / length

'''


''' 다른 코드 4
def get_dict_avg(scores):
    cnt = 0
    sum = 0
    for key in scores.keys():
        cnt += 1
    for value in scores.values():
        sum += value
    return sum / cnt

'''



# 2. 


def count_blood(blood) :
    li = []
    
    for i in blood :
        li.append(i)
        
    idx = list(set(li))
    
    cnt = {}
    for i in idx :
        cnt[i] = blood.count(i)
        
    return cnt
    

count_blood( [
    'A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB'
])


''' 다른 코드 1
def count_blood(blood):
    type = ['A', 'B', 'O', 'AB']
    count_blood =[]
    dict_ = {}
    for t in type:
        count_blood.append(blood.count(t))
    for i in range(len(type)):
        dict_.update({type[i] : count_blood[i]})
    return print(dict_)

'''

def count_blood(bloods) :
    blood_dict = {}
    for blood in bloods :
        if blood_dict.get(blood) : # 키 있으면
            blood_dict[blood] += 1 # value += 1해줌
        else :
            blood_dict[blood] = 1 # 키 없으면 하나 생성, value 1 넣어줌
                                # 무조건 하나는 있으니까!
        
        
## value 호출
## blood_dict['key'] # value 없으면 에러 반환
## blood_dict.get()  # value 없으면 None      

## homework

1

def count_vowels(word) :
    idx = ['a', 'e', 'i', 'o', 'u']
    
    cnt = 0
    for i in idx :
        cnt += word.count(i)
    return cnt

print(count_vowels('apple'))
print(count_vowels('banana'))


''' 다른 코드 ## 리스트 따로 만들 필요 없이, 문자열 바로 돌 수 있다.
def count_vowels(word):
    result = 0
    for i in 'aeiou':
        result += word.count(i)
    return result
    
'''

# 2 : 4번


#3

def only_square_area(num1, num2) :
    
    li = []
    for i in num1 :
        for j in num2 :
            if i == j :
                li.append(i*j) 
    print(li)
            
only_square_area([32, 55, 63], [13, 32, 40, 55])


''' 다른 코드
def only_square_area(list1, list2) :
    value = set(list1) & set(list2) # 교집합, 똑같은 것만 남기기
    return [i**2 for i in value]
only_square_area([32, 55, 63], [13, 32, 40, 55])

'''

def only_square_area(widths, heights) :
    comb = [ widths*height for width in widths for height in heights if width == height]
    return comb