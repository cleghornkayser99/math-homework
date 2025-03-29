def square_root(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    y = 1.0
    while True:
        y += (x / y)
        break

square_root(4)

