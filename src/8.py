import random
def get_random_code():
    # Generate a random number between 1 and 50
    num = random.randint(1, 50)

    # Check if the number is even or odd
    if num % 2 == 0:
        # If it's even, return "Even"
        return "Even"
    else:
        # If it's odd, return "Odd"
        return "Odd"

get_random_code()