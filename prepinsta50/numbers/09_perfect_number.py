"""
PrepInsta Problem 9: Perfect number operations
"""

def find_divisors(num):
    """
    Find all proper divisors of a number (excluding the number itself)
    
    Args:
        num (int): Number to find divisors for
    
    Returns:
        list: List of proper divisors
    """
    if num <= 1:
        return []
    
    divisors = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != 1 and i != num // i and num // i != num:
                divisors.append(num // i)
    
    return sorted(divisors)

def is_perfect_number(num):
    """
    Check if a number is a perfect number
    A perfect number is equal to the sum of its proper divisors
    
    Args:
        num (int): Number to check
    
    Returns:
        bool: True if perfect number, False otherwise
    """
    if num <= 1:
        return False
    
    divisors = find_divisors(num)
    return sum(divisors) == num

def find_perfect_numbers(limit):
    """
    Find all perfect numbers up to a given limit
    
    Args:
        limit (int): Upper limit to search
    
    Returns:
        list: List of perfect numbers up to limit
    """
    perfect_numbers = []
    for num in range(2, limit + 1):
        if is_perfect_number(num):
            perfect_numbers.append(num)
    return perfect_numbers

def perfect_number_breakdown(num):
    """
    Show the breakdown of perfect number calculation
    
    Args:
        num (int): Number to break down
    
    Returns:
        str: Breakdown string
    """
    if num <= 1:
        return f"{num} has no proper divisors"
    
    divisors = find_divisors(num)
    divisor_sum = sum(divisors)
    
    divisors_str = " + ".join(map(str, divisors))
    result = f"{num}: divisors = {divisors} = {divisors_str} = {divisor_sum}"
    
    if divisor_sum == num:
        result += " (Perfect)"
    elif divisor_sum > num:
        result += " (Abundant)"
    else:
        result += " (Deficient)"
    
    return result

def classify_number(num):
    """
    Classify a number as perfect, abundant, or deficient
    
    Args:
        num (int): Number to classify
    
    Returns:
        str: Classification of the number
    """
    if num <= 1:
        return "Neither"
    
    divisors = find_divisors(num)
    divisor_sum = sum(divisors)
    
    if divisor_sum == num:
        return "Perfect"
    elif divisor_sum > num:
        return "Abundant"
    else:
        return "Deficient"

def mersenne_perfect_numbers(limit):
    """
    Generate perfect numbers using Mersenne primes
    Perfect numbers have the form 2^(p-1) * (2^p - 1) where 2^p - 1 is prime
    
    Args:
        limit (int): Upper limit for search
    
    Returns:
        list: List of perfect numbers generated from Mersenne primes
    """
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    perfect_numbers = []
    p = 2
    
    while True:
        mersenne = (2 ** p) - 1
        if mersenne > limit:
            break
        
        if is_prime(mersenne):
            perfect_num = (2 ** (p - 1)) * mersenne
            if perfect_num <= limit:
                perfect_numbers.append(perfect_num)
            else:
                break
        
        p += 1
        if p > 50:  # Prevent infinite loop for very large limits
            break
    
    return perfect_numbers

def main():
    # Test perfect number checking
    print("Perfect number checking:")
    print("-" * 25)
    test_numbers = [1, 6, 12, 28, 30, 496, 8128, 100, 1000]
    
    for num in test_numbers:
        is_perfect = is_perfect_number(num)
        classification = classify_number(num)
        print(f"{num} is {classification.lower()} ({'perfect' if is_perfect else 'not perfect'})")
    
    # Show breakdown for some numbers
    print("\nNumber classifications with breakdowns:")
    print("-" * 45)
    breakdown_numbers = [6, 12, 28, 30, 100]
    
    for num in breakdown_numbers:
        breakdown = perfect_number_breakdown(num)
        print(breakdown)
    
    # Find perfect numbers up to different limits
    print("\nPerfect numbers up to different limits:")
    print("-" * 40)
    limits = [100, 1000, 10000]
    
    for limit in limits:
        perfect_nums = find_perfect_numbers(limit)
        print(f"Up to {limit}: {perfect_nums}")
    
    # Compare with Mersenne method
    print("\nPerfect numbers using Mersenne primes:")
    print("-" * 40)
    mersenne_perfect = mersenne_perfect_numbers(10000)
    print(f"Using Mersenne method: {mersenne_perfect}")
    
    # Classification statistics
    print("\nNumber classification statistics (1-100):")
    print("-" * 45)
    perfect_count = abundant_count = deficient_count = 0
    
    for num in range(1, 101):
        classification = classify_number(num)
        if classification == "Perfect":
            perfect_count += 1
        elif classification == "Abundant":
            abundant_count += 1
        elif classification == "Deficient":
            deficient_count += 1
    
    print(f"Perfect numbers: {perfect_count}")
    print(f"Abundant numbers: {abundant_count}")
    print(f"Deficient numbers: {deficient_count}")
    
    # Interactive input
    print("\nEnter a number to check if it's perfect (or 'quit' to exit):")
    while True:
        user_input = input("Number: ")
        if user_input.lower() == 'quit':
            break
        try:
            num = int(user_input)
            if num <= 0:
                print("Please enter a positive number!")
                continue
            
            is_perfect = is_perfect_number(num)
            classification = classify_number(num)
            breakdown = perfect_number_breakdown(num)
            
            print(f"{num} is a {classification.lower()} number")
            print(f"Breakdown: {breakdown}")
            
        except ValueError:
            print("Please enter a valid integer!")

if __name__ == "__main__":
    main()