"""
PrepInsta Recursion Problem 2: Calculate HCF (GCD) and LCM
"""

def hcf_recursive(a, b):
    """
    Calculate HCF (Highest Common Factor) using Euclidean algorithm recursively
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: HCF of a and b
    """
    # Base case
    if b == 0:
        return abs(a)
    
    # Recursive case
    return hcf_recursive(b, a % b)

def hcf_iterative(a, b):
    """
    Calculate HCF using Euclidean algorithm iteratively
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: HCF of a and b
    """
    a, b = abs(a), abs(b)
    
    while b != 0:
        a, b = b, a % b
    
    return a

def lcm_using_hcf(a, b):
    """
    Calculate LCM using the relationship: LCM(a,b) = (a*b) / HCF(a,b)
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: LCM of a and b
    """
    if a == 0 or b == 0:
        return 0
    
    hcf = hcf_recursive(a, b)
    return abs(a * b) // hcf

def hcf_multiple_numbers(numbers):
    """
    Calculate HCF of multiple numbers using recursion
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int: HCF of all numbers
    """
    if not numbers:
        return 0
    if len(numbers) == 1:
        return abs(numbers[0])
    if len(numbers) == 2:
        return hcf_recursive(numbers[0], numbers[1])
    
    # Recursive case: HCF(a, b, c, ...) = HCF(HCF(a, b), c, ...)
    return hcf_recursive(numbers[0], hcf_multiple_numbers(numbers[1:]))

def lcm_multiple_numbers(numbers):
    """
    Calculate LCM of multiple numbers using recursion
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        int: LCM of all numbers
    """
    if not numbers:
        return 0
    if len(numbers) == 1:
        return abs(numbers[0])
    if len(numbers) == 2:
        return lcm_using_hcf(numbers[0], numbers[1])
    
    # Recursive case: LCM(a, b, c, ...) = LCM(LCM(a, b), c, ...)
    return lcm_using_hcf(numbers[0], lcm_multiple_numbers(numbers[1:]))

