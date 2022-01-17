if x == 1 :
    print(a)
elif x == 2 :
    print(b)
elif x == 3 :
    print(c)
    


x = int(input())

arr = [0, 'a', 'b', 'c']

print(arr[x])




while True: # 해당 코드는 0 이 나올 때까지 반복한다.
    N = input() # 주소판으로 사용할 숫자 input

    if N == '0': # 0 이 나올 경우, 반복 종료
        break

    answer = len(N) + 1 # 간격은 양 옆 공백(2cm) 문자사이의 간격사이 (len(N)-1cm)

    if N[i] == '0': # 0 일 때, 4cm
        answer += 4
    if N[i] == '1': # 1 일 때, 2cm
        answer += 2
    else: # 그 외의 경우, 3cm
        answer += 3

    print(answer)
    
    
    
    
    # 배열화 하여, 해당 코드의 cm 를 index 접근한다.
arr = [4,2,3,3,3,3,3,3,3,3]

while True: # 해당 코드는 0 이 나올 때까지 반복한다.
    N = input() # 주소판으로 사용할 숫자 input

    if N == '0': # 0 이 나올 경우, 반복 종료
        break

    answer = len(N) + 1 # 간격은 양 옆 공백(2cm) 문자사이의 간격사이 (len(N)-1cm)

    for i in N: # 문자열을 한개씩 보면서, arr에 저장된 배열의 값을 answer 에 더해준다.
        answer += arr[int(i)]

    print(answer)