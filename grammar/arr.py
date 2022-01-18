# 배열화하여 직관성 높이기

## While
# if x = 1 :
#     print('aaa')
# elif x = 2 :
#     print('bbb')
# elif x = 3 :
#     print('ccc')
    
# arr = [0, 'aaa', 'bbb', 'ccc']
# print(arr[x])




change = [500, 100, 50, 10, 5, 1]

n = int(input())

tmp = 1000 - n

cnt = 0

for i in change :
    cnt += tmp // i
    tmp = tmp % i
    
print(cnt)
    