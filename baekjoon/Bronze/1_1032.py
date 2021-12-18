# 1032번_명령 프롬프트

## 파일명의 패턴 출력
## 예를들어 a?b.exe는 acb.exe, aab.exe 등이 출력됨
## 주어진 파일명에서 패턴 도출, 패턴에는 알파벳, ".", "?"만 사용 가능

N = int(input())

first_file = list(input())

for i in range(N-1) :
    other_file = list(input())
    
    for j in range(len(first_file)) :
        if first_file[j] != other_file[j] :
            first_file[j] = "?"

print(''.join(first_file))
