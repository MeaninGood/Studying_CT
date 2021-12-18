# 1012번_8진수 2진수

## 8진수가 주어졌을 때, 2진수로 변환하는 프로그램 출력

oct_num = int(input(), 8)
bin_num = bin(oct_num)

print(bin_num[2:])