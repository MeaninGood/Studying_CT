def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    
def order(cur): #후위표기식
    if 0 < cur <= v:
        order(l[cur])
        order((r[cur]))
        li.append(tree[cur])
        
for tc in range(1, 3):
    v = int(input())
    l = [0] * (v + 1)
    r = [0] * (v + 1)
    tree = [0] * (v + 1)
    li = []
    
    for _ in range(v):
        temp = input().split()
        if len(temp) == 4:
            l[int(temp[0])] = int(temp[2])
            r[int(temp[0])] = int(temp[3])
            tree[int(temp[0])] = temp[1]
        else:
            tree[int(temp[0])] = int(temp[1])
            
    order(1)
    print(li)
    
    stack = []
    for i in li:
        if type(i) != int:
            b = stack.pop()
            a = stack.pop()
            c = calc(a, b, i)
            stack.append(c)
            
        else:
            stack.append(i)
            
    ans = int(stack.pop())
    print(f'#{tc} {ans}')