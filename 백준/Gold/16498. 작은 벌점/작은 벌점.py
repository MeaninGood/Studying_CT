import sys

input = lambda: sys.stdin.readline().strip()

a, b, c = map(int, input().split())

aarr = map(int, input().split())
barr = sorted(map(int, input().split()))
carr = sorted(map(int, input().split()))

def check(num, target, nearest):
    return abs(num - target) < abs(nearest - target)

def bin_search(target, arr):
    s, e = 0, len(arr) - 1
    tmp = arr[(s + e) // 2]

    while s <= e:
        mid = (s + e) // 2
        
        if check(arr[mid], target, tmp):
            tmp = arr[mid]
            
        if arr[mid] == target:
            return target
        
        if arr[mid] < target:
            s = mid + 1
            
        elif arr[mid] > target:
            e = mid - 1
            
    return tmp


ans = 1 << 31
for anum in aarr:
    num1 = bin_search(anum, barr)
    num2 = bin_search(anum, carr)
    num3 = bin_search(num1, carr)
    
    ans = min(ans, abs(max(anum, max(num1, num2)) - min(anum, min(num1, num2))))
    ans = min(ans, abs(max(anum, max(num1, num3)) - min(anum, min(num1, num3))))
    

print(ans)