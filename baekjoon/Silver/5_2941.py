# 2941번_크로아티아 알파벳

## 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력
## 글자 수 세서 출력하기

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] # 크로아티아 알파벳
word = input() # 예제 입력
for i in cro : # i가 cro 리스트를 돌며
    word = word.replace(i, '*') # word에서 cro[i]에 해당하는 단어를 *로 바꿈

print(len(word)) # 길이 출력
