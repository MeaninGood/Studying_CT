# n = int(input())
# words = []
# count = 0
# for _ in range(n):
#   words.append(input())

# for _ in range(n):
#   word = words.pop()
#   words_dict = {}
#   is_answer = True
#   for i in range(len(word)):
#     if word[i] not in words_dict:
#       words_dict[word[i]] = 1
#     else :
#       if word[i-1] == word[i]:
#         pass
#       else : 
#         is_answer = False
#         break
  
#   if is_answer:
#     count += 1

# print(count)


n = int(input())
words = {}
for _ in range(n):
  word = input()
  words[word] = len(word)

answer = [x for x, y in sorted(words.items(), key=lambda x:(x[1], x[0]))]

for i in answer:
  print(i)