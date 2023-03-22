# 0. 모듈러의 성질

# print(5 % 3)
#
# print((5 + 8) % 3)
# print((5 % 3 + 8 % 3) % 3)

# (a + b) % c == (a % c + b % c) % c
# (a * b) % c == (a % c * b % c) % c
# (a - b) % c == (a % c - b % c + 1000 * c) % c
# (a // b) % c == (a % c // b % c) % c  => 수학적으로는 되지만, 코딩할땐 안된다. 안된다고 생각하자. => 역원을 구하는 페르마 소정리 a^p % p == a
# 5 // 3 같이 안 나누어 떨어지는 것은 몫(1)만 취하기 때문에 안 된다
"""
더하기
n = a c + d
a 찾기 : //
d 찾기 : %

n // c = a
n % c = d

a = xc + y
b = wc + z
a + b = (x + w)c + y + z

뺴기
(a - b) % c == (a % c - b % c + 1000 * c) % c
(6 - 3) % 5 == 3
(6 % 5 - 3 % 5) % 5
(1 - 3) % 5 == 음수
(1 - 3 + 5) % 5 로 씀, 결과를 변화시키지 않기 위해. 사실상 0으로 인식되는 5의 배수
아무거나 넣어주면 됨

"""
# 파이썬을 제외하면 모두 자료형을 지정함.
# int => 21억
# long, long long => 21억*21억*2
# 파이썬도 기본적으로 21억*21억*2(그 이상은 느려진다.)
# 이 이상 처리는 자바 기준 BigInteger
# 10000000000000000000000000000 + 10000000000000000000000000000000000000000
# 그냥 정수 담듯 하는 게 아니라 문자열로 저장해서 따로 연산 과정을 거침(자바도 파이썬도)
# 커지면 연산이 되게 느려짐
# 문제에 따라 정말 큰 수를 연산해야 하는 경우가 종종 나옴
# 코딩테스트 기준으로 그런 큰 수를 진짜 출력하라고 하지는 않고, 아주 큰 소수인 십억칠 정도 1000000007로
# 로 나눈 나머지만 출력해라. 그게 같으면 정답으로 인정하겠다.

"""
1부터 1000000000의 합의 % 1000000007 출력
## 몰랐다면
total = 0
for i in range(1, 1000000000):
  total += i
  
print(total % 1000000007)

## 이제는
total = 0
for i in range(1, 1000000000):
  total += i
  total %= 1000000007

print(total)

정수의 범위를 계속 작은 상태에서만 연산하기 위해, 굳이 계속 큰 값 들고 있다가 마지막에 나누는 게 아니라

"""




# 1. 소수 판정 => 1 조심
# 자연수 하나를 입력 받아서 이 수가 소수면 YES, 소수가 아니면 NO를 출력한다.
# n제한이 일반적으로 10^12정도로 나온다.

# 12의 약수
# 1 2 3 4 6 12

# 쌍이 있다
# 1 12
# 2 6
# 3 4

# 왼쪽 <= 오른쪽     따라서 "왼쪽 수는 모두 루트n 이하"
# 왼쪽 x 오른쪽 n이 되어야 함.
# 1~루트n까지 약수가 정확히 하나인지 구한다.

"""
## 완전탐색으로 소수판정
n = int(input())
cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1

elif cnt == 2:
    print("YES")
else:
    print("NO")
    
# 근데 문제에서는 n 제한이 일반적으로 10^12정도로 나옴.
# 위의 코드로 불가능.
"""
n = int(input())

cnt = 0
for i in range(2, n + 1):
    if i * i > n:
        break

    if n % i == 0:
        cnt += 1

if n == 1:
    print("NO")
elif cnt == 1:
    print("YES")
else:
    print("NO")





# 2. 약수 구하기 => 제곱수를 조심.
# 약수의 개수가 홀수 <=> 제곱수

# n = int(input())
# prime = []
#
# for i in range(1, n + 1):
#     if i * i > n:
#         break
#
#     if n % i == 0:
#         prime.append(i)
#         if i * i != n:
#             prime.append(n // i)
#
# print(*prime)





# 3. 소인수 분해 => 계산하는 변수랑 i * i보다 작은지 판단할 변수를 따로 둬야 한다.

# n => a, b, c, d, e, f, g, h, i
# a * b * c * d * e * f * g * h * i => n

# n = int(input())
#
# x = n
# for i in range(2, n + 1):
#     if i * i > n:
#         break
#
#     while x % i == 0:
#         print(i)
#         x //= i
#
# if x != 1:
#     print(x)




# 4. 유클리드 호제법 => GCD(최대공약수)를 구할 수 있는데, 응용을 조금 하면 LCM(최소공배수)도 구할 수 있다.
# 목표 : 두 자연수 a, b가 주어질 때 이 둘의 최대공약수를 구한다.(log n)

# a, b = map(int, input().split())
#
# A, B = a, b
# while a % b != 0:
#     a, b = b, a % b
#
# print(b)            #최대공약수
# print(A * B // b)   #최소공배수




# 5. 에라토스테네스의 체
# 목표 : 1~n까지의 자연수 중 소수를 모두 출력한다.

# n = int(input())
# isPrime = [True for i in range(n + 1)]
#
# isPrime[0] = False
# isPrime[1] = False
# for i in range(2, n + 1):
#     if not isPrime[i]:
#         continue
#
#     for j in range(i * i, n + 1, i):
#         isPrime[j] = False
#
# print(*[i for i in range(n + 1) if isPrime[i]])

# 응용 : 2~n까지의 자연수 각각의 가장 작은 소인수 출력

# n = int(input())
# prime = [-1 for i in range(n + 1)]
#
# for i in range(2, n + 1):
#     if prime[i] != -1:
#         continue
#
#     prime[i] = i
#     for j in range(i * i, n + 1, i):
#         if prime[j] == -1:
#             prime[j] = i
#
# print(*prime[2:])



# 6. 빠른 거듭제곱
# 목표 : (n ** m) % 1000000007 (n <= 100, m <= 1,000,000,000,000,000,000) 빠르게 구하기


# def pows(n, m):
#     if m == 0:
#         return 1
#
#     ret = pows(n, m // 2)
#     ret *= ret
#     ret %= 1000000007
#
#     if m % 2 == 0:
#         return ret
#     else:
#         return (ret * n) % 1000000007
#
