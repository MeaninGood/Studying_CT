import sys

input = lambda: sys.stdin.readline().strip()

n = int(input())
arr = list(map(int, input().split()))

total = 0
cards = []
for i in range(0, n, 2):
    total += arr[i]
    if arr[i + 1] > arr[i]:
        cards.append([arr[i + 1], arr[i]])
    
cards.sort(key = lambda x: -abs(x[1] - x[0]))
tmp = total - cards[0][1] + cards[0][0]
print(cards)
print(total, tmp)

print(max(tmp, total))
