"""
PrepInsta Problem 3: Sum of first N natural numbers
"""

def sum_natural_numbers_formula(n):
    """
    Calculate sum of first n natural numbers using formula: n*(n+1)/2
    
    Args:
        n (int): Number of natural numbers to sum
    
    Returns:
        int: Sum of first n natural numbers
    """
    return n * (n + 1) // 2

def sum_natural_numbers_loop(n):
    """
    Calculate sum of first n natural numbers using loop
    
    Args:
        n (int): Number of natural numbers to sum
    
    Returns:
        int: Sum of first n natural numbers
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_natural_numbers_recursive(n):
    """
    Calculate sum of first n natural numbers using recursion
    
    Args:
        n (int): Number of natural numbers to sum
    
    Returns:
        int: Sum of first n natural numbers
    """
    if n <= 1:
        return n
    return n + sum_natural_numbers_recursive(n - 1)

def main():
    # Test cases
    test_numbers = [5, 10, 100, 1, 0]
    
    print("Sum of first N natural numbers:")
    print("-" * 40)
    print(f"{'N':<5} {'Formula':<10} {'Loop':<10} {'Recursive':<10}")
    print("-" * 40)
    
    for n in test_numbers:
        if n >= 0:
            formula_result = sum_natural_numbers_formula(n)
            loop_result = sum_natural_numbers_loop(n)
            # Only use recursion for small numbers to avoid stack overflow
            recursive_result = sum_natural_numbers_recursive(n) if n <= 100 else "N/A"
            print(f"{n:<5} {formula_result:<10} {loop_result:<10} {recursive_result:<10}")
    
    # Interactive input
    print("\nEnter a number to calculate sum (or 'quit' to exit):")
    while True:
        user_input = input("N: ")
        if user_input.lower() == 'quit':
            break
        try:
            n = int(user_input)
            if n < 0:
                print("Please enter a non-negative number!")
                continue
            result = sum_natural_numbers_formula(n)
            print(f"Sum of first {n} natural numbers: {result}")
        except ValueError:
            print("Please enter a valid integer!")

if __name__ == "__main__":
    main()