from itertools import permutations

# k = 현재 피로도
# [최소 필요 피로도, 소모 피로도]
def solution(k, dungeons):
    answer = 0
    arr = list(permutations(dungeons, len(dungeons)))
    
    for i in range(len(arr)):
        total = 0
        tmp_k = k
        for j in range(len(arr[0])):
            if tmp_k >= arr[i][j][0] and tmp_k >= arr[i][j][1]:
                tmp_k -= arr[i][j][1]
                total += 1
            
            else:
                break
                
        answer = max(answer, total)
            
                
        
        
    return answer