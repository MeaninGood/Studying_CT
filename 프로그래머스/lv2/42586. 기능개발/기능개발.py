def solution(progresses, speeds):
    answer = []
    n = len(speeds)
    arr = []
    for i in range(n):
        tmp = 100 - progresses[i]
        arr.append( tmp // speeds[i] if tmp % speeds[i] == 0 else (tmp // speeds[i]) + 1)
        
    
    if n == 1:
        return [1]
    
    for i in range(1, n):
        if arr[i] <= arr[i - 1]:
            arr[i] = arr[i - 1]
    
    prefix = [0 for i in range(110)]
    for i in arr:
        prefix[i] += 1
        
    for i in range(110):
        if prefix[i] != 0:
            answer.append(prefix[i])
            
        
    return answer