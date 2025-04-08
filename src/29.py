def calculate_area(length, width):
    area = length * width
    return area

def main():
    # Input parameters
    l = float(input("Enter the length: "))
    w = float(input("Enter the width: "))

    # Calculate area
    area = calculate_area(l, w)
    
    # Output result
    print(f"The area is {area:.2f} square units.")

if __name__ == "__main__":
    main()
