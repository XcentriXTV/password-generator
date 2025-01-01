import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

length = input('Password length?')
length = int(length)

for p in range(20): # Amend value produced
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
