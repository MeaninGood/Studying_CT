a, b = map(int, input().split())

x = int((-2*a + ((2*a)**2 - 4*b)**0.5) / 2)
y = int((-2*a - ((2*a)**2 - 4*b)**0.5) / 2)

if x == y :
    print(x)
else:
    print(y, x)
# 어차피 x보다 y가 더 작을 거기 때문에(당연히 뺀 게 더 작음)
## print(x, y)는 써줄 이유가 없음.