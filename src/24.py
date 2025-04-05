def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    else:
        return x / y

# Example usage
result1 = add_numbers(5, 3)
result2 = subtract_numbers(5, 3)

try:
    result3 = multiply_numbers(4, 2)
except ValueError as e:
    print(e)

result4 = divide_numbers(6, 0)  # This will raise a division by zero error
