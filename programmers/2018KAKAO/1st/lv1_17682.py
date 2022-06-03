dartResult = '1D2S#10S'
dartResult = dartResult.replace('10', 't')
    
d = {'S': 1, 'D': 2, 'T': 3}
stack = []

for i in dartResult: 
    if i in d:
        if i == 'S' or i == 'D' or i == 'T':
            tmp = stack.pop()
            tmp = tmp ** d[i]
            stack.append(tmp)
        
    elif i == '*':
        if len(stack) > 1:
            tmp1 = stack.pop()
            tmp1 *= 2
            tmp2 = stack.pop()
            tmp2 *= 2
            stack.append(tmp2)
            stack.append(tmp1)
        
        else:
            tmp = stack.pop()
            tmp *= 2
            stack.append(tmp)
                
    elif i == '#':
        tmp = stack.pop()
        tmp *= -1
        stack.append(tmp)
            
    else:
        if i == 't':
            stack.append(10)
        else:
            stack.append(int(i))

answer = sum(stack)
print(dartResult)
print(sum(stack))
            
            