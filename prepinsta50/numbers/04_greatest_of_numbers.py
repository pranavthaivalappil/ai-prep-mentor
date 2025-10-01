"""
PrepInsta Problem 4: Find greatest of two or three numbers
"""

def greatest_of_two(a, b):
    """
    Find the greatest of two numbers
    
    Args:
        a, b: Numbers to compare
    
    Returns:
        The greater number
    """
    return a if a > b else b

def greatest_of_three(a, b, c):
    """
    Find the greatest of three numbers
    
    Args:
        a, b, c: Numbers to compare
    
    Returns:
        The greatest number
    """
    return max(a, b, c)

def greatest_of_three_without_max(a, b, c):
    """
    Find the greatest of three numbers without using max()
    
    Args:
        a, b, c: Numbers to compare
    
    Returns:
        The greatest number
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def greatest_of_list(numbers):
    """
    Find the greatest number in a list
    
    Args:
        numbers (list): List of numbers
    
    Returns:
        The greatest number
    """
    if not numbers:
        return None
    
    greatest = numbers[0]
    for num in numbers[1:]:
        if num > greatest:
            greatest = num
    return greatest

def main():
    # Test cases for two numbers
    print("Greatest of two numbers:")
    print("-" * 30)
    test_pairs = [(5, 3), (10, 15), (-2, -8), (0, 0)]
    
    for a, b in test_pairs:
        result = greatest_of_two(a, b)
        print(f"Greatest of {a} and {b}: {result}")
    
    # Test cases for three numbers
    print("\nGreatest of three numbers:")
    print("-" * 30)
    test_triplets = [(5, 3, 8), (10, 15, 12), (-2, -8, -1), (7, 7, 7)]
    
    for a, b, c in test_triplets:
        result1 = greatest_of_three(a, b, c)
        result2 = greatest_of_three_without_max(a, b, c)
        print(f"Greatest of {a}, {b}, {c}: {result1} (using max: {result2})")
    
    # Test cases for list of numbers
    print("\nGreatest in list:")
    print("-" * 20)
    test_lists = [[1, 5, 3, 9, 2], [-1, -5, -2], [42], []]
    
    for lst in test_lists:
        result = greatest_of_list(lst)
        print(f"Greatest in {lst}: {result}")
    
    # Interactive input
    print("\nEnter numbers separated by spaces (or 'quit' to exit):")
    while True:
        user_input = input("Numbers: ")
        if user_input.lower() == 'quit':
            break
        try:
            numbers = [float(x) for x in user_input.split()]
            if len(numbers) == 0:
                print("Please enter at least one number!")
            elif len(numbers) == 1:
                print(f"Only one number: {numbers[0]}")
            elif len(numbers) == 2:
                result = greatest_of_two(numbers[0], numbers[1])
                print(f"Greatest of two: {result}")
            elif len(numbers) == 3:
                result = greatest_of_three(numbers[0], numbers[1], numbers[2])
                print(f"Greatest of three: {result}")
            else:
                result = greatest_of_list(numbers)
                print(f"Greatest in list: {result}")
        except ValueError:
            print("Please enter valid numbers!")

if __name__ == "__main__":
    main()