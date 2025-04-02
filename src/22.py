def add_numbers(a, b):
    """
    Add two numbers.
    
    Parameters:
    a (int/float): The first number to be added.
    b (int/float): The second number to be added.
    
    Returns:
    int/float: The sum of the two numbers.
    """
    return a + b

def subtract_numbers(a, b):
    """
    Subtract two numbers.
    
    Parameters:
    a (int/float): The first number from which another is subtracted.
    b (int/float): The second number to be subtracted from the first.
    
    Returns:
    int/float: The difference between the two numbers.
    """
    return a - b

def multiply_numbers(a, b):
    """
    Multiply two numbers.
    
    Parameters:
    a (int/float): The first number to be multiplied.
    b (int/float): The second number to be multiplied by.
    
    Returns:
    int/float: The product of the two numbers.
    """
    return a * b

def divide_numbers(a, b):
    """
    Divide two numbers with remainder.
    
    Parameters:
    a (int/float): The numerator.
    b (int/float): The denominator.
    
    Returns:
    int/float: The quotient and the remainder of the division.
    """
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b
