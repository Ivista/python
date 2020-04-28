import re

passwrdchck = re.compile(
    r'(?=.*[A-Z])(?=.*[a-z])(?=.*[^A-Za-z0-9])(?=.*\d).{8,}')

datacheck = input('Input string to test')

mo = passwrdchck.findall(datacheck)

if mo:
    print('Password is strong enough!')
else:
    print('Password is not strong enough')
