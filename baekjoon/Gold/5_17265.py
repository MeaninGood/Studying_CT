# 17265번_나의 인생에는 수학과 함께

## 임의의 숫자와 연산자를 각 블록에 넣은 N x N 크기의 바둑판
## 오른쪽과 아래쪽으로만 이동
## 집(1, 1)에서 학교(N, N)까지 어떻게 연산이 되는지 확인
## 경로에서 만나는 연산자들의 우선순위는 고려하지 않음
## 최댓값과 최솟값을 구하기

'''
# 첫 번째 줄에는 지도의 크기 N이 주어진다. (3 ≤ N ≤ 5, N은 홀수) 
# 그 다음 N 줄에는 N개의 숫자 또는 연산자가 빈칸을 사이에 두고 주어짐
# 현이네 집 (1, 1)과 학교 (N, N)는 반드시 숫자
# 숫자 다음에는 연산자, 연산자 다음에는 숫자가 나오도록 주어진
# 주어지는 숫자는 0이상 5이하의 정수, 연산자는 (‘+’, ‘-’, ‘*’) 
## 연산 결과의 최댓값과 최솟값을 하나의 공백을 두고 출력
## 연산자 우선순위는 고려하지 않음


(입력)
5
5 + 5 - 3
* 3 - 1 -
4 + 5 + 2
- 2 * 3 -
1 * 5 + 2

(출력) 
127 3

'''
   
n = int(input())
arr = [list(input().split()) for _ in range(n)]

mx = -100000000000 # 아주 작은 값
mn = 100000000000 # 아주 큰 값

li = [] # 값 입력해줄 list
op = '+-*' # 연산자

def recur(x, y):
    global mx, mn
    if x == n or y == n :
        return # 아무것도 리턴하지 말기
    
    li.append(arr[x][y]) # li에 추가
    # x, y가 끝까지 도착했을 때! 여기서 계산
    if x == n - 1 and y == n - 1:
        ans = int(li[0]) # ans = li[0]
        for i in range(1, len(li), 2): # 연산자만 봄
            if li[i] == '+':
                ans += int(li[i + 1])
            elif li[i] == '-':
                ans -= int(li[i + 1])
            else:
                ans *= int(li[i + 1])
                
        mx = max(mx, ans) # for문 돌면서 계산 끝나면 mx, mn 구해주기
        mn = min(mn, ans)

        li.pop() # 리스트에 있는 것 빼주기, 마지막 숫자 빼는 것!
        
        return
    
    recur(x, y + 1) # 모든 경로 돌 때
    recur(x + 1, y) # 이렇게 쓰면 된다!
    
    li.pop() # 위에서 append 했으니 빼줘야 함, 재귀 쓴 이후에 넣기!
    
recur(0, 0)

print(f'{mx} {mn}')
