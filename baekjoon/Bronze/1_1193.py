# 1193번_분수찾기

## 1/1 1/2 1/3 1/4 1/5 ...
## 2/1 2/2 2/3 2/4 ...
## 3/1 3/2 3/3 ...
## 4/1 4/2 ...
## 1/1 -> 1/2 -> 2/1 -> 3/1 -> 2/2와같이 지그재그로 1번,2번,3번,4번,5번... 분수
## X가 주어졌을 때, X번째 분수 구하기

X = int(input())
 
#line1 = [1,1], line2 = [1/2,2/1], line3 = [3/1, 2/2, 1/3], line4 = [1/4, 2/3, 3/2, 4/1]
line = 1 #line1(1,1은 첫번째 줄)이 디폴트
while X > line : #X가 몇 번째 줄의 몇 번째에 있는 분수인지 찾기
    X = X - line #X에서 라인 빼기 - 몇 번째에 있는 분수인지
    line += 1 #라인 한 줄 씩 추가 - X가 몇 번째 줄인지

for i in range(X) :
    if line % 2 == 0 : #짝수 라인은
        nume = X #[분자] 위의 식에서 몇 번째에 있는 숫자인지
        deno = line - (X-1) #[분모] 1번째 줄 1개, 2번째 줄 2개,,, 맨 끝 숫자에서 X-1만큼 빼주기
        ##예를 들어 7번째 분수 = 넷째 줄의 첫 번째 분수. 위 식에서 X = 1, line = 4이므로
        ##line - (X-1)은 4번째 줄에서 첫 번째 숫자 : (4) - (1-1) = (4) - 0 = 첫 번째
    else :
        nume = line - (X-1) #홀수라인은 반대로 해주기
        deno = X
    
print(nume, '/', deno, sep='') #다 붙여서 출력하기