'''
1. () -> x로 바꾸기
2. (x) -> x로 바꾸기, 카운트 1 + 1 
3. (xx) => xx 로 바꾸기 2 + 1
저거 점점 늘려가면서 x 개수 + 1 해줘야 함

'''

# def arr_replace(args):
#     return args.replace('()', 'x')

# def 

# T = int(input())
# for t in range(1, T+1):
#     arr = input()
    
p = '()(((()())(())()))(())'
a = '('
b = ')'
c = 'x'
cnt = 0

while 1:
    p = p.replace(a + b, c)
    a = '('
    a += c

    c += 'x'

    if '(' not in p:
        break
    
    print(cnt)

    
