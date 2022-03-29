T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    # 이차원 배열 생성, 카운팅 소트 해줄 배열
    p1 = [[] for i in range(12)]
    p2 = [[] for i in range(12)]

    # 배열이 비었는지 안 비었는지 T, F 리턴
    def check(x):
        return 0 < len(x)

    def baby():
        for i in range(12):
            if i % 2 == 0: # 홀수번째로 들어오는 애들
                p1[arr[i]].append(arr[i])
                
                if len(p1[arr[i]]) == 3: # 해당 카드가 3장 모이면
                    return 1
                
                for j in range(2, 10): # 연속한 카드 3장이 들어온다면
                    if check(p1[j - 2]) and check(p1[j - 1]) and check(p1[j]):
                        return 1

            
            elif i % 2: # 짝수번째로 들어오는 애들
                p2[arr[i]].append(arr[i])
                
                if len(p2[arr[i]]) == 3:
                    return 2
                
                for j in range(2, 10):
                    if check(p2[j - 2]) and check(p2[j - 1]) and check(p2[j]):
                        return 2
        
        return 0

    print(f'#{tc} {baby()}')
