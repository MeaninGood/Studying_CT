# 1. n자리 m진수 출력
'''
000
001
002
003
004
010
011
...
444

'''
n = 3
m = 5

arr = [ 0 for i in range(n) ]

def recur(cur):
    if cur == n:
        print(*arr)
        return
        
    for i in range(m):
        arr[cur] = i
        recur(cur + 1)
        
recur(0)



# 2. 한 케이스 내에서 중복된 값이 없는 순열
# 숫자 두 개가 똑같으면 안 볼 거임! 중복 제거
'''
012
013
014
021
023
024
...
'''


# n = 3
# m = 5

# visited = [ False for i in range(m) ]
# arr= [ 0 for i in range(n) ]

# def recur(cur):
#     if cur == n:
#         print(*arr)
#         return
    
#     for i in range(m):
#         if visited[i]:
#             continue
        
#         arr[cur] = i
#         visited[i] = True
#         recur( cur + 1 )
#         visited[i] = False


# 3. 중복된 케이스 다 안 본다
'''
5, 6, 7, 8, 9나 6, 5, 8, 7, 9나 같은 거니까 하나만 보겠다

012 # 얘만 보고
021 같은 거니까 안 봄
102 안 봄
120 안 봄

'''

# n = 3
# m = 5

# arr = [0 for i in range(110)]

# def recur(cur, start):
#     if cur == n :
#         print(*arr)
#         return

#     for i in range(start, m):
#         arr[cur] = i
#         recur(cur + 1, i + 1)
        
# recur(0, 0)


# 4. 순서가 바뀐 것을 같은 case로 보지 않음
'''
0 1 2 3 4 5
0 1 2 3 5 4
0 1 2 4 5 3
...
5 4 3 2 1 0 다 보겠다
근데 순서만 바꿔서 보겠다,, 2번 템플릿임!
'''

## 10819 차이를 최대로
# n = int(input())
# arr = list(map(int, input().split()))
# arr2 = [ 0 for i in range(n)]
# visited = [ False for i in range(n)]


# def recur(cur):
#     if cur == n:
#         total = 0
#         for i in range(1, n):
#             total += abs(arr[arr2[i]] - arr[arr2[i-1]])
            
#         return total
    
#     total = 0 
#     for i in range(n):
#         if visited[i]:
#             continue
        
#         arr2[cur] = i
#         visited[i] = True
#         total = max(total, recur( cur + 1 ))
#         visited[i] = False
        
#     return total


# print(recur(0))