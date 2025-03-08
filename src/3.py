import random

def get_random_math_problem():
    operation = random.choice(["+", "-", "*", "/"])
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    else:
        result = num1 / num2
    return f"{num1} {operation} {num2} = {result}"

def main():
    for i in range(3):
        print(get_random_math_problem())

if __name__ == "__main__":
    main()
