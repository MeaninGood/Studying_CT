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
    
    
''' 기존 코드 (투포인터 배우기 전)
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
    
'''


import sys

# 리스트로 입력 받아줌
arr = [int(sys.stdin.readline()) for heit in range(9)]
# arr = []
# for heit in range(9) :
#     arr.append(int(sys.stdin.readline()))
total = sum(arr) # 미리 합계 변수 지정
                # while문에 일일이 sum(arr)를 해주면 while을 도는 동안
                # sum을 계속 수행하므로, 애초에 변수로 지정해줌

arr.sort() # 정렬


s = 0 # s = 0에서 시작
e = 8 # e = 8에서 시작(리스트 인덱스 8까지니까)

while s < e : # s == e가 되면 종료
    # 7명의 합이 100이 되는 애들이 아니라, 100이 안 되는 2명을 찾자
    if arr[s] + arr[e] == total - 100 : # 탈출 조건 지정, total - 100해주면 됨
        for i in range(9) : # 위의 리스트를 돌면서
            if i == s or i == e : # i가 s 혹은 e와 같으면 출력 안 하고 continue
                continue
            print(arr[i]) # s와 e를 제외한 애들만 출력해줌
            
        break # 출력 다 했으면 멈춰줌 (안 그러면 무한히 출력함)
        
    elif arr[s] + arr[e] < total - 100 : # 합이 작으면
        s += 1 # s를 뒤로 보내줌, 오름차순이기 때문
    
    else :
        e -= 1 # 합이 더 크면 e를 앞으로 보내줌, 오름차순이기 때문