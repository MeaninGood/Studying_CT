import sys
sys.stdin = open('GNS_test_input.txt', encoding='UTF-8')

t = int(input())
for tc in range(t):
    case, m = input().split()
    arr = input().split()
    # 숫자 체계 저장한 리스트
    li = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    # 입력 받은 문자열을 숫자로 바꿔서 저장할 리스트
    res = []
    for i in arr:
        res.append(li.index(i)) #li의 인덱스로 접근해 li의 값에 해당하는 인덱스를 바로 res에 저장

    res.sort() # 정렬

    print(case) # 출력할 케이스 번호
    for j in res: # res 리스트(숫자)에서 li의 j번째에 해당하는 값 그대로 출력
        print(li[j], end=' ')