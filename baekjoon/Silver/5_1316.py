# 1316번_그룹 단어 체커

## 각 문자가 연속해서 나타나는 경우
## 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성

'''
# 첫째 줄에 단어의 개수 N, N은 100보다 작거나 같은 자연수
# 둘째 줄부터 N개의 줄에 단어
# 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100

(입력)
3
happy
new
year

(출력)
3
'''

def check(arr):
    d = {}
    for i in range(0, len(arr) - 1):
        d[arr[i]] = d.get(arr[i], 0) + 1
        
        if arr[i + 1] != arr[i] and arr[i + 1] in d:
            return 0
        
    return 1

n = int(input())
ans = 0
for i in range(n):
    arr = list(input())
    
    ans += check(arr)
    
print(ans)
        
        