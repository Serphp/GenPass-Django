import random
import string


def generate_password(length=16, include_uppercase=True, include_numbers=True):
    chars = string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    password = "".join(random.choice(chars) for _ in range(length))
    return password
