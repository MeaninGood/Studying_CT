# stack1 = [10, 20, 30]
# stack2 = [8]
# stack3 = [1]

# answer = ''

# d = [0, -10000]
# stacks = [stack1, stack2, stack3]
# mx = 0
# while 1:
#     if stacks == [[], [], []]:
#         break

#     for i in range(3):
#         if not stacks[i]:
#             continue

#         if stacks[i][-1] > d[1]:
#             d = [i, stacks[i][-1]]
#             print(d)

#     answer += str(d[0] + 1)
    
#     stacks[d[0]].pop()
#     d = [0, -10000]
    

# print(answer)






# sentences = 'This ate an apple Oh John'
# answer = ''
# arr = sentences.split(' ')
    
# n = len(arr)
# for i in range(n):
#     if arr[i][0].isupper():
#         if i > 1 and arr[i - 1][0].isupper():
#             answer += 'X'

#         elif i > 1 and arr[i - 1][0].islower():
#             answer += ' '

#         answer += 'X' * len(arr[i])

#     else:
#         if i == 0:
#             answer += arr[i]

#         else:
#             answer += ' ' + arr[i]

# print(answer)

import spacy

nlp = spacy.load("en_core_web_sm")

def anonymize_text(sentences):
    answer = list(sentences)
    doc = nlp(sentences)

    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            for i in range(ent.start_char, ent.end_char):
                answer[i] = 'X'

    return ''.join(answer)

sentences = 'John ate an apple Oh John'
anonymize_text(sentences)








# def solution(S, C):
#     n = len(S)
#     arr = [[0 for i in range(n)] for j in range(26)]

#     for i in range(n):
#         arr[ord(S[i]) - 97][i] += 1
    
    
    
#     for i in range(26):
#         for j in range(1, n):
#             arr[i][j] += arr[i][j - 1]
    
#     print(arr)
#     print('===============')

#     m = len(C)
#     for k in range(m):
#         flag1 = False
#         flag2 = False
#         for i in range(26):
#             if arr[i][C[k] - 1] > 1:
#                 flag1 = True
#             for j in range(C[k], n):
#                 arr[i][j] -= arr[i][C[k] - 1]
#                 if arr[i][j] > 1:
#                     flag2 = True

#         if not flag1 and not flag2:
#             return k + 1

#     print(arr)
# S = 'aabcddcb'
# C = [3, 5, 1, 4, 7]
# solution(S, C)