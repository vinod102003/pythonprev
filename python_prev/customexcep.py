class MyCustomException(Exception):
    def __init__(self, message="This is a custom exception"):
        self.message = message
        super().__init__(self.message)

def divide(x, y):
    if y == 0:
        raise MyCustomException("Division by zero is not allowed")
    else:
        return x / y

try:
    # Example usage of the divide function
    result = divide(10, 0)
    print("Result of division:", result)
except MyCustomException as e:
    print("An error occurred:", e)
