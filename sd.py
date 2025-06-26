import math

def scientific_calculator():
    print("=== Scientific Calculator ===")
    print("Available operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Logarithm (log base 10)")
    print("6. Square (x²)")
    
    choice = input("Enter the operation symbol or name (e.g., +, -, log, square): ").lower()
    
    if choice in ['+', '-', '*', '/']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '+':
            result = num1 + num2
        elif choice == '-':
            result = num1 - num2
        elif choice == '*':
            result = num1 * num2
        elif choice == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero.")
                return
        
        print("Result:", result)

    elif choice == 'log':
        num = float(input("Enter a positive number: "))
        if num > 0:
            result = math.log10(num)
            print("Log base 10 of", num, "is", result)
        else:
            print("Error: Logarithm undefined for non-positive numbers.")
    
    elif choice == 'square':
        num = float(input("Enter a number: "))
        result = num ** 2
        print("Square of", num, "is", result)

    else:
        print("Invalid operation.")

scientific_calculator()