def extended_euclidean(a, b):
    """
    Extended Euclidean algorithm to find HCF and coefficients
    Returns HCF and coefficients x, y such that ax + by = HCF(a, b)
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        tuple: (hcf, x, y) where ax + by = hcf
    """
    if b == 0:
        return abs(a), 1 if a >= 0 else -1, 0
    
    hcf, x1, y1 = extended_euclidean(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    return hcf, x, y

def are_coprime(a, b):
    """
    Check if two numbers are coprime (HCF = 1)
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        bool: True if coprime, False otherwise
    """
    return hcf_recursive(a, b) == 1

def find_coprime_pairs(numbers):
    """
    Find all coprime pairs in a list of numbers
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        list: List of coprime pairs
    """
    coprime_pairs = []
    
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if are_coprime(numbers[i], numbers[j]):
                coprime_pairs.append((numbers[i], numbers[j]))
    
    return coprime_pairs

def reduce_fraction(numerator, denominator):
    """
    Reduce a fraction to its simplest form using HCF
    
    Args:
        numerator (int): Numerator
        denominator (int): Denominator
    
    Returns:
        tuple: (reduced_numerator, reduced_denominator)
    """
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    
    hcf = hcf_recursive(numerator, denominator)
    return numerator // hcf, denominator // hcf

def solve_linear_diophantine(a, b, c):
    """
    Solve linear Diophantine equation ax + by = c
    
    Args:
        a (int): Coefficient of x
        b (int): Coefficient of y
        c (int): Constant term
    
    Returns:
        tuple or None: (x, y) solution if exists, None otherwise
    """
    hcf, x, y = extended_euclidean(a, b)
    
    if c % hcf != 0:
        return None  # No solution exists
    
    # Scale the solution
    scale = c // hcf
    return x * scale, y * scale

def hcf_using_subtraction(a, b):
    """
    Calculate HCF using subtraction method (slower but educational)
    
    Args:
        a (int): First number
        b (int): Second number
    
    Returns:
        int: HCF of a and b
    """
    a, b = abs(a), abs(b)
    
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    
    if a > b:
        return hcf_using_subtraction(a - b, b)
    else:
        return hcf_using_subtraction(a, b - a)

def main():
    # Test basic HCF and LCM calculations
    print("HCF and LCM calculations:")
    print("-" * 50)
    print(f"{'A':<6} {'B':<6} {'HCF (Rec)':<10} {'HCF (Iter)':<10} {'LCM':<10} {'Coprime':<8}")
    print("-" * 50)
    
    test_pairs = [
        (12, 18),
        (15, 25),
        (7, 13),
        (48, 18),
        (100, 75),
        (17, 19),
        (24, 36),
        (0, 5),
        (14, 28)
    ]
    
    for a, b in test_pairs:
        hcf_rec = hcf_recursive(a, b)
        hcf_iter = hcf_iterative(a, b)
        lcm = lcm_using_hcf(a, b)
        coprime = are_coprime(a, b)
        
        print(f"{a:<6} {b:<6} {hcf_rec:<10} {hcf_iter:<10} {lcm:<10} {'Yes' if coprime else 'No':<8}")
    
    # Test multiple numbers
    print("\nHCF and LCM of multiple numbers:")
    print("-" * 40)
    
    test_lists = [
        [12, 18, 24],
        [15, 25, 35],
        [8, 12, 16, 20],
        [7, 14, 21, 28],
        [5, 10, 15, 20, 25]
    ]
    
    for numbers in test_lists:
        hcf_multi = hcf_multiple_numbers(numbers)
        lcm_multi = lcm_multiple_numbers(numbers)
        
        print(f"Numbers: {numbers}")
        print(f"HCF: {hcf_multi}, LCM: {lcm_multi}")
        print()
    
    # Test extended Euclidean algorithm
    print("Extended Euclidean Algorithm:")
    print("-" * 35)
    
    extended_test_pairs = [
        (12, 18),
        (15, 25),
        (35, 15),
        (48, 18)
    ]
    
    for a, b in extended_test_pairs:
        hcf, x, y = extended_euclidean(a, b)
        verification = a * x + b * y
        
        print(f"For {a} and {b}:")
        print(f"  HCF = {hcf}")
        print(f"  Coefficients: x = {x}, y = {y}")
        print(f"  Verification: {a} × {x} + {b} × {y} = {verification}")
        print()
    
    # Test coprime pairs
    print("Coprime pairs analysis:")
    print("-" * 25)
    
    numbers_list = [6, 8, 9, 15, 21, 25]
    coprime_pairs = find_coprime_pairs(numbers_list)
    
    print(f"Numbers: {numbers_list}")
    print(f"Coprime pairs: {coprime_pairs}")
    
    # Test fraction reduction
    print("\nFraction reduction:")
    print("-" * 20)
    
    fractions = [
        (12, 18),
        (15, 25),
        (48, 64),
        (7, 13),
        (100, 150)
    ]
    
    for num, den in fractions:
        reduced_num, reduced_den = reduce_fraction(num, den)
        print(f"{num}/{den} = {reduced_num}/{reduced_den}")
    
    # Test linear Diophantine equations
    print("\nLinear Diophantine equations (ax + by = c):")
    print("-" * 45)
    
    diophantine_equations = [
        (3, 5, 1),
        (6, 9, 3),
        (4, 6, 5),
        (12, 18, 6),
        (7, 11, 1)
    ]
    
    for a, b, c in diophantine_equations:
        solution = solve_linear_diophantine(a, b, c)
        
        print(f"{a}x + {b}y = {c}")
        if solution:
            x, y = solution
            verification = a * x + b * y
            print(f"  Solution: x = {x}, y = {y}")
            print(f"  Verification: {a} × {x} + {b} × {y} = {verification}")
        else:
            print("  No integer solution exists")
        print()
    
    # Test subtraction method
    print("HCF using subtraction method:")
    print("-" * 30)
    
    subtraction_test_pairs = [
        (12, 8),
        (15, 10),
        (21, 14)
    ]
    
    for a, b in subtraction_test_pairs:
        hcf_sub = hcf_using_subtraction(a, b)
        hcf_euc = hcf_recursive(a, b)
        
        print(f"HCF({a}, {b}): Subtraction = {hcf_sub}, Euclidean = {hcf_euc}")
    
    # Performance comparison
    print("\nPerformance comparison (large numbers):")
    print("-" * 40)
    
    import time
    
    large_a, large_b = 123456789, 987654321
    
    # Recursive Euclidean
    start_time = time.time()
    result1 = hcf_recursive(large_a, large_b)
    time1 = time.time() - start_time
    
    # Iterative Euclidean
    start_time = time.time()
    result2 = hcf_iterative(large_a, large_b)
    time2 = time.time() - start_time
    
    print(f"Numbers: {large_a}, {large_b}")
    print(f"Recursive: {time1*1000:.4f} ms, Result: {result1}")
    print(f"Iterative: {time2*1000:.4f} ms, Result: {result2}")
    
    # Interactive input
    print("\nEnter two numbers to find HCF and LCM (or 'quit' to exit):")
    while True:
        user_input = input("Number1 Number2 (space-separated): ")
        if user_input.lower() == 'quit':
            break
        
        try:
            parts = user_input.split()
            if len(parts) != 2:
                print("Please enter exactly two numbers!")
                continue
            
            a = int(parts[0])
            b = int(parts[1])
            
            print(f"Analyzing {a} and {b}:")
            
            # Basic calculations
            hcf = hcf_recursive(a, b)
            lcm = lcm_using_hcf(a, b)
            coprime = are_coprime(a, b)
            
            print(f"HCF: {hcf}")
            print(f"LCM: {lcm}")
            print(f"Coprime: {'Yes' if coprime else 'No'}")
            
            # Extended Euclidean
            hcf_ext, x, y = extended_euclidean(a, b)
            print(f"Extended Euclidean: {a} × {x} + {b} × {y} = {hcf_ext}")
            
            # Fraction reduction
            if b != 0:
                reduced_num, reduced_den = reduce_fraction(a, b)
                print(f"Fraction {a}/{b} reduces to {reduced_num}/{reduced_den}")
            
            # Ask for more numbers
            more_input = input("Enter more numbers for multiple HCF/LCM (space-separated, or press Enter to skip): ")
            if more_input.strip():
                try:
                    more_numbers = [int(x) for x in more_input.split()]
                    all_numbers = [a, b] + more_numbers
                    
                    multi_hcf = hcf_multiple_numbers(all_numbers)
                    multi_lcm = lcm_multiple_numbers(all_numbers)
                    
                    print(f"HCF of {all_numbers}: {multi_hcf}")
                    print(f"LCM of {all_numbers}: {multi_lcm}")
                except ValueError:
                    print("Invalid numbers entered!")
            
        except ValueError:
            print("Please enter valid integers!")
        except Exception as e:
            print(f"Error: {e}")
        
        print()

if __name__ == "__main__":
    main()