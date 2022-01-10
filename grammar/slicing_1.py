# 문자열 슬라이싱

N = list(map(int, input().split())) ## 34 234 53 20

print(N[1]) # 가능 ## 234 출력
print(N[1:]) # 가능 ## [234, 53, 2] 리스트로 출력
print(float(N[1])) # 가능 ## 234.0 출력
print(float(N[1:])) # 불가능!!!
print(sum(N[1:]/N[0])) # 가능
## TypeError : float() argument must be a string or a number, not 'list'