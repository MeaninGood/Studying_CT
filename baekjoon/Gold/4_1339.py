import sys
input = lambda : sys.stdin.readline().strip()


n = int(input())
arr = [list(input()) for _ in range(n)]

d = {}
for i in range(n):
    idx = len(arr[i])
    for j in range(len(arr[i])):
        tmp = 10 ** (idx - 1) # 가중치 부여 (자릿수)
        if d.get(arr[i][j]):
            d[arr[i][j]] += tmp
        
        else:
            d[arr[i][j]] = d.get(arr[i][j], tmp)
        
        idx -= 1
        
li = sorted(d.items(), key=lambda x : -x[1]) # value 기준으로 정렬

total = 0
idx = 9
for k, v in li:
    total += idx * v # 10000의 자리 A에 9를 넣는다는 것 = 9가 10000개 있다는 뜻이므로 total에 바로 곱해서 더하기
    idx -= 1
    
print(total)