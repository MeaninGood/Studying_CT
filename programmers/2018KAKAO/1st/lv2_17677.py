# import math
# def solution(str1, str2):
#     answer = 0

#     arr1 = {}
#     arr2 = {}

#     for i in range(len(str1) - 1):
#         cnt = 0
#         tmp = ''
#         for j in range(i, i + 2):
#             if 'A' <= str1[j] <= 'z':
#                 cnt += 1
#                 tmp += str1[j].lower()

#         if cnt == 2:
#             arr1[tmp] = arr1.get(tmp, 0) + 1

#     for i in range(len(str2) - 1):
#         cnt = 0
#         tmp = ''
#         for j in range(i, i + 2):
#             if 'A' <= str2[j] <= 'z':
#                 cnt += 1
#                 tmp += str2[j].lower()

#         if cnt == 2:
#             arr2[tmp] = arr2.get(tmp, 0) + 1

#     mxd = arr1.copy()
#     mxtotal = 0
#     for i in arr2:
#         if i in mxd:
#             mxd[i] = max(arr2[i], mxd[i])
#             mxtotal += mxd[i]
#         else:
#             mxd[i] = arr2[i]
#             mxtotal += mxd[i]

#     mn = 0
#     for i in arr1:
#         for j in arr2:
#             if i == j:
#                 mn += min(arr1[i], arr2[i])

#     mx = 0
#     for i in mxd:
#         mx += mxd[i]

#     answer = math.trunc((mn / mx) * 65536)
#     return answer



# import math
# def solution(str1, str2):
#     answer = 0

#     arr1 = {}
#     arr2 = {}

#     for i in range(len(str1) - 1):
#         cnt = 0
#         tmp = ''
#         for j in range(i, i + 2):
#             if 'A' <= str1[j] <= 'z':
#                 cnt += 1
#                 tmp += str1[j].lower()

#         if cnt == 2:
#             arr1[tmp] = arr1.get(tmp, 0) + 1

#     for i in range(len(str2) - 1):
#         cnt = 0
#         tmp = ''
#         for j in range(i, i + 2):
#             if 'A' <= str2[j] <= 'z':
#                 cnt += 1
#                 tmp += str2[j].lower()

#         if cnt == 2:
#             arr2[tmp] = arr2.get(tmp, 0) + 1

#     mxd = arr1.copy()
#     for i in arr2:
#         if i in mxd:
#             mxd[i] = max(arr2[i], mxd[i])
#         else:
#             mxd[i] = arr2[i]

#     mn = 0
#     for i in arr1:
#         for j in arr2:
#             if i == j:
#                 mn += min(arr1[i], arr2[i])

#     mx = 0
#     for i in mxd:
#         mx += mxd[i]

#     answer = math.trunc((mn / mx) * 65536)
#     return answer



# import math

# str1 = 'A+C'
# str2 = 'DEF'

# arr1 = {}
# arr2 = {}

# for i in range(len(str1) - 1):
#     cnt = 0
#     tmp = ''
#     for j in range(i, i + 2):
#         if 'a' <= str1[j].lower() <= 'z':
#             cnt += 1
#             tmp += str1[j].lower()

#     if cnt == 2:
#         arr1[tmp] = arr1.get(tmp, 0) + 1

# for i in range(len(str2) - 1):
#     cnt = 0
#     tmp = ''
#     for j in range(i, i + 2):
#         if 'a' <= str2[j].lower() <= 'z':
#             cnt += 1
#             tmp += str2[j].lower()

#     if cnt == 2:
#         arr2[tmp] = arr2.get(tmp, 0) + 1
        
#     if len(arr1) == 0 and len(arr2) == 0:
#         print(65536)
#         exit()

# mxd = arr1.copy()
# for i in arr2:
#     if i in mxd:
#         mxd[i] = max(arr2[i], mxd[i])
#     else:
#         mxd[i] = arr2[i]

# mn = 0
# for i in arr1:
#     for j in arr2:
#         if i == j:
#             mn += min(arr1[i], arr2[i])
            
# mx = 0
# for i in mxd:
#     mx += mxd[i]


# answer = math.trunc((mn / mx) * 65536)
# print(answer)




import math
def solution(str1, str2):
    answer = 0

    arr1 = {}
    arr2 = {}

    for i in range(len(str1) - 1):
        cnt = 0
        tmp = ''
        for j in range(i, i + 2):
            if 'a' <= str1[j].lower() <= 'z':
                cnt += 1
                tmp += str1[j].lower()

        if cnt == 2:
            arr1[tmp] = arr1.get(tmp, 0) + 1

    for i in range(len(str2) - 1):
        cnt = 0
        tmp = ''
        for j in range(i, i + 2):
            if 'a' <= str2[j].lower() <= 'z':
                cnt += 1
                tmp += str2[j].lower()

        if cnt == 2:
            arr2[tmp] = arr2.get(tmp, 0) + 1

        if len(arr1) == 0 and len(arr2) == 0:
            return 65536

    mxd = arr1.copy()
    for i in arr2:
        if i in mxd:
            mxd[i] = max(arr2[i], mxd[i])
        else:
            mxd[i] = arr2[i]

    mn = 0
    for i in arr1:
        for j in arr2:
            if i == j:
                mn += min(arr1[i], arr2[i])

    mx = 0
    for i in mxd:
        mx += mxd[i]


    answer = math.trunc((mn / mx) * 65536)
    return answer