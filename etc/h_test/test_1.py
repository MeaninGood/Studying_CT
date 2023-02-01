import sys
input = lambda : sys.stdin.readline().strip()

k = 1500
rate1 = [1200, 1000, 1100, 1200, 900, 1000, 1500, 900, 750, 1100]
rate2 = [900, 1100, 200, 1000, 1100, 1200, 900, 900]
#        100  1200  1000 2000  900   2100           
rate4 = [900, 800, 700, 600]
rates = [1500, 1400, 1300, 1200]
cnt = False
# 뒤에 2개는 따로 볼 필요가 없네
for i in range(len(rates) - 1):
    # 달러를 사지 않았는데, 가격이 더 높은 경우 패스
    if not cnt and k < rates[i]:
        continue
    # 살 때
    # 현재 가진 돈이 더 많거나 같고, 다음 가격보다 쌀 때
    if k >= rates[i] and rates[i] < rates[i + 1] and not cnt:
        k -= rates[i]
        cnt = True
        continue

    # 팔 때
    # 다음에 팔 가격보다 지금 팔면 더 이득인 경우 팔기
    if rates[i] > rates[i + 1] and cnt:
        k += rates[i]
        cnt = False
        continue

# 맨 마지막에 샀으면(이미 지금 가격이 더 높음) 팔고, 안 샀으면 그냥 끝내기
if rates[-2] < rates[-1]:
    k += rates[-1]

print(k)
