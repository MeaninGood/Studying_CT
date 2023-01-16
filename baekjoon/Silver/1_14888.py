# import sys
# input = lambda : sys.stdin.readline().strip()

# calc = [
#     lambda x, y: x+y,
#     lambda x, y: x-y,
#     lambda x, y: x*y,
#     lambda x, y: x // y if x*y > 0 else -(abs(x)//y)
# ]

# def recur(cnt, total):
#     global mx, mn
#     if cnt == n-1:
#         # 최대 최소 갱신
#         mx = max(mx, total)
#         mn = min(mn, total)
#         return
    
#     # + - * /
#     for i in range(4):
#         # 사용할 수 있는 연산자가 없으면 continue
#         if not oper[i]:
#             continue
        
#         # 해당 연산자 사용한거 체크해주고
#         oper[i] -= 1
        
#         # total이 이전 연산 결과니까
#         # total arr[cnt+1] 해서 recur(cnt+1, x)
#         recur(cnt+1, calc[i](total, arr[cnt+1]))
        
#         # 다시 재귀 빠져나오면서 연산자 사용 체크한거 되돌려주기
#         oper[i] +=1

# n = int(input())
# mx = -10**11    # 최대값
# mn = 10**11     # 최소값
# arr = list(map(int, input().split()))
# oper = list(map(int, input().split()))

# recur(0, arr[0])    # 숫자 하나는 무조건 들어감

# print(mx)
# print(mn)


import sys
input = lambda : sys.stdin.readline().strip()


calc = [
    lambda x, y : x + y,
    lambda x, y : x - y,
    lambda x, y : x * y,
    lambda x, y : x // y if x * y > 0 else -(abs(x) // y)
]

mx = -10 ** 11
mn = 10 ** 11
def recur(cur, total):
    global mx, mn
    
    if cur == n - 1:
        mx = max(mx, total)
        mn = min(mn, total)
        return
    
    for i in range(4):
        if not arr2[i]:
            continue
        
        arr2[i] -= 1
        recur(cur + 1, calc[i](total, arr1[cur + 1]))
        
        arr2[i] += 1
        

n = int(input())
arr1 = list(map(int, input().split())) # 입력받는 배열
arr2 = list(map(int, input().split())) # 연산자 배열

recur(0, arr1[0])

print(mx)
print(mn)
