# B
def f(x):
    return x // a + x % a


t = int(input())

for _ in range(t):
    l, r, a = map(int, input().split())
    
    print(max(f(max(l, a * (r // a - 1) + a - 1)), f(r))))
    
    
    
'''
6 20 6

6 7 8 9 10 11               1
1 2 3 4  5  6

12 13 14 15 16 17           2
2  3  4  5  6  7

18 19 20                    3
3  4  5


'''

# C

'''
(0, 10, 1) # 번호까지 붙여서 저장하기
(-2, 1, 2)
(4, 10, 3)
(11, 20, 4)
(7, -1, 5)


정렬
(7, -1, 5)  (-2, 1, 2)  (0, 10, 1)  (4, 10, 3)  (11, 20, 4)

x 값 기준으로 정렬
(-2, 1, 2)  (0, 10, 1)  (4, 10, 3)  (11, 20, 4)

'''

t = int(input())

for _ in range(t):
    input()
    
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) + [i + 1] for i in range(m)]
    
    arr.sort(key=lambda x:x[1])
    
    arr = arr[:2 * n]
    
    arr.sort(key=lambda x:x[0])
    
    total = 0
    for i in range(2 * n):
        total += arr[i][1]
        
    print(total)
    
    for i in range(n):
        print(arr[i][2], arr[2 * n - i - 1][2])
        
        
        
# D
t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0 for i in range(n + 1)]
    
    for i in range(1, n + 1)[::-1]:
        for j in range(n):
            if arr[j] == i:
                idx = j
                break
            
        ans[i] = (idx + 1) % i # 자기 자신이면 0
        
        arr = arr[idx + 1: i + 1] + arr[:idx + 1] + arr[i + 1:]
    