import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))

cards = [False for _ in range(1000010)]
score = [0 for _ in range(1000010)]

for num in arr:
    cards[num] = True
    
for i in arr:
    for j in range(i * 2, 1000010, i):
        if cards[j]:
            score[i] += 1
            score[j] -= 1
            
ans = []
for num in arr:
    ans.append(score[num])
    
print(*ans)
