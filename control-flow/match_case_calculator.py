# match Case Calculator
# ask the user to input number
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# ask the user to input the operation
operation = input("Enter operation (+, -, *, /): ")
# perform the operation using match-case
match operation:
    case "+":   
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is {result}.")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Error: Invalid operation.")