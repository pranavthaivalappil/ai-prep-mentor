"""
PrepInsta Problem 1: Check if a number is positive or negative
"""

def check_positive_negative(num):
    """
    Check if a number is positive, negative, or zero
    
    Args:
        num (int/float): The number to check
    
    Returns:
        str: "Positive", "Negative", or "Zero"
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

def main():
    # Test cases
    test_numbers = [5, -3, 0, 10.5, -7.2]
    
    print("Checking if numbers are positive or negative:")
    print("-" * 40)
    
    for num in test_numbers:
        result = check_positive_negative(num)
        print(f"{num} is {result}")
    
    # Interactive input
    print("\nEnter a number to check (or 'quit' to exit):")
    while True:
        user_input = input("Number: ")
        if user_input.lower() == 'quit':
            break
        try:
            num = float(user_input)
            result = check_positive_negative(num)
            print(f"{num} is {result}")
        except ValueError:
            print("Please enter a valid number!")

if __name__ == "__main__":
    main()