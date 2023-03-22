import sys
input = lambda : sys.stdin.readline().strip()

idx = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR',
       'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']

# d_idx
# zero부터 다 세서 {0 : {Z : 1, E:1, R:1, O:1}, ...} 구조 만들기


T = int(input())
for tc in range(T):
    arr = list(input())
    
    d = {}
    n = len(arr)
    for i in range(n):
        d[arr[i]] = d.get(arr[i], 0) + 1
        
    #d_dix랑 비교해서 개수 뺄 수 있으면 추가