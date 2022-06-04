def solution(words, queries):
    answer = []
    
    qlen = len(queries)
    wlen = len(words)
    
    idx = 0
    while idx < qlen:
        tmp = queries[idx]
        print(tmp)
        cnt = 0
        if tmp[0] != '?':
            tmplen = len(tmp[0])
            for i in range(wlen):
                flag = True
                for j in range(tmplen):
                    print(tmp[0][j])
                    if tmp[j] != words[i][j]:
                        flag = False
                        break
                
                if not flag:
                    continue
                
                if len(tmp) == len(words[i]):
                    cnt += 1
            
            answer.append(cnt)
                        

        if tmp[0] == '?':
            tmplen = len(tmp[-1])
            tmp = tmp[::-1]
            for i in range(wlen):
                flag = True
                w = words[i][::-1]
                for j in range(tmplen):
                    if tmp[j] != w[j]:
                        flag = False
                        break
                
                if not flag:
                    continue
                
                if len(tmp) == len(words[i]):
                    cnt += 1
            
            answer.append(cnt)
            
        idx += 1
        
            
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
               ["fro??", "????o", "fr???", "fro???", "pro?","???st"]))





# def solution(words, queries):
#     answer = []

#     d1 = {}
#     d2 = {}
#     for i in words:
#         tmp = i
#         ilen = len(i)
#         for j in range(1, ilen + 1):
#             tmp = ('?' * j) + i[j:]
#             # print(tmp)
#             d1[tmp] = d1.get(tmp, 0) + 1
            
#         tmp2 = i    
#         for j in range(ilen + 1)[::-1]:
#             tmp2 = i[:j] + ('?' * (ilen - j))
#             # print(tmp2)
#             d2[tmp2] = d2.get(tmp2, 0) + 1

#     for i in queries:
#         answer.append(max(d1.get(i, 0), d2.get(i, 0)))
 
#     return answer



# def solution(words, queries):
#     answer = []

#     d = {}
#     for i in words:
#         ilen = len(i)
#         for j in range(ilen):
#             tmp = ('?' * j) + i[j:]
#             d[tmp] = d.get(tmp, 0) + 1
            
#             tmp = i[:j] + ('?' * (ilen - j))
#             d[tmp] = d.get(tmp, 0) + 1
            
#     for i in queries:
#         answer.append(d.get(i, 0))
 
#     return answer


# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
#                ["fro??", "????o", "fr???", "fro???", "pro?","?????"]))



# def solution(words, queries):
#     answer = [0 for i in range(len(queries))]
    
#     sort_words = words.copy()
#     sort_words.sort()
#     print(sort_words)

#     # d = {}
#     # for i in range(len(words)):
#     #     ilen = len(words[i])
#     #     for j in range(ilen):
#     #         tmp1 = ('?' * j) + words[i][j:]
#     #         if tmp1 in queries:
#     #             print(f'tmp1은 {tmp1}')
#     #             answer[queries.index(tmp1)] += 1
            
#     #         tmp2 = words[i][:j] + ('?' * (ilen - j))
#     #         if tmp2 in queries:
#     #             print(f'tmp2는 {tmp2}')
#     #             answer[queries.index(tmp2)] += 1

#     return answer


# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
#                ["fro??", "????o", "fr???", "fro???", "pro?","?????", "???st"]))




# def solution(words, queries):
#     answer = []

#     d = {}
#     for i in words:
#         ilen = len(i)
#         for j in range(ilen):
#             tmp = ('?' * j) + i[j:]
#             d[tmp] = d.get(tmp, 0) + 1
            
#             tmp = i[:j] + ('?' * (ilen - j))
#             d[tmp] = d.get(tmp, 0) + 1
            
#     for i in queries:
#         answer.append(d.get(i, 0))
        
#     return answer


# print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
#                ["fro??", "????o", "fr???", "fro???", "pro?","?????"]))

