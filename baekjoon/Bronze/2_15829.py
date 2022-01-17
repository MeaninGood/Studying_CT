# 15829번_hashing

## r = 31(소수), M = 1234567891
## 문자열의 해시값 계산


# 아직은 깊게 팔 필요 없을 듯해서 구글링 후 개념만 이해하고 쓰루합니다

# 1. 아스키 코드 값을 ord로 반환

L = int(input())
string = input()
answer = 0

for i in range(L):
    answer += (ord(string[i])-96) * (31 ** i)
print(answer % 1234567891)


# 2. 알파벳 다 적어놓고 딕셔너리로 find 하기
apb = "abcdefghijklmnopqrstuvwxyz"
sum = 0
N = int(input())
string=list(input())
# print(string)
for idx, char in enumerate(string):
    sum += (apb.find(char)+1)*(31**idx)
print(sum % 1234567891)