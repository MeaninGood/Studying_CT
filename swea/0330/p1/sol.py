'''
퀵소트

lesser_arr, equal_arr, greater_arr 개념

쪼개기, 비교하기, 담기

'''

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

for tc in range(T):
    arr = list(map(int, input().split()))
    
    print(*qsort(arr))