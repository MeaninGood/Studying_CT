n = int(input())

total = 0
idx = 0
x = 1
while total <= n:
    total += x
    idx = x - 1
    x += 1
    
print(idx)