# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def main():
    print("Simple Calculator")
    print("Operations: ")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    try:
        # Input numbers
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Input operation
        print("\nChoose an operation:")
        operation = input("Enter +, -, *, or /: ")

        # Perform calculation based on the operation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation! Please enter a valid operator (+, -, *, /).")
            return

        # Display the result
        print(f"\nThe result is: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()
