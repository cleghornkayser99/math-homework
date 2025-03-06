import random

def get_random_code(length=10):
    char = string.ascii_letters + string.digits
    return ''.join(random.choice(char) for _ in range(length))