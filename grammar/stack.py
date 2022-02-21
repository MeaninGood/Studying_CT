top = -1
size = 3
stack = [0] * size

top += 1
stack[top] = 10

top += 1
stack[top] = 20

top += 1
stack[top] = 30

for i in range(size):
    if top > -1:
        print(stack[top])
        top -= 1