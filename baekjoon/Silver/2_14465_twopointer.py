# 14465번_소가 길을 건너간 이유 5

## 1번부터 N번까지의 번호가 붙은 횡단보도 N (1 ≤ N ≤ 100,000)개
## 존은 연속한 K개의 신호등이 존재하도록 신호등을 수리

'''
# 첫 줄에 N, K, B (1 ≤ B,K ≤ N)
# 그 다음 B줄에는 고장난 신호등의 번호가 하나씩 주어짐
## 정상적으로 작동하는 연속 K개의 신호등이 존재하려면 최소 몇 개의 신호등을 수리해야 하는지 출력

(입력)
10 6 5
2
10
1
5
9

(출력)
1

'''

# import sys

# n, k, b = map(int, sys.stdin.readline().split())

# li = [int(sys.stdin.readline()) for _ in range(b)]

# arr = [k for k in range(1,n+1)]

# li.sort()

# s = 0
# e = k - 1
# cnt = 0
# while e < n :
    

# import sys
# n, k, b = map(int, sys.stdin.readline().split())

# li = [int(sys.stdin.readline()) for _ in range(b)]

# arr = [False] * (n+1)

# for i in li :
#     arr[i] = True
    
# # print(arr)

# s = 0
# e = k
# cnt = arr[s:e].count(True)

# # print(arr[s:e])

# while e < n+1 :     
#     s += 1
#     e += 1
#     if arr[s:e].count(True) < cnt :
#         cnt = arr[s:e].count(True)

    
# print(cnt)



import sys
n, k, b = map(int, sys.stdin.readline().split())

arr = [False] * (n+1)

for i in range(b) :
    x = int(sys.stdin.readline())
    arr[x-1] = True
    
s = 0
e = 0
cnt = 0
total = 0
while e < n :
    if e < k :
        if arr[e] == True :
            cnt += 1
            total += 1
        e += 1

    elif e > k :
        s += 1
        e += 1
        if arr[s] == True :
            total -= 1
        
        elif arr[e] == True :
            total += 1
    
    elif cnt > total :
        cnt = total

print(cnt)
            
       
    