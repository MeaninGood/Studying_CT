'''
<진법 변환>

1. 2진수 = 0bn / 10진수 -> 2진수 bin(n)
2. 8진수 = 0on / 10진수 -> 8진수 oct(n)
3. 16진수 = 0xn / 10진수 -> 16진수 hex(n)

==> box (2 -> 8 -> 10)

'''




'''
<비트 연산>

1. AND ( & )
>>> bin(0b1 & 0b1)
'0b1'
>>> bin(0b1 & 0b0)
'0b0'
>>> bin(0b0 & 0b1)
'0b0'
>>> bin(0b0 & 0b0)
'0b0'

2. OR ( | )
>>> bin(0b1 | 0b1)
'0b1'
>>> bin(0b1 | 0b0)
'0b1'
>>> bin(0b0 | 0b1)
'0b1'
>>> bin(0b0 | 0b0)
'0b0'

3. NOT ( ~ ) ## 원래 수에 - 기호 붙인 뒤 1뺀 값
>>> bin(~0b1)
'-0b10'


# 결과 값 같음
>>> bin(~0b0)
'-0b1'
>>> bin(-0b0 - 0b1)
'-0b1'


4. XOR ( ^ )
>>> bin(0b1 ^ 0b1)
'0b0'
>>> bin(0b1 ^ 0b0)
'0b1'
>>> bin(0b0 ^ 0b1)
'0b1'
>>> bin(0b0 ^ 0b0)
'0b0'


5. 네 자리 이진수의 비트 연산
# &
>>> bin(0b1111 & 0b1100)
'0b1100'
>>> bin(0b1010 & 0b1100)
'0b1000'

# |
>>> bin(0b1111 | 0b1100)
'0b1111'
>>> bin(0b1010 | 0b1100)
'0b1110'

# ~
>>> bin(~0b1100)
'-0b1101'
>>> bin(~0b1001)
'-0b1010'

# ^
>>> bin(0b1111 ^ 0b1100)
'0b11'
>>> bin(0b1010 ^ 0b1100)
'0b110'

'''

