import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def length_password():
    length = int(input("Enter password length : "))
    if length < 6:
      print("password length should be at least 6 characters.")
    else:
       pwd = generate_password(length)
       print("Genrated password:" , pwd)

length_password()

