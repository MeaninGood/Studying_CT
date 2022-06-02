def is_num(a):
    return '0' <= a <= '9'

def solution(files):
    answer = []

    li = []
    for i in range(len(files)):
        s = 0
        e = 0
        for j in range(len(files[i])):
            if is_num(files[i][j]):
                cnt = 0
                s = j
                tmp = j
                while tmp < len(files[i]) and is_num(files[i][tmp]):
                    tmp += 1

                e = tmp
                break
                
        head = files[i][:s].lower()
        number = int(files[i][s:e])
        tail = files[i][e:]
        li.append([head , number , tail, files[i]])

    li.sort(key = lambda x: (x[0], x[1]))
    for i in range(len(li)):
        answer.append(li[i][-1])

    
    return answer