# 14453번_Hoof, Paper, Scissors

## 가위바위보를 하는데 하나만 계속해서 내다가 중간에 딱 한 번 다른 걸로 바꿈
## 물론 바꾸지 않아도 됨
## 그렇게 하나 or 두개만 냈을 때, 가장 많이 이기는 경우가 몇 번인지 출력

'''
# 첫째 줄에 가위바위보를 하는 횟수가 주어짐
# 둘째 줄부터 한 줄에 하나씩 H, P, S가 주어짐
## 최대 몇 번 이길 수 있는지 출력

(입력)
5
P
P
H
P
S

(출력)
4

'''
n = int(input())
arr = [0] + [input() for _ in range(n)]
prefix = [0 for _ in range(n + 1)]

cnt = {}

idxh = -1
idxs = -1
idxp = -1
for i in range(1, n + 1):
    cnt[arr[i]] = cnt.get(arr[i], 0) + 1
    prefix[i] = cnt[arr[i]]

idxh = -1
idxs = -1
idxp = -1
for i in range(1, n + 1):
    if arr[i] == 'H'
print(prefix)

'''
 
P P H P S P P H H H H H H S S
1 2 1 3 1 4 5 2 3 4 5 6 7 2 3

P 앞에 하나 있으니까 H는 1 빼주고
P 앞에 H 없으면 걍 둘이 더해주고 일케,,?
각 알파벳 max값 기준으로

'''