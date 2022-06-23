import string

print(string.ascii_letters)
#소문자 대문자 52개
#출력 : abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.ascii_uppercase)
#대문자 26개
#출력 : ABCDEFGHIJKLMNOPQRSTUVWXYZ

print(string.ascii_lowercase)
#소문자 26개
#출력 : abcdefghijklmnopqrstuvwxyz

import string

alph = [i for i in string.ascii_letters]
print(alph)
#출력 : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
#        'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
#        'W', 'X', 'Y', 'Z']

upper = [i for i in string.ascii_uppercase]
print(upper)
#출력 : ['A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
#        'Q', 'R', 'S', 'T', 'U', 'V','W', 'X', 'Y', 'Z']

lower = [i for i in string.ascii_lowercase]
print(lower)
#출력 : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
#        'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lower = lower.upper()
print(lower)


asd = list(string.ascii_letters)
print(asd)


