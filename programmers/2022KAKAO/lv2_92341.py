import math
def solution(fees, records):
    answer = []
    
    for i in range(len(records)):
        records[i] = records[i].split()
        
        records[i][0] = records[i][0].split(':')
        x, y = records[i][0]
        
        tmp = (int(x) * 60) + (int(y))
        
        records[i][0] = tmp

    d = {}
    d2 = {}
    for i in range(len(records)):
        if records[i][2] == 'IN':
            d[records[i][1]] = d.get(records[i][1], records[i][0])
            
        elif records[i][2] == 'OUT' and records[i][1] in d:
            d2[records[i][1]] = d2.get(records[i][1], 0) + (records[i][0] - d[records[i][1]])
            del d[records[i][1]]
    
    if len(d) > 0:
        for i in d:
            d2[i] = d2.get(i, 0) + (((23 * 60) + 59)- d[i])

    cnt = 0
    for i in d2:
        cnt += 1
        if d2[i] <= fees[0]:
            d2[i] = fees[1]
        else:
            d2[i] = fees[1] + math.ceil((d2[i] - fees[0]) / fees[2]) * fees[3]
    
    idx = sorted(d2)

    for i in range(len(idx)):
        answer.append(d2[idx[i]])

            
    return answer

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))