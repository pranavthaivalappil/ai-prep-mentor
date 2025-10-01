"""
PrepInsta Problem 7: Fibonacci series
"""

def fibonacci_iterative(n):
    """
    Generate first n Fibonacci numbers using iterative approach
    
    Args:
        n (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: First n Fibonacci numbers
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]
    
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    
    return fib_series

def fibonacci_recursive(n):
    """
    Calculate nth Fibonacci number using recursion
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
    
    Returns:
        int: nth Fibonacci number
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_memoized(n, memo={}):
    """
    Calculate nth Fibonacci number using memoization
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
        memo (dict): Memoization dictionary
    
    Returns:
        int: nth Fibonacci number
    """
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

def fibonacci_golden_ratio(n):
    """
    Calculate nth Fibonacci number using golden ratio formula (Binet's formula)
    
    Args:
        n (int): Position in Fibonacci sequence (0-indexed)
    
    Returns:
        int: nth Fibonacci number (approximate for large n)
    """
    import math
    
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    
    return int((phi**n - psi**n) / math.sqrt(5) + 0.5)

def is_fibonacci_number(num):
    """
    Check if a number is a Fibonacci number
    A number is Fibonacci if one of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    
    Args:
        num (int): Number to check
    
    Returns:
        bool: True if number is Fibonacci, False otherwise
    """
    import math
    
    def is_perfect_square(n):
        if n < 0:
            return False
        root = int(math.sqrt(n))
        return root * root == n
    
    return is_perfect_square(5 * num * num + 4) or is_perfect_square(5 * num * num - 4)

def main():
    # Test Fibonacci series generation
    print("Fibonacci series (first 15 numbers):")
    print("-" * 40)
    fib_series = fibonacci_iterative(15)
    print("Iterative:", fib_series)
    
    # Test individual Fibonacci numbers
    print("\nIndividual Fibonacci numbers:")
    print("-" * 35)
    print(f"{'Position':<10} {'Recursive':<12} {'Memoized':<12} {'Golden Ratio':<12}")
    print("-" * 50)
    
    for i in range(10):
        # Only use recursion for small numbers due to exponential time complexity
        rec_result = fibonacci_recursive(i) if i <= 20 else "Too slow"
        memo_result = fibonacci_memoized(i)
        golden_result = fibonacci_golden_ratio(i)
        
        print(f"{i:<10} {rec_result:<12} {memo_result:<12} {golden_result:<12}")
    
    # Test large Fibonacci numbers
    print("\nLarge Fibonacci numbers:")
    print("-" * 30)
    large_positions = [50, 100, 200]
    
    for pos in large_positions:
        fib_num = fibonacci_memoized(pos)
        print(f"F({pos}) has {len(str(fib_num))} digits")
        print(f"First 50 digits: {str(fib_num)[:50]}...")
        print()
    
    # Test Fibonacci number checking
    print("Checking if numbers are Fibonacci:")
    print("-" * 35)
    test_numbers = [0, 1, 2, 3, 4, 5, 8, 13, 21, 22, 34, 55, 100]
    
    for num in test_numbers:
        is_fib = is_fibonacci_number(num)
        print(f"{num} is {'a Fibonacci number' if is_fib else 'not a Fibonacci number'}")
    
    # Interactive input
    print("\nEnter number of Fibonacci numbers to generate (or 'quit' to exit):")
    while True:
        user_input = input("Count: ")
        if user_input.lower() == 'quit':
            break
        try:
            n = int(user_input)
            if n <= 0:
                print("Please enter a positive number!")
                continue
            if n > 100:
                print("Number too large! Please enter a number <= 100")
                continue
            
            fib_series = fibonacci_iterative(n)
            print(f"First {n} Fibonacci numbers:")
            print(fib_series)
            
        except ValueError:
            print("Please enter a valid integer!")

if __name__ == "__main__":
    main()