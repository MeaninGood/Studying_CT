# 3003번_킹, 퀸, 룩, 비숍, 나이트, 폰

## 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성
## 피스의 개수가 주어졌을 때, 몇 개를 더하거나 뺴야 올바른 세트가 되는지


'''
# 첫째 줄에 킹, 퀸, 룩, 비숍, 나이트, 폰의 개수가 주어짐
## 입력에서 주어진 순서대로 몇 개의 피스를 더하거나 뺴야 되는지 출력

(입력) 2 1 2 1 2 1
(출력) -1 0 0 1 0 7
'''


chess = [1, 1, 2, 2, 2, 8]

cnt = list(map(int, input().split()))

for i in range(len(cnt)) :
    print(chess[i] - cnt[i], end = ' ')


# ==== 배열 이용하기 (2)
# chess = [1, 1, 2, 2, 2, 8]

# cnt = list(map(int, input().split()))

# n = len(cnt)
# result = []

# for i in range(n) :
#     result.append(chess[i] - cnt[i])
    
# print(*result)
        
        
    