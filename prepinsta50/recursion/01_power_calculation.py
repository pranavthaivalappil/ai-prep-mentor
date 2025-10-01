"""
PrepInsta Recursion Problem 1: Calculate power of a number
"""

def power_recursive(base, exponent):
    """
    Calculate power using recursion
    
    Args:
        base (float): Base number
        exponent (int): Exponent
    
    Returns:
        float: base^exponent
    """
    # Base cases
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent < 0:
        return 1 / power_recursive(base, -exponent)
    
    # Recursive case
    return base * power_recursive(base, exponent - 1)

def power_recursive_optimized(base, exponent):
    """
    Calculate power using optimized recursion (divide and conquer)
    
    Args:
        base (float): Base number
        exponent (int): Exponent
    
    Returns:
        float: base^exponent
    """
    # Base cases
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent < 0:
        return 1 / power_recursive_optimized(base, -exponent)
    
    # Divide and conquer
    if exponent % 2 == 0:
        half_power = power_recursive_optimized(base, exponent // 2)
        return half_power * half_power
    else:
        return base * power_recursive_optimized(base, exponent - 1)

def power_iterative(base, exponent):
    """
    Calculate power using iteration
    
    Args:
        base (float): Base number
        exponent (int): Exponent
    
    Returns:
        float: base^exponent
    """
    if exponent == 0:
        return 1
    
    result = 1
    abs_exponent = abs(exponent)
    
    for _ in range(abs_exponent):
        result *= base
    
    return result if exponent > 0 else 1 / result

def power_builtin(base, exponent):
    """
    Calculate power using built-in pow() function
    
    Args:
        base (float): Base number
        exponent (int): Exponent
    
    Returns:
        float: base^exponent
    """
    return pow(base, exponent)

def power_with_modulo(base, exponent, modulo):
    """
    Calculate (base^exponent) % modulo efficiently
    
    Args:
        base (int): Base number
        exponent (int): Exponent
        modulo (int): Modulo value
    
    Returns:
        int: (base^exponent) % modulo
    """
    if exponent == 0:
        return 1 % modulo
    
    result = 1
    base = base % modulo
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulo
        exponent = exponent >> 1  # Divide by 2
        base = (base * base) % modulo
    
    return result

def power_of_two_check(n):
    """
    Check if a number is power of 2 using recursion
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if n is power of 2, False otherwise
    """
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    
    return power_of_two_check(n // 2)

def find_power_of_base(number, base):
    """
    Find what power of base equals the number
    
    Args:
        number (int): Target number
        base (int): Base
    
    Returns:
        int or None: Power if found, None otherwise
    """
    if number == 1:
        return 0
    if number < base:
        return None
    if number % base != 0:
        return None
    
    sub_power = find_power_of_base(number // base, base)
    return sub_power + 1 if sub_power is not None else None

def power_series_sum(x, n):
    """
    Calculate sum of power series: 1 + x + x^2 + x^3 + ... + x^n
    
    Args:
        x (float): Base value
        n (int): Maximum power
    
    Returns:
        float: Sum of power series
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    return power_recursive(x, n) + power_series_sum(x, n - 1)

def factorial_using_power_concept(n):
    """
    Calculate factorial using power concept (n! = n * (n-1)!)
    
    Args:
        n (int): Number to calculate factorial for
    
    Returns:
        int: Factorial of n
    """
    if n <= 1:
        return 1
    
    return n * factorial_using_power_concept(n - 1)

def main():
    # Test basic power calculations
    print("Power calculation methods:")
    print("-" * 60)
    print(f"{'Base':<6} {'Exp':<4} {'Recursive':<12} {'Optimized':<12} {'Iterative':<12} {'Built-in':<12}")
    print("-" * 60)
    
    test_cases = [
        (2, 3),
        (5, 4),
        (3, 0),
        (7, 1),
        (2, 10),
        (10, 3),
        (2, -3),
        (-2, 3),
        (-2, 4)
    ]
    
    for base, exp in test_cases:
        recursive_result = power_recursive(base, exp)
        optimized_result = power_recursive_optimized(base, exp)
        iterative_result = power_iterative(base, exp)
        builtin_result = power_builtin(base, exp)
        
        print(f"{base:<6} {exp:<4} {recursive_result:<12.3f} {optimized_result:<12.3f} {iterative_result:<12.3f} {builtin_result:<12.3f}")
    
    # Test large exponents (only optimized methods)
    print("\nLarge exponent calculations:")
    print("-" * 40)
    large_test_cases = [
        (2, 20),
        (3, 15),
        (5, 10),
        (10, 6)
    ]
    
    for base, exp in large_test_cases:
        optimized_result = power_recursive_optimized(base, exp)
        iterative_result = power_iterative(base, exp)
        builtin_result = power_builtin(base, exp)
        
        print(f"{base}^{exp} = {optimized_result} (optimized recursive)")
        print(f"{base}^{exp} = {iterative_result} (iterative)")
        print(f"{base}^{exp} = {builtin_result} (built-in)")
        print()
    
    # Test modular exponentiation
    print("Modular exponentiation:")
    print("-" * 30)
    mod_test_cases = [
        (2, 10, 1000),
        (3, 5, 7),
        (5, 3, 13),
        (2, 100, 1000000007)
    ]
    
    for base, exp, mod in mod_test_cases:
        result = power_with_modulo(base, exp, mod)
        print(f"({base}^{exp}) % {mod} = {result}")
    
    # Test power of 2 checking
    print("\nPower of 2 checking:")
    print("-" * 25)
    power_of_two_test = [1, 2, 3, 4, 8, 15, 16, 32, 33, 64, 100, 128]
    
    for num in power_of_two_test:
        is_power_of_two = power_of_two_check(num)
        print(f"{num} is {'a power of 2' if is_power_of_two else 'not a power of 2'}")
    
    # Test finding power
    print("\nFinding power of base:")
    print("-" * 25)
    find_power_test = [
        (8, 2),    # 2^3 = 8
        (27, 3),   # 3^3 = 27
        (125, 5),  # 5^3 = 125
        (100, 10), # 10^2 = 100
        (15, 3),   # Not a power of 3
        (1, 5)     # 5^0 = 1
    ]
    
    for number, base in find_power_test:
        power = find_power_of_base(number, base)
        if power is not None:
            print(f"{number} = {base}^{power}")
        else:
            print(f"{number} is not a power of {base}")
    
    # Test power series
    print("\nPower series sum (1 + x + x^2 + ... + x^n):")
    print("-" * 45)
    series_test_cases = [
        (2, 5),
        (0.5, 4),
        (3, 3),
        (1, 10)
    ]
    
    for x, n in series_test_cases:
        series_sum = power_series_sum(x, n)
        print(f"x={x}, n={n}: Sum = {series_sum:.4f}")
    
    # Performance comparison
    print("\nPerformance comparison (2^1000):")
    print("-" * 35)
    
    import time
    
    base, exp = 2, 1000
    
    # Optimized recursive
    start_time = time.time()
    result1 = power_recursive_optimized(base, exp)
    time1 = time.time() - start_time
    
    # Iterative
    start_time = time.time()
    result2 = power_iterative(base, exp)
    time2 = time.time() - start_time
    
    # Built-in
    start_time = time.time()
    result3 = power_builtin(base, exp)
    time3 = time.time() - start_time
    
    print(f"Optimized recursive: {time1*1000:.4f} ms")
    print(f"Iterative: {time2*1000:.4f} ms")
    print(f"Built-in: {time3*1000:.4f} ms")
    print(f"Result has {len(str(int(result1)))} digits")
    
    # Interactive input
    print("\nEnter base and exponent to calculate power (or 'quit' to exit):")
    while True:
        user_input = input("Base Exponent (space-separated): ")
        if user_input.lower() == 'quit':
            break
        
        try:
            parts = user_input.split()
            if len(parts) != 2:
                print("Please enter exactly two numbers!")
                continue
            
            base = float(parts[0])
            exponent = int(parts[1])
            
            print(f"Calculating {base}^{exponent}:")
            
            # Choose method based on exponent size
            if abs(exponent) <= 20:
                recursive_result = power_recursive(base, exponent)
                print(f"Recursive: {recursive_result}")
            
            optimized_result = power_recursive_optimized(base, exponent)
            iterative_result = power_iterative(base, exponent)
            builtin_result = power_builtin(base, exponent)
            
            print(f"Optimized recursive: {optimized_result}")
            print(f"Iterative: {iterative_result}")
            print(f"Built-in: {builtin_result}")
            
            # Additional operations
            if base > 0 and exponent > 0:
                # Check if result is power of 2
                if base == 2:
                    result_int = int(optimized_result)
                    is_power_of_two = power_of_two_check(result_int)
                    print(f"Result is power of 2: {is_power_of_two}")
                
                # Modular exponentiation
                if exponent >= 10:
                    mod = 1000000007
                    mod_result = power_with_modulo(int(base), exponent, mod)
                    print(f"Result mod {mod}: {mod_result}")
            
        except ValueError:
            print("Please enter valid numbers!")
        except Exception as e:
            print(f"Error: {e}")
        
        print()

if __name__ == "__main__":
    main()