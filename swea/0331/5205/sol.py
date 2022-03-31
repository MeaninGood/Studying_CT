# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# def quick_sort(array):
#     # 리스트가 하나 이하의 원소만을 담고 있다면 종료
#     if len(array) <= 1:
#         return array

#     pivot = array[0] # 피벗은 첫 번째 원소
#     tail = array[1:] # 피벗을 제외한 리스트

#     left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
#     right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# print(quick_sort(array))


# def qsort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     s = arr[0]
#     e = arr[1:]
    
#     larr = [i for i in e if i <= s]
#     rarr = [i for i in e if i > s]
    
#     return qsort(larr) + [s] + qsort(rarr)

def qsort(arr):
    if len(arr) <= 1:
        return arr
    
    pv = arr[len(arr) // 2]
    larr, earr, garr = [], [], []
    
    for num in arr:
        if num < pv:
            larr.append(num)
        
        elif num > pv:
            garr.append(num)
        
        else:
            earr.append(num)
    
    return qsort(larr) + earr + qsort(garr)

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    
    print(f'#{tc} {qsort(arr)[n // 2]}')