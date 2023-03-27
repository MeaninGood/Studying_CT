'''
< 페이지 교체 알고리즘 >
페이지 부재가 발생 하여 새로운 페이지를 할당하기 위해
현재 할당된 페이지 중 어느 것과 교체할지를 결정하는 방법.


LRU (Least Recently Used)
- 페이지 부재 발생 시 가장 오랫동안 사용되지 않은 페이지를 제거

'''


cacheSize = 3
reference = [5, 2, 3, 4, 5, 6, 5, 4, 7]
cache = []

for ref in reference:
    if not ref in cache:               # ref이 cache 안에 없다면
        if len(cache) < cacheSize:      # cache 사이즈보다 cache에 든 게 더 적을 때
            cache.append(ref)           # 넣어줌
        else:                           # cache가 이미 꽉 차고 ref이 cache 안에 없을 때
            cache.pop(0)                # 가장 오래된 것(맨 앞의 것) 지워줌
            cache.append(ref)
        
    else:                               # 이미 ref이 cache 안에 있을 때
        cache.pop(cache.index(ref))     # 길이는 상관 없고 제일 오래 있었던 애 지워줌
        cache.append(ref)               # 새로 추가해 줌

