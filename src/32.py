def find_max_value(numbers):
    """
    Find the maximum value in a list of numbers.
    
    Args:
        numbers: A list of integers.
        
    Returns:
        The maximum value found in the list. If there are no elements,
        return None (to simulate an empty list).
    """
    if not numbers:
        return None
    else:
        return max(numbers)
