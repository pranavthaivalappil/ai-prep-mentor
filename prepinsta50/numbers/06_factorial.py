"""
PrepInsta Problem 6: Factorial calculation
"""

import math

def factorial_iterative(n):
    """
    Calculate factorial using iterative approach
    
    Args:
        n (int): Number to calculate factorial for
    
    Returns:
        int: Factorial of n
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    """
    Calculate factorial using recursive approach
    
    Args:
        n (int): Number to calculate factorial for
    
    Returns:
        int: Factorial of n
    """
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_builtin(n):
    """
    Calculate factorial using built-in math.factorial
    
    Args:
        n (int): Number to calculate factorial for
    
    Returns:
        int: Factorial of n
    """
    if n < 0:
        return None
    return math.factorial(n)

def factorial_trailing_zeros(n):
    """
    Count trailing zeros in n!
    
    Args:
        n (int): Number to calculate factorial trailing zeros for
    
    Returns:
        int: Number of trailing zeros in n!
    """
    if n < 0:
        return 0
    
    count = 0
    power_of_5 = 5
    while power_of_5 <= n:
        count += n // power_of_5
        power_of_5 *= 5
    return count

def main():
    # Test factorial calculations
    print("Factorial calculations:")
    print("-" * 30)
    print(f"{'N':<5} {'Iterative':<15} {'Recursive':<15} {'Built-in':<15} {'Trailing 0s':<12}")
    print("-" * 70)
    
    test_numbers = [0, 1, 5, 10, 15, 20]
    
    for n in test_numbers:
        iter_result = factorial_iterative(n)
        # Only use recursion for small numbers to avoid stack overflow
        rec_result = factorial_recursive(n) if n <= 15 else "Stack limit"
        builtin_result = factorial_builtin(n)
        trailing_zeros = factorial_trailing_zeros(n)
        
        print(f"{n:<5} {iter_result:<15} {rec_result:<15} {builtin_result:<15} {trailing_zeros:<12}")
    
    # Test large numbers
    print("\nLarge factorial calculations:")
    print("-" * 35)
    large_numbers = [50, 100, 200]
    
    for n in large_numbers:
        result = factorial_iterative(n)
        trailing_zeros = factorial_trailing_zeros(n)
        print(f"{n}! has {len(str(result))} digits and {trailing_zeros} trailing zeros")
        print(f"First 50 digits: {str(result)[:50]}...")
        print()
    
    # Interactive input
    print("Enter a number to calculate factorial (or 'quit' to exit):")
    while True:
        user_input = input("Number: ")
        if user_input.lower() == 'quit':
            break
        try:
            n = int(user_input)
            if n < 0:
                print("Factorial is not defined for negative numbers!")
                continue
            if n > 1000:
                print("Number too large! Please enter a number <= 1000")
                continue
            
            result = factorial_iterative(n)
            trailing_zeros = factorial_trailing_zeros(n)
            print(f"{n}! = {result}")
            print(f"Trailing zeros: {trailing_zeros}")
            print(f"Number of digits: {len(str(result))}")
            
        except ValueError:
            print("Please enter a valid integer!")

if __name__ == "__main__":
    main()