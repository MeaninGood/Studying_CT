arr = [1, 2, 3, 4, 5, 6]
num = []
for i in range(3) :
    for j in arr[i + 1:] :
        num.append((arr[i], j))
print(num)


'''(출력)
[(1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 3), 
(2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

'''


'''
arr = [1, 2, 3, 4, 5, 6]

def div_li(l, n) :
    for i in range(0, len(l), n) :
        yield l[i:i+n]
        

n = 2

result = list(div_li(arr, n))
print(result)



(출력)
[[1, 2], [3, 4], [5, 6]]

'''




'''
arr = [1, 2, 3, 4, 5, 6]
n = 2
div_li = []
for i in range(0, len(arr), n) :
    div_li.append(arr[i:i+n])
print(div_li)



(출력)
[[1, 2], [3, 4], [5, 6]]

'''