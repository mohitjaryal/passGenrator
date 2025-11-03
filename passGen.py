# Password generator made with python
import random
import string

def passGen(length):
    int(input('Enter password length'))
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# U