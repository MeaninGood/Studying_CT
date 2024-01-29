import sys
input = lambda: sys.stdin.readline().strip()

# 두 수의 합이 짝수면 무조건 가능
# 홀수일 땐.. -2한 값이 소수면 가능


tmpn = 2000010
sieve = [True for _ in range(tmpn)]
sieve[0], sieve[1] = False, False

for i in range(2, tmpn):
    if i * i > tmpn:
        break
    
    for j in range(i * 2, tmpn, i):
        sieve[j] = False

primes = []
for i in range(tmpn):
    if sieve[i]:
        primes.append(i)

t = int(input())
for tc in range(t):
    a, b = map(int, input().split())
    
    # 두 수의 합이 3이하면 무조건 소수로 나눌 수 없으니까 안 됨
    if a + b <= 3:
        print('NO')
    
    # 그 외에 두 수의 합이 짝수이면 가능
    elif (a + b) % 2 == 0:
        print('YES')
    
    # 두 수의 합이 홀수인 경우 -2를 하고 남는 애가 소수이면 가능
    else:
        tmp = a + b - 2
        
        # 남는 애가 0이거나 1이면 불가
        if tmp <= 1:
            print('NO')
            continue
        
        # 소수로 나눠지는지 판정
        flag = True
        for prime in primes:
            if prime * prime > tmp:
                break
            
            if tmp % prime == 0:
                flag = False
                break
        
        if flag:
            print('YES')
        
        else:
            print('NO')
            