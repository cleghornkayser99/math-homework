def get_random_math_problem(n):
    # Generate a random math problem
    x = randint(1, n)
    y = randint(1, n)
    op = choice(['+', '-', '*', '/'])
    if op == '+':
        return f"{x} {op} {y}"
    elif op == '-':
        return f"{x} - {y}"
    elif op == '*':
        return f"{x} * {y}"
    else:
        return f"{x} / {y}"
