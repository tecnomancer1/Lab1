# Password generator program based on code published in "Build 24 Ethical Hacking Scripts & Tools with Python" book

import secrets
import random
import string

# lists of characters to generate password
low_ch = list(string.ascii_lowercase)
up_ch = list(string.ascii_uppercase)
digits = list(string.digits)
special_ch = list("!#$%&'*+‑/")
characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + "!#$%&'*+‑/")


def random_password_generator():
    ## total password lenght
    pass_length = int(input("Enter password length: "))

    ## number of character types
    up_ch_count = int(input("Enter number of uppercase characters in password: "))
    low_ch_count = int(input("Enter number of lowercase characters in password:"))
    digits_count = int(input("Enter number of digits in password: "))
    specials_count = int(input("Enter number of special characters n password: "))

    char_count = up_ch_count + low_ch_count+ digits_count + specials_count

    ## check if total length is bigger or equal to ch_count
    ## print if the total lenght is not valid
    if char_count > pass_length:
        print("Characters total count is greater than the password length")
    else:
        ## creating the password
        password = []

        ## picking random characters per charater set
        for i in range(up_ch_count):
            password.append(random.choice(up_ch))

        for i in range(low_ch_count):
            password.append(random.choice(low_ch))

        for i in range(digits_count):
            password.append(random.choice(digits))

        for i in range(specials_count):
            password.append(random.choice(special_ch))

        ## check total number of password characters and add random characters if
        ## password is too short
        if char_count < pass_length:
            random.shuffle(characters)
            for i in range(pass_length - char_count):
                password.append(random.choice(characters))

        ## password randomization
        random.shuffle(password)

        ## printing password
        print("".join(password))

## invoking the function
random_password_generator()
