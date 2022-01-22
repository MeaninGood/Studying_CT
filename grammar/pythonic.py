# 특정 내용이 맞는지 확인해야 하는 로직을 만들어야 한다...!
# 하지만 그 내용이 하나가 아니라 여러개다...!!
# 괜찮아 나에겐 in 연산자가 있으니까!!!
vowel = ['a', 'e', 'i', 'o', 'u']
word = 'apple'

for char in word:
    if char in vowel:
        print(f'{char} is {word}`s vowel!!')

>>> a is apple`s vowel!!
>>> e is apple`s vowel!!