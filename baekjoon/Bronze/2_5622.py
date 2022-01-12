# 5622번_다이얼

## 숫자 하나 누르면 다이얼 처음 위치로 돌아감
## 다음 다이얼 누를 때 처음 위치에서 다시 돌림
## 숫자 1 걸려면 총 2초 필요, 한 칸 옆은 1초씩 더 걸림
## 전화 번호를 각 숫자에 해당하는 문자로 침
## 1 : ABC, 2 : DEF,... 7 : PQRS, 8 : TUV, 9 WXYZ

word = input().upper() # 대문자로 받기

idx = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'] # 각 번호에 입력된 다이얼

cnt = 0 # 전화 걸기 위해 필요한 최소 시간 초기값 0초
for i in range(len(word)) : # 문자 세기
    for j in idx : # idx를 돌며 각 문자가 다이얼의 어디 적힌 숫자인지 셀 것 
        if word[i] in j : # idx에서 word의 [i] 자리에 해당하는 다이얼 찾기
            cnt += idx.index(j)+3 
            # 문제에서 다이얼이 숫자 2번부터 적혀 있음, 숫자 1을 걸려면 총 2초가 필요
            # 2번을 걸려면 3초가 필요하기 때문에 +3을 해줌

print(cnt)