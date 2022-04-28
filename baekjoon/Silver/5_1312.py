import sys
input = sys.stdin.readline

a, b, n = map(int, input().split())

a %= b # 처음에 a를 b로 나눠준다. (1의 자리수)
# n - 1 반복을 통해 나눗셈을 구현 (우리가 흔히 하는 나눗셈 방식 그대로 구현한 것)
for _ in range(n - 1):
    a = (a * 10) % b

res = (a * 10) // b # 마지막 나눗셈의 몫을 출력(n의 자리수)
print(res)