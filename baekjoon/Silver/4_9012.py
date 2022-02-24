def push_stack(n):
    return p[n] in "()"

# stack의 top과 쌍이 맞는지 확인
def check(top, n):
    return (stack[top] == '(' and p[n] == ')')


# stack에 뭐가 남아 있으면 0, 비었으면 1 반환
def is_True(top):
    if top > -1:
        return 'NO'
    return 'YES' # else

T = int(input())
for tc in range(1, T+1):
    p = input()

    top = -1
    size = len(p)
    stack = [0] * size
    # stack[top]과 p[i]가 쌍이 된다면
    for i in range(size):
        if check(top, i):
            top -= 1
            stack[top + 1] = 0 # 현재 top은 0으로
        # 쌍이 맞지 않고 새로운 괄호가 들어오면
        elif push_stack(i):
            top += 1
            stack[top] = p[i] # 현재 top 바꿔줌

    print(is_True(top))