"""
PrepInsta Problem 2: Check if a number is even or odd
"""

def check_even_odd(num):
    """
    Check if a number is even or odd
    
    Args:
        num (int): The number to check
    
    Returns:
        str: "Even" or "Odd"
    """
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    # Test cases
    test_numbers = [2, 3, 10, 15, 0, -4, -7]
    
    print("Checking if numbers are even or odd:")
    print("-" * 35)
    
    for num in test_numbers:
        result = check_even_odd(num)
        print(f"{num} is {result}")
    
    # Interactive input
    print("\nEnter a number to check (or 'quit' to exit):")
    while True:
        user_input = input("Number: ")
        if user_input.lower() == 'quit':
            break
        try:
            num = int(user_input)
            result = check_even_odd(num)
            print(f"{num} is {result}")
        except ValueError:
            print("Please enter a valid integer!")

if __name__ == "__main__":
    main()