def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def main():
    # Read the number of values
    n = int(input("Enter the number of values: "))
    
    # Initialize the list to hold the values
    values = []
    
    # Read the values into the list
    for _ in range(n):
        value = int(input("Enter a value: "))
        values.append(value)
    
    # Initialize lists for prime and non-prime numbers
    prime_numbers = []
    non_prime_numbers = []
    
    # Separate the values into prime and non-prime lists
    for value in values:
        if is_prime(value):
            prime_numbers.append(value)
        else:
            non_prime_numbers.append(value)
    
    # Print the prime and non-prime lists
    print("Prime numbers:", prime_numbers)
    print("Non-prime numbers:", non_prime_numbers)

if __name__ == "__main__":
    main()
