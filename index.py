
#Password Generator

import random
import pyperclip

def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password_length = random.randint(8, 16)  # Random length between 8 and 16

    password = ''
    for _ in range(password_length):
        char = random.choice(characters)

        password+=char
    pyperclip.copy(password)  # Copy the password to clipboard
    return print(password)




print("Welcome to the Password Generator!")
print("This program will generate a random password for you.")
print("The password will contain a mix of uppercase, lowercase, numbers, and special characters.")
print("do you want to generate a password? (yes/no)")
user_input = input().strip().lower()
if user_input != 'yes':
    print("Exiting the program.")
    exit()
else:
    print("Generating a password...")
    generate_password()
print("The password has been copied to your clipboard!")




