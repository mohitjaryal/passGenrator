# Password generator made with python
import random
import string

def passGen(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password


try:
    # User input
    length = int(input("Enter password length: "))
    if length < 4:
        print("Password length should be at least 4 characters.")
    else:
        print("Your password is:", passGen(length))
except ValueError:
    print("Please enter a valid number.")