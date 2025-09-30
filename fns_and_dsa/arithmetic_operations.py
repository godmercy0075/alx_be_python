# fns_and_dsa/arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation on two numbers.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float | str: The numeric result, or a string error message for invalid
                     operations or division by zero.
    """
    op = operation.strip().lower()

    if op == 'add':
        return num1 + num2
    elif op == 'subtract':
        return num1 - num2
    elif op == 'multiply':
        return num1 * num2
    elif op == 'divide':
        if num2 == 0:
            # Return a clear, printable message instead of crashing
            return "Error: division by zero"
        return num1 / num2
    else:
        return "Error: invalid operation"
