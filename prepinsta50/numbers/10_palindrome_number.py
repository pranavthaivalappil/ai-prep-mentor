"""
PrepInsta Problem 10: Palindrome number operations
"""

def is_palindrome_number(num):
    """
    Check if a number is a palindrome
    
    Args:
        num (int): Number to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Convert to string and compare with reverse
    num_str = str(abs(num))  # Use absolute value to handle negative numbers
    return num_str == num_str[::-1]

def is_palindrome_number_mathematical(num):
    """
    Check if a number is a palindrome using mathematical operations
    
    Args:
        num (int): Number to check
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    if num < 0:
        return False  # Negative numbers are not palindromes
    
    original_num = num
    reversed_num = 0
    
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    return original_num == reversed_num

def reverse_number(num):
    """
    Reverse the digits of a number
    
    Args:
        num (int): Number to reverse
    
    Returns:
        int: Reversed number
    """
    is_negative = num < 0
    num = abs(num)
    
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    return -reversed_num if is_negative else reversed_num

def find_palindromes_in_range(start, end):
    """
    Find all palindrome numbers in a given range
    
    Args:
        start (int): Start of range (inclusive)
        end (int): End of range (inclusive)
    
    Returns:
        list: List of palindrome numbers in range
    """
    palindromes = []
    for num in range(start, end + 1):
        if is_palindrome_number(num):
            palindromes.append(num)
    return palindromes

def next_palindrome(num):
    """
    Find the next palindrome number greater than given number
    
    Args:
        num (int): Starting number
    
    Returns:
        int: Next palindrome number
    """
    num += 1
    while not is_palindrome_number(num):
        num += 1
    return num

def previous_palindrome(num):
    """
    Find the previous palindrome number less than given number
    
    Args:
        num (int): Starting number
    
    Returns:
        int: Previous palindrome number (None if no positive palindrome exists)
    """
    num -= 1
    while num >= 0 and not is_palindrome_number(num):
        num -= 1
    return num if num >= 0 else None

def palindrome_by_digit_count(digits):
    """
    Generate all palindromes with given number of digits
    
    Args:
        digits (int): Number of digits
    
    Returns:
        list: List of palindromes with specified digit count
    """
    if digits <= 0:
        return []
    if digits == 1:
        return list(range(0, 10))
    
    palindromes = []
    start = 10 ** (digits - 1)
    end = 10 ** digits - 1
    
    for num in range(start, end + 1):
        if is_palindrome_number(num):
            palindromes.append(num)
    
    return palindromes

def is_lychrel_number(num, max_iterations=50):
    """
    Check if a number might be a Lychrel number
    A Lychrel number never forms a palindrome through the reverse-and-add process
    
    Args:
        num (int): Number to check
        max_iterations (int): Maximum iterations to try
    
    Returns:
        tuple: (is_lychrel, iterations, final_number)
    """
    current = num
    for i in range(max_iterations):
        reversed_num = reverse_number(current)
        current += reversed_num
        if is_palindrome_number(current):
            return (False, i + 1, current)
    
    return (True, max_iterations, current)  # Might be Lychrel

def main():
    # Test palindrome checking
    print("Palindrome number checking:")
    print("-" * 30)
    test_numbers = [0, 1, 11, 121, 123, 1221, 12321, -121, 1234321]
    
    for num in test_numbers:
        is_pal_str = is_palindrome_number(num)
        is_pal_math = is_palindrome_number_mathematical(num)
        reversed_num = reverse_number(num)
        
        print(f"{num}: String method = {is_pal_str}, Math method = {is_pal_math}, Reversed = {reversed_num}")
    
    # Find palindromes in ranges
    print("\nPalindromes in different ranges:")
    print("-" * 35)
    ranges = [(1, 20), (100, 200), (1000, 1100)]
    
    for start, end in ranges:
        palindromes = find_palindromes_in_range(start, end)
        print(f"Range {start}-{end}: {palindromes}")
    
    # Palindromes by digit count
    print("\nPalindromes by digit count:")
    print("-" * 30)
    for digits in range(1, 5):
        palindromes = palindrome_by_digit_count(digits)
        count = len(palindromes)
        if count <= 20:
            print(f"{digits} digits ({count} total): {palindromes}")
        else:
            print(f"{digits} digits ({count} total): {palindromes[:10]} ... {palindromes[-10:]}")
    
    # Next and previous palindromes
    print("\nNext and previous palindromes:")
    print("-" * 35)
    test_nums = [50, 100, 500, 1000]
    
    for num in test_nums:
        next_pal = next_palindrome(num)
        prev_pal = previous_palindrome(num)
        print(f"Number: {num}, Next: {next_pal}, Previous: {prev_pal}")
    
    # Lychrel number testing
    print("\nLychrel number testing:")
    print("-" * 25)
    lychrel_candidates = [47, 89, 196, 295, 394]
    
    for num in lychrel_candidates:
        is_lychrel, iterations, final_num = is_lychrel_number(num)
        if is_lychrel:
            print(f"{num}: Possibly Lychrel (no palindrome after {iterations} iterations)")
        else:
            print(f"{num}: Not Lychrel (palindrome {final_num} after {iterations} iterations)")
    
    # Interactive input
    print("\nEnter a number to check if it's palindrome (or 'quit' to exit):")
    while True:
        user_input = input("Number: ")
        if user_input.lower() == 'quit':
            break
        try:
            num = int(user_input)
            is_palindrome = is_palindrome_number(num)
            reversed_num = reverse_number(num)
            
            print(f"{num} is {'a palindrome' if is_palindrome else 'not a palindrome'}")
            print(f"Reversed: {reversed_num}")
            
            if not is_palindrome:
                next_pal = next_palindrome(num)
                prev_pal = previous_palindrome(num)
                print(f"Next palindrome: {next_pal}")
                if prev_pal is not None:
                    print(f"Previous palindrome: {prev_pal}")
            
        except ValueError:
            print("Please enter a valid integer!")

if __name__ == "__main__":
    main()