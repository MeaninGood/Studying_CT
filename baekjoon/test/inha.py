# 1

# n = int(input())
# word = input()

# q = 'qwertasdfgzxcv'
# a = 'yuiophjklbnm'

# if (len(word) > 2) and (word[-3] in q) and (word[-2] in a) and (word[-1] in q):
#     print(1)

# else:
#     print(0)



# 2
# d = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 
#      'D+': 1.5, 'D0': 1.0, 'F': 0.0}

# total = 0
# cnt = 0
# for _ in range(20):
#     a, b, c = input().split()
    
#     if c == '':
#         continue
    
#     total += float(b) * d[c]
#     cnt += float(b)

# if total == 0:
#     print(f'{0:.6f}')
# else:
#     print(f'{(total / cnt):.6f}')





# 3

# def recur(cur, total, cnt):
#     global ans
    
#     if cur == n:
#         if (99 / 100) <= total <= (101 / 100) and cnt > 0:
#             ans += 1
#         return
    

#     recur(cur + 1, total + (1 / arr[cur]), cnt + 1)
#     recur(cur + 1, total, cnt)
    

# n = int(input())
# arr = list(map(int, input().split()))
# ans = 0
# recur(0, 0, 0)
# print(ans)




# 4
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

ans = [0]
mn = arr[0]
mx = 0

for i in range(1, n):
    mn = min(mn, arr[i])
    mx = max(mx, arr[i] - mn)
    ans.append(mx)
    
print(*ans)
