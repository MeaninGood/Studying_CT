# 1026번_보물

## 길이가 N인 정수 배열 A와 B
## 함수 S = A[0] × B[0] + ... + A[N-1] × B[N-1]
## S의 값을 가장 작게 만들기 위해 A의 수를 재배열
## 단, B에 있는 수는 재배열하면 안 된다.
## S의 최솟값을 출력하는 프로그램을 작성

'''
# 첫째 줄에 N이 주어짐
# 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어짐
# N은 50보다 작거나 같은 자연수
# A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수
## 첫째 줄에 S의 최솟값을 출력

(입력)
5
1 1 1 6 0
2 7 8 3 1

(출력)
18

'''

n = int(input())
a = list(map(int, input().split()))
a.sort()

b = list(map(int, input().split()))
tmp = sorted(b, reverse=True)

# print(b)
v = [-1 for _ in range(n)]
while -1 in v:
    if tmp == []:
        break
    
    mx = max(tmp)
    for i in range(n):
        if b[i] == mx and v[i] != -1:
            continue
        
        elif b[i] == mx and v[i] == -1:
            v[i] = a.pop(0)
            tmp.pop(0)
            break
        # print(mx)
    # idx = b.index(mx)
    # v[idx] = a.pop(0)
    # tmp.pop(0)
    
ans = 0
for i in range(n):
    ans += v[i] * b[i]

print(ans)
    