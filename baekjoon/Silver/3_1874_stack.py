# 1874번_스택 수열

## 1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음
## 스택에 push하는 순서는 반드시 오름차순
## 임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지
## 있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지 계산


'''
# 첫 줄에 n (1 ≤ n ≤ 100,000)
# 둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩
# 같은 정수가 두 번 나오는 일은 없다.
## 입력된 수열을 만들기 위해 필요한 연산을 한 줄에 한 개씩 출력
## push연산은 +로, pop 연산은 -로 표현
## 불가능한 경우 NO를 출력

(입력)
8
4
3
6
8
7
5
2
1

(출력)
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-

'''

# t = int(input())

# top = -1
# stack = [0] * t
# arr = []
# for i in range(t):
#     arr.append(int(input()))
    
# n = 0
# li = []
# for i in range(1, t+1):
#     if stack[top] == arr[n]:
#         top -= 1
#         stack[top + 1] = 0
#         li.append('-')
#         n += 1
#     else:
#         top += 1
#         stack[top] =  i
#         li.append('+')
   
# print(li)
   
        
# t = int(input())

# top = -1
# stack = [0] * t
# arr = []
# for _ in range(t):
#     arr.append(int(input()))

# n = 0
# i = 1
# while -2 < top < t:
#     if i == t + 1:
#         print('-')
#         top -= 1

#     elif stack[top] == arr[n]:
#         top -= 1
#         stack[top + 1] = 0
#         print('-')
#         n += 1
#     else:
#         top += 1
#         stack[top] = i
#         print('+')
#         i += 1




# t = int(input())

# top = -1
# stack = [0]
# arr = []
# for _ in range(t):
#     arr.append(int(input()))

# n = 0
# i = 1
# while stack:
#     if i == t + 1:
#         stack.pop()
#         print('-')

#     elif stack[-1] == arr[n]:
#         stack.pop()
#         print('-')
#         n += 1
#     else:
#         stack.append(i)
#         print('+')
#         i += 1


t = int(input())

top = -1
stack = [0]
arr = []
for _ in range(t):
    arr.append(int(input()))
    
result = []
n = 0
i = 1
while stack != []:
    if i == t + 1:
        if stack and n<t and stack[-1]==arr[n]:
            stack.pop()
            result.append('-')
            n +=1
        else:
            break

    elif stack[-1] == arr[n]:
        stack.pop()
        result.append('-')
        n += 1
    else:
        stack.append(i)
        result.append('+')
        i += 1
if stack[0]==0:
    stack.pop()
if stack:
    print('NO')
else:
    for r in result:
        print(r)