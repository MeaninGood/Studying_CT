T = int(input())

number = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [input() for i in range(n)]
    arr2 = []

    for i in range(n):
        if '1' in arr[i]:
            arr2.append(arr[i])

    s = arr2[0]
    for i in range(m)[::-1]:
        if s[i] == '1':
            s = s[i - 55:i + 1]
            break

    num = []
    for i in range(0, 56, 7):
        for j in range(10):
            if s[i:i+7] == number[j]:
                num.append(j)
                break

    total = 0
    for i in range(8):
        if i % 2 == 0:
            total += 3 * num[i]
        else:
            total += num[i]

    if total % 10 == 0:
        print(f'#{tc} {sum(num)}')
        
    else:
        print(f'#{tc} 0')

