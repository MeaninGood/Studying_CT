n = int(input())
arr = input().split()

visited = [False for i in range(10)]
mn = 10000000000000
mx = -1000000000000
def recur(cur, tmp):
    global mn, mx
    if cur == n + 1:
        # 부등호를 만족만 한다면
        # 가장 먼저 딸려 나오는 애가
        # 가장 작은 숫자다
        for i in range(n):
            if arr[i] == "<" and tmp[i] > tmp[i + 1]:
                return
            
            if arr[i] == '>' and tmp[i] < tmp[i + 1]:
                return
        
        if mn > int(tmp):
            mn = int(tmp)
        
        if mx < int(tmp):
            mx = int(tmp)

        return
    
    for i in range(10):
        if visited[i]:
            continue
        
        visited[i] = True
        recur(cur + 1, tmp + str(i))
        visited[i] = False
  
recur(0, "")

print(str(mx))
print(str(mn))
# n, m = 3, 5
# visited = [False for i in range(m)]
# def recur(cur, tmp):
#     if cur == n:
#         print(tmp)
#         # 부등호를 만족만 한다면
#         # 가장 먼저 딸려 나오는 애가
#         # 가장 큰 숫자
#         return
    
#     for i in range(m)[::-1]:
#         if visited[i]:
#             continue
        
#         visited[i] = True
#         recur(cur + 1, tmp + str(i))
#         visited[i] = False
        

