# 조합 식: n! / (r! ( n - r)!)

import sys
input = lambda: sys.stdin.readline().strip()

a, b = map(int,input().split())

def get_nums(x, y):
    ret = 0
    while x != 0:
        ret += x // y
        x //= y
    
    return ret

a2, ab2, b2 = get_nums(a, 2), get_nums(a - b, 2), get_nums(b, 2)
a5, ab5, b5 = get_nums(a, 5), get_nums(a - b, 5), get_nums(b, 5)

if a2 - ab2 - b2 <= 0 or a5 - ab5 - b5 <= 0:
    print(0)
else:
    print(min(a2 - ab2 - b2, a5 - ab5 - b5))