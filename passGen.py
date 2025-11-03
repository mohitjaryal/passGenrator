# Password generator made with python
import random
import string

def passGen(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# User input
length = int(input("Enter password length: "))
print("Your password is:", passGen(length))