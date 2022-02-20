import sys
sys.stdin = open('input.txt')
t = int(input())
for tc in range(1, t+1):
    word = input()
    arr = input()

    s = 0 # 시작 인덱스
    e = len(word) # 끝 인덱스
    n = len(arr) # 배열 길이
    while 1:
        # 배열의 시작~끝 인덱스가 word와 같다면
        if arr[s:e] == word:
            print(f'#{tc} 1') # 1 출력 후 break
            break
        # s가 arr의 마지막 부분까지 갔는데도 word와 같은 단어가 없다면
        if s == len(arr) - len(word) + 1:
            print(f'#{tc} 0') # 0 출력 후 break
            break
        # arr[s:e]가 word와 같지 않다면 시작~끝 인덱스 +1씩 추가
        elif arr[s:e] != word:
            s += 1
            e += 1
            continue