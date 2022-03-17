# # 연속 부분 수열
# ## 투포인터
# ## 누적합

# '''
# 누적합

# prefix[i] : arr[1] + arr[2] + arr[3] + arr[4] + ... + arr[i]

# prefix[i] = prefix[i - 1] + arr[i]


# 5 4 3 2 1

# 1까지의 합 : arr[1]
# 1~2 : arr[1] + arr[2]
# 1~3 합 : arr[1] + arr[2] + arr[3]
# ...


# 2~4합이면
# 1~4합 - 1합

# '''
# # 11659 구간 합 구하기4

# n, m = map(int, input().split())
# arr = [0] + list(map(int, input().split()))
# prefix = [0 for i in range(n + 1)]

# for i in range(1, n + 1):
#     prefix[i] = prefix[i - 1] + arr[i]
    
# for _ in range(m):
#     a, b = map(int, input().split())
    
#     print(prefix[b] - prefix[a - 1])
    
    


# # 2559 수열
# '''
# prefix[6] - prefix[1]
# prefix[7] - prefix[2]

# '''
# n, m = map(int, input().split())
# arr = list(map(int, input().split()))
# prefix = [0 for i in range(n + 1)] # 어지간하면 앞에 한 칸 붙여줘라
# # prefix[b] - prefix[a - 1] 하는데 a가 0이면 -1이 되니까 패딩해주는 것

# for i in range(1, n + 1):
#     prefix[i] = prefix[i - 1] + arr[i]
    
# ans = -(1 << 60) # 아주 작은 수로 해주기, 합이 음수일 수도 있으니까
# for i in range(m , n + 1):
#     ans = max(ans, prefix[i] - prefix[i - m])

# print(ans)




# # 11660 구간 합 구하기 5

# n, m = map(int, input().split())
# arr = [[0 for i in range(n + 1)] + [0] + list(map(int, input().split())) for i in range(n)]
# prefix = [[0 for i in range(n + 1)] for j in range(n + 1)]

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + arr[i][j]
        
# for _ in range(m):
#     a, b, c, d = map(int, input().split())
    
#     print(prefix[c][d] - prefix[a - 1][d] - prefix[c][b - 1] + prefix[a - 1][b - 1])
        

# # 2015 수들의 합 4
# '''
# 7 5
# 0 1 2 3 4 5 0 5맨 앞에 제로패딩

# 0 1 3 6 10 15 15 20
# 이 중에서 5가 되는 걸 찾겠다
# == 뒤에거에서 앞에 걸 뺀 게 5가 되는 걸 찾겠다
# == 여기서 두 수의 차이


# 카운팅 배열

# cnt[0] = 1
# cnt[1] = 1
# cnt[3] = 1
# 6 해주기 전에 5 되는 게 몇 개 있냐 (cnt[1])
# cnt[6] = 1
# 10 해주기 전에 5되는 게 몇 개 있냐 (cnt[5])
# cnt[10] = 1
# 15 해주기 전에 5 되는 게 몇 개 있냐 (cnt[10])
# cnt[15] = 2
# cnt[20] = 1

# 연속 부분 수열에 대한 문제를 두 수에 대한 문제로 바꾼다. 

# 근데 이 문제에서는 n 제한이 20억이라 딕셔너리 써야 함

# '''

# # 카운팅 소트로 만들기
# n, m = map(int, input().split())
# arr = [0] + list(map(int, input().split()))
# prefix = [0 for i in range(n + 1)]
# cnt = [0 for i in range(100010)]

# for i in range(1, n + 1):
#     prefix[i] = prefix[i - 1] + arr[i]
    
# ans = 0
# for i in range(n + 1):
#     ans += cnt[prefix[i] - m]
    
#     cnt[prefix[i]] += 1
    

# 딕셔너리로 해주기  
# n, m = map(int, input().split())
# arr = [0] + list(map(int, input().split()))
# prefix = [0 for i in range(n + 1)]
# cnt = {}

# for i in range(1, n + 1):
#     prefix[i] = prefix[i - 1] + arr[i]
    
# ans = 0
# for i in range(n + 1):
#     ans += cnt.get(prefix[i] - m, 0) # 저런 키를 넣은 적이 없으면 0이 리턴됨
    
#     cnt[prefix[i]] = cnt.get(prefix[i], 0) + 1 # prefix[i]가 있으면 얘 + 1
#                                        # 없으면 0 + 1
# print(cnt)
# print(ans)


# n = int(input())
# arr = [0] + [input() for _ in range(n)]
# prefix = [0 for _ in range(n + 1)]
# idx = ['P', 'H', 'S']

# mx = 0
# for i in range(1, n + 1):
#     cnt[arr[i]] = cnt.get(arr[i], 0) + 1
    
# mx = max(cnt[arr[i]])

# print(mx)


    
    # ans += cnt[prefix[i] - m]

# for i in range(1, n + 1):
#     prefix[i] = prefix[i - 1] + arr[i]
    
#     cnt[prefix[i]] += 1



n = int(input())
arr = [0] + [input() for _ in range(n)]
prefix = [0 for _ in range(n + 1)]
cnt = {}


for i in range(1, n + 1):
    cnt[arr[i]] = cnt.get(arr[i], 0) + 1
    prefix[i] = cnt[arr[i]]


for i in range(1, n + 1):
    
print(prefix)

'''

P P H P S P P H H H H H H S S
1 2 1 3 1 4 5 2 3 4 5 6 7 2 3

'''