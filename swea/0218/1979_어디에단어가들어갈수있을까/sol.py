# N X N 크기
# 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수
# N은 5 이상 15 이하의 정수
# K는 2 이상 N 이하의 정수

'''
# 입력은 첫 줄에 총 테스트 케이스의 개수 T
# 다음 줄부터 각 테스트 케이스
# 테스트 케이스의 첫 번째 줄에는 단어 퍼즐의 가로, 세로 길이 N 과, 단어의 길이 K
# 테스트 케이스의 두 번째 줄부터 퍼즐의 모양이 2차원 정보로 주어짐
# 퍼즐의 각 셀 중, 흰색 부분은 1, 검은색 부분은 0
## 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력

'''
    
def find_idx(arr, n):
    idx = 0
    i = 0
    while i != n:
        if arr[i] == 1:
            idx = i
            break
        i += 1
    return idx
    

T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = 0
    for i in range(n):
        idx = find_idx(arr[i], n)
        
        temp = 0
        for j in range(idx, n):
            if arr[j] == 1:
                cnt += 1
                
        if temp >= k:
            cnt += 1
            
    print(f'#{t} {cnt}')