# 11866번_요세푸스 문제 0

## 1번부터 N번까지 원을 이루고 앉아있는 사람을 K만큼 순서대로 제거
## N명의 사람이 모두 제거될 때까지 계속함
## 원에서 사람들이 제거되는 순서 출력


'''
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어짐
## 예제와 같은 요세푸스 순열 출력

(입력)
7 3

(출력)
<3, 6, 2, 7, 5, 1, 4>

'''

# import sys

# a, b = map(int, sys.stdin.readline().split()) 


# arr = [i for i in range(1, a+1)] # a에 맞춰 1번부터 사람 채워주기


# cnt = [] # 제거한 사람만 뽑아 올 리스트
# while arr != [] : # arr를 계속 줄여줄 것이기 때문에 빈 리스트가 되면 break
#     for j in range(b-1) : # 3명이면 앞에 2명을 뒤로 옮기고, 3번째를 뽑아줄 것
#         temp = arr.pop(0) # 맨 앞자리의 사람을 뽑아서
#         arr.append(temp) # 맨 뒤로 옮겨줌
        
#     # b-1만큼 반복 후에 맨 앞에 있는 사람은 cnt에 넣어줌(제거 당한 사람)
#     cnt.append(arr.pop(0))
# #     print(arr)
# #     print(cnt)
# # print(cnt)
# cnt = list(map(str, cnt)) # 조인 함수를 쓸 것이기 때문에 map과 str로 문자열로 변환
# print(f'<{", ".join(cnt)}>') # 조인 함수로 출력해 줌


''' 고민의 흔적들
# while 1 :
#     for i in range(b-1) :
#         arr.append(arr.pop(0))
       
#     else :
#         temp = arr.pop(b-1)
#         cnt.append(temp)


# n,k = map(int,input().split())
# q = [i for i in range(1,n+1)]
# r = []


        
    
#     if arr == [] :
#         break
    
# print(cnt) # 3 출력됨

'''



''' 다른 코드 1
import sys

N, K = map(int, sys.stdin.readline().split())
K += -1
list = [i for i in range(1, N+1)]
result = []
size = N
ptr = K

for i in range(0,N):
    result.append(str(list[ptr]))
    list.pop(ptr)
    if size > 1:
        size -= 1
    ptr = (ptr+K)%size
print(f'<{", ".join(result)}>')


'''



'''pop 안 쓰고 푼 코드

N , K = map(int,input().split())

arr = [ k for k in range(1,N+1)]
idx = 0
result = []
while True:
    if len(result) == N:
        break
    i = 0
    cnt = 0
    while i < K:
        if arr[(idx+cnt)%N] !=0:
            i+=1
        cnt +=1
    idx += cnt-1
    result.append(str(arr[(idx)%N]))
    arr[(idx)%N] =0
print(f'<{", ".join(result)}>')


'''




# 골드 1 제출 버전

import sys

a, b = map(int, sys.stdin.readline().split()) 

arr = [ i for i in range(1, a+1)]

cnt = 0 
while arr != [] : 
    for j in range(b-1) : 
        arr.append(arr.pop(0))
  
    cnt = arr.pop(0)

print(cnt)



# arr = 'abcd'





# arr = [map(str, i for i in range(10))]

# # b= 3
# # for j in range(b-1) :
# #     arr = arr[1:] + arr[0]
# arr = arr[1:] + arr[0]

# print(arr)





# N , K = map(int,input().split())

# arr = [ k for k in range(1,N+1)]
# idx = 0
# result = []
# while True:
#     if len(result) == N:
#         break
#     i = 0
#     cnt = 0
#     while i < K:
#         if arr[(idx+cnt)%N] !=0:
#             i+=1
#         cnt +=1
#     idx += cnt-1
#     result.append(str(arr[(idx)%N]))
#     arr[(idx)%N] =0
# print(f'<{", ".join(result)}>')




# import sys

# a, b = map(int, sys.stdin.readline().split()) 

# arr = range(1, a+1)

# idx = 0

# while range(b) :
#     i = 0
#     cnt = 0 
#     if arr[(idx+cnt)%N] !=0:
#         i+=1
#     cnt +=1
#     idx += cnt-1