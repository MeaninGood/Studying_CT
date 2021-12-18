# 1032번_명령 프롬프트

## 파일명의 패턴 출력
## 예를들어 a?b.exe는 acb.exe, aab.exe 등이 출력됨
## 주어진 파일명에서 패턴 도출, 패턴에는 알파벳, ".", "?"만 사용 가능

N = int(input()) #파일의 개수 N

first_file = list(input()) #처음 입력되는 파일명을 비교 대상으로 지정

for i in range(N-1) : #이후 N-1개의 파일 반복문으로 추가
    other_file = list(input()) #리스트로 만들어줌
    
    for j in range(len(first_file)) : #first_file과 문자 하나씩 비교
        if first_file[j] != other_file[j] :
            first_file[j] = "?" #다르면 ?로 바꿔줌

print(''.join(first_file))
#print(first_name)으로 하면 ['c','o','n'] 등으로 출력됨
#'구분자'.join(리스트)는 매개변수로 들어온 각 문자를 문자열로 합쳐서 변환
#['c','o','n'] -> con으로 출력해줌
#'_'.join(리스트) : c_o_n으로 출력