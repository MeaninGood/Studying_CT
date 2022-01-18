# 1864번_문어 숫자

## 기호를 숫자에 대응시킴
## 8진법에 기반함
## 기호를 입력 받아 십진수로 출력

'''
# 한 줄에 하나씩 기호 입력됨. 입력으로 #이 들어오기까지 계속 반복
## 대응하는 십진수를 한 줄에 하나씩 출력

(입력) (@&
(출력) 158

'''

# dic_oct = {
#     '-' : 0,
#     '\\' : 1,
#     '(' : 2,
#     '@' : 3,
#     '?' : 4,
#     '>' : 5,
#     '&' : 6,
#     '%' : 7,
#     '/' : -1
# }

sign = "-\(@?>&%"

d = {}

for i in range(8):
   d[sign[i]] = i
   
d['/'] = -1


while 1 :
    num = input()
    if num == '#' :
        break

    n = len(num)    
    ans = 0

    for i in range(n) :
        ans &= oct(d[num[i]])
    
    print(int(ans, 8))

ans = 0
mul = 1
for i in range(len(str))[::-1]:
   ans += arr[str[i]] * mul
   mul *= 8

