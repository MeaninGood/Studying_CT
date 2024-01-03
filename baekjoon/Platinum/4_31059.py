'''

1	2	3	4	10

1에 모으는 경우
1,1 = 1(1-1) + 1(2-1) + 1(3-1) + 1(4-1) + 1(10-1) = 0 + 1 + 2 + 3 + 9 = 15      0 / 15


2에 모으는 경우
1,1 : 1(1-2) + 1(2-2) + 1(3-2) + 1(4-2) + 1(10-2) = 1 + 0 + 1 + 2 + 8 = 12     2 <- 1 / 11 -> 22
1,2 : 1(1-2) + 1(2-2) + 2(3-2) + 2(4-2) + 2(10-2) = 1 + 0 + 2 + 2 + 16 = 13              V (1,2)
2,1 : 1(1-2) + 1(2-2) + 2(3-2) + 2(4-2) + 2(10-2) = 1 + 0 + 2 + 4 + 16 = 23

3에 모으는 경우
1,1: 1(1-3) + 1(2-3) + 1(3-3) + 1(4-3) + 1(10-3) = 2 + 1 + 0 + 1 + 7 = 11               V (1,1)     3 / 8
1,2: 2(3-1) + 2(3-2) + 2(3-3) + 1(4-3) + 1(10-3) = 4 + 2 + 0 + 1 + 7 = 14


4에 모으는 경우
1,1: 1(1-4) + 1(2-4) + 1(3-4) + 1(4-4) + 1(10-4) = 3 + 2 + 1 + 0 + 6 = 12           6 / 6
1,2: 1(1-4) + 1(2-4) + 1(3-4) + 2(4-4) + 2(10-4) = 3 + 2 + 1 + 0 + 12 = 18
1,4: 1(1-4) + 1(2-4) + 1(3-4) + 4(4-4) + 4(10-4) = 3 + 2 + 1 + 0 + 24 = 30

10에 모으는 경우
1,1: 1(1-10) + 1(2-10) + 1(3-10) + 1(4-10) + 1(10-10) = 9 + 8 + 7 + 6 + 0 = 30      30 / 0
1,2 : 1(1-10) + 1(2-10) + 1(3-10) + 1(4-10) + 2(10-10) = 9 + 8 + 7 + 6 + 0 = 30


가중치가 없었다면(1,1) 가운데가 무조건 최선임.
가중치가 생겼기 때문에 가운데가 아닌 다른 점들이 가능


1, 2, 3, 4, 10      가중치가 2,4라면? -> 오른쪽이 크면 오른쪽으로 당기고, 왼쪽이 크면 왼쪽으로 당김, 같으면 가운데

1에 모으는 경우
4(1-1) + 2(2-1) + 2(3-1) + 2(4-1) + 2(10-1) = 0 + 2 + 4 + 6 + 18 = 30

2에 모으는 경우
4(1-2) + 4(2-2) + 2(3-2) + 2(4-2) + 2(10-2) = 4 + 0 + 2 + 4 + 6 = 16

3에 모으는 경우
4(1-3) + 4(2-3) + 4(3-3) + 2(4-3) + 2(10-3) = 8 + 4 + 0 + 2 + 14 = 18

4에 모으는 경우
4(1-4) + 4(2-4) + 4(3-4) + 4(4-4) + 2(10-4) = 12 + 8 + 4 + 0 + 12 = 36

10에 모으는 경우
4(1-10) + 4(2-10) + 4(3-10) + 4(4-10) + 4(10-10) = 36 + 32 + ...

쿼리 20만 개 들어옴
20만 개를 다 3번씩 해보면 ..?


'''

# print(10 ** 6) # 100만 N
# print(2 * (10 ** 5)) # 20만 Q
# print(100000 * 200000) # 이건 안 됨

import sys
input = lambda : sys.stdin.readline().strip()

n = int(input())
n_arr = sorted(map(int, input().split(' ')))
q = int(input())
q_arr = [list(map(int, input().split(' '))) for _ in range(q)]

print(n, n_arr, q, q_arr)

# n이 짝수면 2개만 보기 ?? - 검증x
a, b, c = 0, 0, 0
if not (n % 2):
    a, b, c = (n // 2), (n // 2), (n // 2) + 1 # 홀수와 개수 맞추기 위해 a = b 동일하게 둠
    
# n이 홀수면 3개 보기 - 검증   
else:
    a = (n // 2) - 1
    b = n // 2
    c = (n // 2) + 1
    
    
prefix, suffix = 0, 0 
for i in range(n):
    if i < n // 2:
        prefix += abs(n_arr[i] - n_arr[b])
        
    elif i > n // 2:
        suffix += abs(n_arr[i] - n_arr[b])
        
print(prefix, suffix)
        

ans = []
for x, y in q_arr:
    if x == y:
        ans.append(prefix * x + suffix * y)

    elif x > y: # 왼쪽이 크면 왼쪽으로 당김
        # 짝수일 떄, 홀수일 떄
        npre, nsuf = prefix, suffix
        if (n % 2):
            npre -= n_arr[a]
            nsuf += n_arr[b]
        
        ans.append(npre * x + nsuf * y)
    
    elif x < y: # 오른쪽이 크면 오른쪽으로 당김
        # 짝수일 때, 홀수일 때
        npre, nsuf = prefix, suffix
        if (n % 2):
            npre += n_arr[b]
            nsuf -= n_arr[c]
            
        print('오른쪽이 클 때:', x, y, 'npre, narr[b]', npre, abs(n_arr[a] - n_arr[b]), npre * x, ':', nsuf, n_arr[c], nsuf * y)
        ans.append(npre * x + nsuf * y)
        
print(ans)
import sys

input = lambda: sys.stdin.readline().strip()


def getSum(mid, x, y):
    return prefix[mid] * x + suffix[mid] * y


def getResult(x, y):
    s, e = 0, 1000010
    res = 1 << 62

    while e >= s:
        mid = (s + e) // 2

        res = min(res, getSum(mid, x, y))

        if getSum(mid, x, y) > getSum(mid + 1, x, y):
            s = mid + 1

        else:
            e = mid - 1

    return res


n = int(input())
arr = sorted(list(map(int, input().split(" "))))

prefix, suffix = [0 for _ in range(1000010)], [0 for _ in range(1000010)]

cnt = 0
for i in range(1000010):
    if i > 0:
        prefix[i] = prefix[i - 1] + cnt

    while cnt < n and arr[cnt] == i:
        cnt += 1

cnt = n - 1
for i in range(1000009)[::-1]:
    suffix[i] = suffix[i + 1] + n - 1 - cnt

    while cnt >= 0 and arr[cnt] == i:
        cnt -= 1

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())

    print(getResult(x, y))
