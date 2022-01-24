# 1 이진수 출력하기

def recur(n) :
    if n == 0 :
        return ''
    
    return recur(n // 2) + str(n % 2)
    
print(recur(n))


# 2
def re(n) :
    return re(n//2) + re(n%2)

re(10)


# 3

def dec_to_bin(n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 종료 조건
    # 2로 나누는 것을 반복하면 마지막에는 1이 되므로 종료 조건은 다음과 같다
    if n == 1:
        return str(n)
    # n을 2로 나눈 나머지를 remainder에 담아두고
    else:
        remainder = n % 2
        # 나머지를 제외한 몫은 다시 n에 집어 넣자
        n = n // 2
        # 새로운 n을 다시 함수에 집어 넣고, 나머지를 더해주자
        return dec_to_bin(n) + str(remainder)

dec_to_bin(10)