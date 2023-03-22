# 백트래킹

# 브루트포스 : 완전탐색
# 백트래킹 : 브루트포스를 재귀함수로 구현한다. 그리고 가지치기를 한다.
# 재귀함수 : 함수 내에서 자기 자신을 또 호출하는 경우


# 우리의 목표 : n자리 m진수를 출력하는 것

"""
7자리 4진수 출력하기
0-based

000
001
002
010
011
012
...
222

0000
0001
0002
...
3333333
"""



## 3가지 방법으로 풀 예정
            
# 첫 번째 템플릿 - 중복까지 허용하는 순열
# n자리 m진수를 모두 출력하는 문제
"""
000
001
...
222
"""
n, m = map(int, input().split())
# cur : int, tmp : String

# n = 3, m = 4
def recur(cur, tmp):                # 0
    if cur == n:                    # 1 != 3 (x)
        print(tmp)
        return
    
    # 0 -> 1 -> 2
    for i in range(m):              # m = 3 for i in range(3): recur(cur + 1, tmp + "0") recur(cur + 1, tmp + "1") recur(cur + 1, tmp + "2")
        print("현재노드: ", cur, "다음 노드: ", cur + 1, "현재 문자열: " , tmp, "넘겨줄 문자열:", tmp + str(i))
        recur(cur + 1, tmp + str(i))    # recur(1, "0") # recur(2, "00")
        
recur(0, "")

# recur(0, "")
#     recur(1, "0")
#         recur(2, "00")

# n, m = 3, 4
for i in range(m):
    for j in range(m):
        for k in range(m):
            print(f"{i}{j}{k}")

def recur(cur, tmp): 
    if cur == n:  
        print(tmp)
        return

    for i in range(m):
        recur(cur + 1, tmp + str(i))    # recur(1, "0") # recur(2, "00")
        
recur(0, "")



## 두번째 템플릿 - 중복을 제거한 순열 n자리 m진수 출력
# 000, 001, 002 이런 애들 출력 안 할 거기 때문에 안 볼 거거든
# 012, 013, 014, 021, 023, 024 .. 이런 애들만 출력

n, m = map(int, input().split())

# [F, F, F]
visited = [False for i in range(m)] # global 변수

def recur(cur, tmp):
    if cur == n:
        print(tmp)
        return
    
    for i in range(m):
        if visited[i]: # visited[i] == True
            continue
        
        visited[i] = True
        print("현재노드: ", cur, "다음 노드: ", cur + 1, "현재 문자열: " , tmp, "넘겨줄 문자열:", tmp + str(i))
        recur(cur + 1, tmp + str(i))
        visited[i] = False
        
recur(0, "")


n, m = 3, 4
visited = [False for _ in range(m)]
for i in range(m):
    if visited[i]:
        continue

    visited[i] = True
    for j in range(m):
        if visited[j]:
            continue

        visited[j] = True
        for k in range(m):
            if visited[k]:
                continue
            
            visited[k] = True
            print(f"{i}{j}{k}")
            visited[k] = False

        visited[j] = False

    visited[i] = False
    

#세번째 템플릿 - 중복된 케이스를 아예 안 본다 : 조합
"""
012
...
021 -> 결국 같은 숫자 3개니까 안 보겠다
012
120
210


4 5
0123
0124
0134
0234
1234

"""

n, m = map(int, input().split())

def recur(cur, start, tmp):
    if cur == n:
        print(tmp)
        return
    
    for i in range(start, m):
        recur(cur + 1, i + 1, tmp + str(i))
        
recur(0, 0, "")




n, m = 3, 5
for i in range(0, m): # 1 2 3 4
    for j in range(i + 1, m): # 2 3 4
        for k in range(i + j + 1, m): # 3 4
            print(f"{i}{j}{k}")
            
            
## 우리가 문제에 맞춰서 풀기 어려운 백트래킹 문제들
## 문제를 우리가 외운 템플릿으로 변형시켜서 풀 수 있다

# n = input()
# arr = input().split()
n, m = 2, 3
visited = [False for i in range(m)]
def recur(cur, tmp):
    if cur == n:
        return
    
    for i in range(m):
        if visited[i]:
            continue
        
        visited[i] = True
        recur(cur + 1, tmp + str(i))
        visited[i] = False
        
        
n = int(input())
arr = input().split()

visited = [False for i in range(10)]
def recur(cur, tmp):
    if cur == n + 1:
        # 부등호를 만족만 한다면
        # 가장 먼저 딸려 나오는 애가
        # 가장 작은 숫자다
        for i in range(n):
            if arr[i] == "<" and tmp[i] > tmp[i + 1]:
                return
            
            if arr[i] == '>' and tmp[i] < tmp[i + 1]:
                return
        
        print(tmp)
        return
    
    for i in range(10):
        if visited[i]:
            continue
        
        visited[i] = True
        recur(cur + 1, tmp + str(i))
        visited[i] = False
  
recur(0, "")
        
# n, m = 3, 5
# visited = [False for i in range(m)]
# def recur(cur, tmp):
#     if cur == n:
#         print(tmp)
#         # 부등호를 만족만 한다면
#         # 가장 먼저 딸려 나오는 애가
#         # 가장 큰 숫자
#         return
    
#     for i in range(m)[::-1]:
#         if visited[i]:
#             continue
        
#         visited[i] = True
#         recur(cur + 1, tmp + str(i))
#         visited[i] = False
        

