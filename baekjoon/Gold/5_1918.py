d = {'+':[1, 1], '-': [1, 1], '*':[2, 2], '/':[2, 2], '#':[-1, -1], '(': [0, 3]}

# 계산해주는 함수

def transform(p):
    ans = '' # 후위표기식으로 변환해 문자열 만들어줄 것
    stack = ['#'] # 에러 피하려고 앞에 잘 안 쓰는 문자 # 추가해줌
    for i in p:
        if i in d: # 연산자가 들어오면
            while d[stack[-1]][0] >= d[i][1]: # stack에 있는 연산자와 들어오는 연산자의 우선순위 비교
                # stack에 있는 연산자가 우선순위가 더 높으면
                ans += stack[-1] # ans에 stack에 있는 연산자 추가
                stack.pop()
            stack.append(i) # 아니면 stack에 추가
            
        elif i == ')': # 닫는 괄호가 들어오면 ~~ 여는 괄호까지 연산해야 함
            while len(stack) > 1: # stack이 비기 전까지 (나는 앞에 # 넣어줘서 길이 1이 됨)
                temp = stack.pop() # stack에 있는 연산자들을 다 빼주고
                if temp == '(': # 여는 괄호가 들어오면 그냥 버리기
                    break
                ans += temp # ans에 추가해줌
        
        else:
            ans += i # ans에 후위 표기식으로 만들어줌
            
    while len(stack) > 1 : # 이후 stack에 남아있는 연산자 다 ans에 추가
        ans += stack[-1]
        stack.pop()
    
    return ans

a = input()
print(transform(a))