def basic_calculator():
    while True:
        try:
            # Get user input for the first number or expression
            num1 = eval(input("Enter the first number or expression: "))
            if not isinstance(num1, (int, float)):
                raise ValueError("The result of the expression must be a number.")
            break  # Exit the loop if input is valid
        except (ValueError, SyntaxError):
            print("Invalid input. Please enter a valid number or expression.")

    while True:
        try:
            # Get user input for the second number or expression
            num2 = eval(input("Enter the second number or expression: "))
            if not isinstance(num2, (int, float)):
                raise ValueError("The result of the expression must be a number.")
            break  # Exit the loop if input is valid
        except (ValueError, SyntaxError):
            print("Invalid input. Please enter a valid number or expression.")

    # Get user input for the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the operation based on user input
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operation. Please enter +, -, *, or /.")

# Call the calculator function
basic_calculator()