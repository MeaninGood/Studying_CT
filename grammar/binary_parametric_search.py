# 이진 탐색 (binary search)
# logn의 시간복잡도 - 한 번에 절반씩 날리니까 : 거의 상수



# arr = [1, 2, 6, 10, 11, 15, 20, 25]

# # 8이 배열에 있냐

# x = 8

# s = 0
# e = len(arr) -1
# while s <= e:
#     mid = (s + e) // 2
    
#     if arr[mid] == x:
#         print('찾았다')
#         break
    
#     elif arr[mid] < x:
#         s = mid + 1
        
#     else :
#         e = mid - 1
        

# 매개변수 탐색 (parametric search)
# 최대값을 최소화, 최소값을 최대화

arr = list(map(int, input().split()))

# 2중에서 제일 뒤에 있는 게 몇 번 인덱스?
# 2중에 제일 앞에 있는 게 몇 번 인덱스?

s  = 0
e = len(arr) - 1
idx = 0

# 제일 뒤에 거 찾기
while s <= e:
    mid = (s + e) // 2
    
    if arr[mid] <= 2:
        s = mid + 1 # 반 날리기
        idx = mid ## 저장해놓고
    
    else :
        e = mid -1
    
print(idx)

# 제일 앞에 거 찾기
while s <= e:
    mid = (s + e) // 2
    
    if arr[mid] >= 2:
        s = mid + 1 # 반 날리기
        idx = mid ## 저장해놓고
    
    else :
        e = mid -1
    
print(idx)
