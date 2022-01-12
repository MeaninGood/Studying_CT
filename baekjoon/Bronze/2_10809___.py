# 10809번_알파벳 찾기

## 알파벳 소문자로만 이루어진 단어 S
## 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치,
## 포함되어 있지 않은 경우에는 -1 출력
## 첫째 줄 단어S, 알파벳 소문자
## 각각의 알파벳에 대해 a가 처음 등장하는 위치, b가 처음 등장하는 위치
## ...z가 처음 등장하는 위치 공백으로 구분해서 출력


'''
S = input()

idx = 0
alphabet = [ chr(k) for k in range(97, 123) ]
for i in range(len(S)) : 
    for j in range(26) :
        alphabet = -1
        if S[i] == alphabet[j] :
            alphabet[j] = idx
            idx += 1
            break
print(alphabet)

'''

## for i in range(97, 123) 보다는
## for i in range(ord('a'), ord('z') + 1) 이 좀더 직관적이고 좋아요

''' 내가 짠 망한 코드 2
S = input()

for i in range(ord('a'), ord('z') + 1) : ## 26개의 -1 생성
    for j in range(len(S)) : 
        alphabet = -1 # 
        if chr(i) == S[j] : 
            alphabet = j # 그자리의 숫자를 j(S의 인덱스)로 바꿔줌
            break

    print(alphabet, end = ' ')
'''

''' 갓튜브 - 리스트 안 쓰고 만들기 -------1
test_word = input()

for i in range(26):
    print(test_word.find(chr(i+97)), end=" ")            
'''

'''싸합님 [-1] 26개 생성 후 find 함수로 출력 -------2
test_word = input()
alphabet_group = [-1] * 26

for i in range(len(alphabet_group)):
    print(test_word.find(chr(i+97)),end=' ')
'''

## ord('A') : 65 <-> chr(65), ord('Z') : 90
## ord('a') : 97, ord('z') : 122 <-> chr(122)

# S = input()
# a = 'abcdefghijklmnopqrstuvwxyz'


''' 내가 짠 망한 코드

S = input()

idx = 0
alphabet = [ chr(k) for k in range(97, 123) ]
for i in range(len(S)) : 
    for j in range(26) :
        if S[i] == alphabet[j] :
            alphabet[j] = idx ##
            idx += 1
        else :
            alphabet[j] = '-1'
print(alphabet)

else가 두번째 for문에 붙으면 j가 없어서 안될것 같아요
저 else에 있는건 첫 for문이 모두 끝난 뒤 판단해야 되는거라서

'''

''' ...님 코드 - 피드백 ------3
S = input()

idx = 0
alphabet = [ -1 for i in range(26) ]
for i in range(0,len(S),-1) : 
    for j in range(26) :
        if S[i] == chr(j + 'a') :
            alphabet[j] = idx ##
            idx += 1
print(alphabet)

어제 max값 구할때 최대보다 자기가 크면 바꾼다
=> 가장 큰것중 제일 앞, 크거나 같으면 바꾼다
=> 제일 뒤라고 했으니 같은 맥락으로 처음 나올때만 바꾼다
=>첫 인덱스, 나올때마다 바꾼다
=> 마지막 인덱스가 나와요

''' 

''' 갓튜브님 코드2 -------4
S = input()

for i in range(ord('a'), ord('z') + 1):
    alphabet = -1
    for j in range(len(S)):
        if chr(i) == S[j] and S.index(chr(i)) == j:
            alphabet = j
            break
    print(alphabet, end=" ")
'''


''' 싸합님 코드2 - 딕셔너리 ------5
S = input()

idx = 0
dic_alpha = dict()
for i in range(ord('a'),ord('z')+1):
    dic_alpha[chr(i)]=-1
for j in S:
    if dic_alpha[j]==-1:
        dic_alpha[j]=idx
    idx+=1

for v in dic_alpha.values():
    print(v,end=' ')
'''

'''...님 코드2 -------6 wow
s = input()

idx = [-1 for i in range(26)]
for i in range(len(s))[::-1]:
  idx[ord(s[i]) - ord('a')] = i

print(*idx)
'''

