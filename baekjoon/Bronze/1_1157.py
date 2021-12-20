# 1157번_단어 공부

## 알파벳 대소문자로 된 단어 중 가장 많이 사용된 알파벳 출력
## 대소문자 구분x
## 가장 많이 사용한 알파벳이 여러개라면 ? 출력

word = input().upper() #대소문자 구분x, 출력 대문자이므로 초기 입력을 대문자로 받기
##Mississipi => MISSISSIPI / zZa => ZZA

alphabet = list(set(word)) #입력받은 단어의 각 문자들을 set으로 중복 제거, list만들기. 비교 대상
##M,I,S,P / Z,A 순서 없음

cnt_list = [] #각 문자의 개수를 카운트하여 저장하는 리스트

for i in alphabet : ## i = M, I, S, P / A, Z
    cnt = word.count(i) #입력받은 단어에서 각 문자의 개수 카운트
    ##1, 4, 4, 1 = 각각 M, I, S, P의 개수 /1,2 = 각각 A, Z의 개수

    cnt_list.append(cnt) #카운트 리스트에 추가

if cnt_list.count(max(cnt_list)) >= 2 : #카운트 리스트에서, 최대값의 개수가 2개 이상인 경우
    print("?") #? 출력
    ##Mississipi = 4가 2개니까 "?" 출력

else :
    print(alphabet[(cnt_list.index(max(cnt_list)))])
    #알파벳 리스트에서 대문자로 값 출력
    #인덱스는 카운트 리스트의 인덱스 중 최대값이 있는 자리
    ## A, Z에서 cnt_list = [1, 2]
    ## max(cnt_list) = 2
    ## cnt_list.index(max(cnt_list)) = cnt_list[1]
    ## alphabet = [A, Z]이므로 alphabet[1] = Z