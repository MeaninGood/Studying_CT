# 9935번_문자열 폭발

## 폭발 문자열이 폭발하면 그 문자는 문자열에서 사라지며
## 남은 문자열은 합쳐지게 됨
## 새로 생긴 문자열에 폭발 문자열이 포함되어 있을 수도 있다.
## 폭발은 폭발 문자열이 문자열에 없을 때까지 계속된다.
## 아있는 문자가 없을 때는 "FRULA" 출력

'''
# 첫째 줄에 문자열이 주어진다. 문자열의 길이는 1보다 크거나 같고, 1,000,000보다 작거나 같다
# 둘째 줄에 폭발 문자열이 주어진다. 길이는 1보다 크거나 같고, 36보다 작거나 같다.
# 두 문자열은 모두 알파벳 소문자와 대문자, 숫자 0, 1, ..., 9로만 이루어져 있다.
## 첫째 줄에 모든 폭발이 끝난 후 남은 문자열을 출력

(입력)
mirkovC4nizCC44
C4

(출력)
mirkovniz

'''
import sys
si = sys.stdin.readline

arr = si().rstrip()
erase = list(si().rstrip())
d = len(erase)


def bomb(arr):
    stack = []
    for i in arr:
        stack.append(i)
        
        if stack[-d:] == erase:
            for j in range(d):
                stack.pop()
                
    if len(stack) > 0:            
        return print(''.join(stack))
    
               
    return print('FRULA')
                
        
# arr = [1, 2, 3, 4, 5]
bomb(arr)

# ans = ''
# for i in ret:
#     ans += i
# print(ans)
# # print(ret)