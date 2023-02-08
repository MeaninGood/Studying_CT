def solution(people, limit):
    answer = 0
    """
       s
    50 50 50 50 70 80
        e
      s  
    50 50
      e
      
    50
    s
    50 60 70 80 90 100
    e
    """
    if len(people) == 1:
        return 1
    
    people.sort()
    
    s = 0
    e = len(people) - 1
    while s <= e:
        if s < e and people[s] + people[e] <= limit:
            answer += 1
            s += 1
            e -= 1
        
        elif s < e and people[s] + people[e] > limit:
            answer += 1
            e -= 1
        
        elif s == e:
            answer += 1
            break
    
    
    
    return answer