# str1 = "hahaha"
# str2 = "hajaha"

# arr1 = {}
# arr2 = {}

# for i in range(len(str1) - 1):
#     cnt = 0
#     tmp = ''
#     for j in range(i, i + 2):
#         if 'A' <= str1[j] <= 'z':
#             cnt += 1
#             tmp += str1[j].lower()
            
#     if cnt == 2:
#         arr1[tmp] = arr1.get(tmp, 0) + 1

# for i in range(len(str2) - 1):
#     cnt = 0
#     tmp = ''
#     for j in range(i, i + 2):
#         if 'A' <= str2[j] <= 'z':
#             cnt += 1
#             tmp += str2[j].lower()
            
#     if cnt == 2:
#         arr2[tmp] = arr2.get(tmp, 0) + 1

# print(arr1)
# print(arr2)
# # mn = {}
# # mx = {}
# # mntotal = 0
# # mxtotal = 0
# # for i in arr1:
# #     if i in arr2:
# #         mn[i] = min(arr1[i], arr2[i])
# #         mntotal += min(arr1[i], arr2[i])
# #         mx[i] = max(arr1[i], arr2[i])
# #         mxtotal += max(arr1[i], arr2[i])
# #         arr2.pop(i)
# #     else:
# #         mx[i] = 1
# #         # mxtotal += arr2[i]

# # print(mn)
# # print(mx)

# # print(f'{(mntotal / mxtotal) * 65536:.0f}')
        

# mxd = arr1

# for i in arr2:
#     mxd[i] = mxd.get(i, max(mxd[i], arr2[i])) + 1
    
# print(mxd)

