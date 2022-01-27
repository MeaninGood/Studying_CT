# 2309번_일곱 난쟁이

## 일곱 난쟁이 키의 합이 100
## 아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱명 찾는 프로그램

'''
# 아홉 개의 줄에 걸쳐 난쟁이들의 키가 주어짐
# 가능한 정답이 여러가지인 경우에는 아무거나 출력
## 일곱 난쟁이의 키를 오름차순으로 출력. 찾을 수 없는 경우는 없음
(입력)
20
7
23
19
10
15
25
8
13

(출력)
7
8
10
13
19
20
23

'''

# heit = []
# for i in range(9) :
#     heit.append(int(input()))

# temp = sum(heit)-100
# print(heit)    
# for j in range(8) :
#     # print(heit[j], end = ' ')
#     for k in range(j+1, -1) :
#         print(len(heit))
#         if heit[j] + heit[k] == temp :
#             heit.remove(heit[j])
#             heit.remove(heit[k])
    
# print(sorted(heit))           
    
    

heit = []
for i in range(9) :
    heit.append(int(input()))

temp = sum(heit)-100
# print(heit)

# while 1 :
     
for j in range(8) :
    # print(heit[j], end = ' ')
    length = 9
    for k in heit[j+1:length-1] :
        # print(len(heit))
        if heit[j] + k == temp and len(heit) == 9:
            heit.remove(heit[j])
            length -= 1
            heit.remove(k)
            
        # if len(heit) == 7 :
        #     break
        # else :
        #     continue
            
heit.sort()    

for l in heit :
    print(l)