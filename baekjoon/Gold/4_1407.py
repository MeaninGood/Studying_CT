import sys
input = lambda: sys.stdin.readline().strip()

a, b = map(int, input().split(' '))

def calc(x):
    ret = x
    i = 2
    while x >= i:
        ret += (x // i) * (i // 2)
        i *= 2
    return ret

print(calc(b) - calc(a - 1))