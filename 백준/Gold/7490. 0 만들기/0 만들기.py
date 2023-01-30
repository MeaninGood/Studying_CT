import sys
input = lambda : sys.stdin.readline().strip()


calc = [
    lambda x, y: x + y,
    lambda x, y: x - y,
    lambda x, y: int(f'{x}{y}')
]


def check(x):
    x = x.replace(' ', '')
    return eval(x)
            
oper = [' ', '+', '-']
def recur(cur, tmp):
    global answers
    
    if cur == n:
        if check(tmp) == 0:
            answers.append(tmp)
        return
    
    for i in range(3):
        tmp += oper[i] + str(cur + 1)
        recur(cur + 1, tmp)
        tmp = tmp[:-2]
        

T = int(input())
for tc in range(T):
    n = int(input())
    
    answers = []
    recur(1, '1')

    print(*answers, sep='\n')
    print()

