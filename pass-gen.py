# Password generator program based on code publshed in "Build 24 Ethical Hacking Scripts & Tools with Python" book

from argparse import ArgumentParser
import secrets
import random
import string

# lists of characters to generate password
low_ch = list(string.ascii_lowercase)
up_ch = list(string.ascii_uppercase)
digits = list(string.digits)
special_characters = list("!#$%&'*+‑/")
characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "!#$%&'*+‑/")


def generate_random_password():
    ## length of password from the user
    pass_length = int(input("Enter password length: "))

    ## number of character types
    char_count = int(input("Enter alphabets count in password: "))
    digits_count = int(input("Enter number of digits in password: "))
    specials_count = int(input("Enter number of special characters n password: "))

    char_count = char_count + digits_count + specials_count

    ## check the total length with characters sum count
    ## print not valid if the sum is greater than length
    if char_count > pass_length:
        print("Characters total count is greater than the password length")
        return
