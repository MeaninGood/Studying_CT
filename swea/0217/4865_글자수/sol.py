import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    word = input()
    arr = input()

    w = len(word)  # 딕셔너리로 만들 문자열 길이 w
    a = len(arr)  # 찾아야 하는 배열의 길이 a
    dit = {}  # 딕셔너리 생성
    for i in range(w):  # word를 돌면서
        dit[word[i]] = 0  # word[i]를 0으로 키 : 값 쌍으로 만들어 둠
        for j in range(a):  # arr를 돌면서
            if word[i] == arr[j]:  # word의 키로 만들어 둔 문자들만 골라서
                dit[word[i]] += 1  # +1씩 카운트해 줌
    print(dit)
    print(f'#{tc}', max(dit.values()))  # 최대값의 values 출력
