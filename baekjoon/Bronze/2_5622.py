# 5622번_다이얼

## 숫자 하나 누르면 다이얼 처음 위치로 돌아감
## 다음 다이얼 누를 때 처음 위치에서 다시 돌림
## 숫자 1 걸려면 총 2초 필요, 한 칸 옆은 1초씩 더 걸림
## 전화 번호를 각 숫자에 해당하는 문자로 침
## 1 : ABC, 2 : DEF,... 7 : PQRS, 8 : TUV, 9 WXYZ

word = input().upper()

idx = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

cnt = 0
for i in range(len(word)) :
    for j in idx :
        if word[i] in j :
            cnt += idx.index(j)+3

print(cnt)
