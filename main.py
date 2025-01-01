import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

length = input('Password length?')
length = int(length)

for p in range(10):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)