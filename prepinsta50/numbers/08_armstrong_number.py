"""
PrepInsta Problem 8: Armstrong number operations
"""

def count_digits(num):
    """
    Count number of digits in a number
    
    Args:
        num (int): Number to count digits for
    
    Returns:
        int: Number of digits
    """
    return len(str(abs(num)))

def is_armstrong_number(num):
    """
    Check if a number is an Armstrong number
    An Armstrong number is equal to the sum of its digits raised to the power of number of digits
    
    Args:
        num (int): Number to check
    
    Returns:
        bool: True if Armstrong number, False otherwise
    """
    if num < 0:
        return False
    
    original_num = num
    num_digits = count_digits(num)
    digit_sum = 0
    
    while num > 0:
        digit = num % 10
        digit_sum += digit ** num_digits
        num //= 10
    
    return digit_sum == original_num

def find_armstrong_numbers_in_range(start, end):
    """
    Find all Armstrong numbers in a given range
    
    Args:
        start (int): Start of range (inclusive)
        end (int): End of range (inclusive)
    
    Returns:
        list: List of Armstrong numbers in range
    """
    armstrong_numbers = []
    for num in range(max(0, start), end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers

def generate_armstrong_numbers(limit):
    """
    Generate Armstrong numbers up to a given limit
    
    Args:
        limit (int): Upper limit
    
    Returns:
        list: List of Armstrong numbers up to limit
    """
    return find_armstrong_numbers_in_range(0, limit)

def armstrong_number_breakdown(num):
    """
    Show the breakdown of Armstrong number calculation
    
    Args:
        num (int): Number to break down
    
    Returns:
        str: Breakdown string
    """
    if num < 0:
        return "Negative numbers are not Armstrong numbers"
    
    original_num = num
    num_digits = count_digits(num)
    breakdown = []
    digit_sum = 0
    
    while num > 0:
        digit = num % 10
        power_result = digit ** num_digits
        breakdown.append(f"{digit}^{num_digits} = {power_result}")
        digit_sum += power_result
        num //= 10
    
    breakdown.reverse()  # Reverse to show digits in original order
    breakdown_str = " + ".join(breakdown)
    
    result = f"{original_num} = {breakdown_str} = {digit_sum}"
    is_armstrong = digit_sum == original_num
    result += f" ({'Armstrong' if is_armstrong else 'Not Armstrong'})"
    
    return result

def main():
    # Test Armstrong number checking
    print("Armstrong number checking:")
    print("-" * 30)
    test_numbers = [0, 1, 9, 153, 371, 407, 1634, 8208, 9474, 54748, 92727, 93084, 123, 456]
    
    for num in test_numbers:
        is_armstrong = is_armstrong_number(num)
        print(f"{num} is {'an Armstrong number' if is_armstrong else 'not an Armstrong number'}")
    
    # Show breakdown for some numbers
    print("\nArmstrong number breakdowns:")
    print("-" * 35)
    breakdown_numbers = [153, 371, 1634, 123]
    
    for num in breakdown_numbers:
        breakdown = armstrong_number_breakdown(num)
        print(breakdown)
    
    # Find Armstrong numbers in ranges
    print("\nArmstrong numbers in different ranges:")
    print("-" * 40)
    ranges = [(1, 100), (100, 1000), (1000, 10000)]
    
    for start, end in ranges:
        armstrong_nums = find_armstrong_numbers_in_range(start, end)
        print(f"Range {start}-{end}: {armstrong_nums}")
    
    # Generate first few Armstrong numbers
    print("\nFirst 20 Armstrong numbers:")
    print("-" * 30)
    armstrong_nums = generate_armstrong_numbers(100000)[:20]
    print(armstrong_nums)
    
    # Armstrong numbers by digit count
    print("\nArmstrong numbers by digit count:")
    print("-" * 35)
    digit_groups = {}
    
    for num in generate_armstrong_numbers(100000):
        digits = count_digits(num)
        if digits not in digit_groups:
            digit_groups[digits] = []
        digit_groups[digits].append(num)
    
    for digits in sorted(digit_groups.keys()):
        print(f"{digits} digits: {digit_groups[digits]}")
    
    # Interactive input
    print("\nEnter a number to check if it's Armstrong (or 'quit' to exit):")
    while True:
        user_input = input("Number: ")
        if user_input.lower() == 'quit':
            break
        try:
            num = int(user_input)
            is_armstrong = is_armstrong_number(num)
            breakdown = armstrong_number_breakdown(num)
            
            print(f"{num} is {'an Armstrong number' if is_armstrong else 'not an Armstrong number'}")
            print(f"Breakdown: {breakdown}")
            
        except ValueError:
            print("Please enter a valid integer!")

if __name__ == "__main__":
    main()