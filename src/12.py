import random

def get_random_code():
    """Generates a random Python code."""
    # Initialize a list of operators
    operators = ["+", "-", "*", "/"]

    # Initialize a list of operands
    operands = [str(random.randint(1, 10)), str(random.randint(1, 10))]

    # Choose a random operator and an operand
    op = random.choice(operators)
    num1 = random.choice(operands)

    # Generate the code
    code = f"{num1} {op} {random.randint(1, 10)}"

    return code