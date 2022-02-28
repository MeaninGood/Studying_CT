from re import A


d = {'+':[1, 1], '*':[2, 2], '#':[-1, -1], '(': [0, 3]}

# 계산해주는 함수
def get_calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '*':
        return a * b
    elif op == '/':
        return b / a
    elif op == '-':
        return a - b
    
def calc(ans):
    st = ['#'] # 맨 첫 인덱스 #으로 맞춰주기
    
    for i in ans:
        if i in d:
            a = st[-1]
            st.pop()
            b = st[-1]
            st.pop()
            st.append(get_calc(a, b, i))
            
        else:
            st.append(int(i))
    
    if len(st) == 2 : # 결과값이 항상 하나여야 함  
        return st[1]

n = int(input())
w = input()
a = ''
for i in range(n):
    n = int(input())
    
    
a = ''
for i in w:
    if i != '*+/-':
        

print(f'#{tc} {calc(p)}')
    