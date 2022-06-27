# report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]

# id_list = ["muzi", "frodo", "apeach", "neo"]
id_list = ["con", "ryan"]
d = {}

k = 2

def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    
    d = {}
    
    for i in range(len(report)):
        tmp = report[i].split()

        user, repo = tmp[0], tmp[1]
        d[repo] = d.get(repo, [])
    
        if user not in d[repo]:
            d[repo].append(user)

    for i in d:
        if len(d[i]) >= k:
            for name in d[i]:
                answer[id_list.index(name)] += 1
            
    return answer

print(solution(id_list, report, k))