# 값 여러 개 return

def ABC(a, b) :
    return a + b, a - b

# x, y = ABC(10, 20) ==> x = 30, y = -10으로 출력됨
#print(y) ==> return 값 여러 개 반환하면 튜플 반환

x = ABC(10, 20)
print(x) # ==> (30, -10)으로 출력