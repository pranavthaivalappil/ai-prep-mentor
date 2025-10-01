"""
PrepInsta String Problem 5: ASCII values and character operations
"""

def get_ascii_value(char):
    """
    Get ASCII value of a character
    
    Args:
        char (str): Single character
    
    Returns:
        int: ASCII value of the character
    """
    return ord(char)

def get_character_from_ascii(ascii_val):
    """
    Get character from ASCII value
    
    Args:
        ascii_val (int): ASCII value
    
    Returns:
        str: Character corresponding to ASCII value
    """
    try:
        return chr(ascii_val)
    except ValueError:
        return None

def string_to_ascii_list(s):
    """
    Convert string to list of ASCII values
    
    Args:
        s (str): Input string
    
    Returns:
        list: List of ASCII values
    """
    return [ord(char) for char in s]

def ascii_list_to_string(ascii_list):
    """
    Convert list of ASCII values to string
    
    Args:
        ascii_list (list): List of ASCII values
    
    Returns:
        str: String formed from ASCII values
    """
    try:
        return ''.join(chr(val) for val in ascii_list)
    except ValueError:
        return None

def sum_of_ascii_values(s):
    """
    Calculate sum of ASCII values in string
    
    Args:
        s (str): Input string
    
    Returns:
        int: Sum of ASCII values
    """
    return sum(ord(char) for char in s)

def average_ascii_value(s):
    """
    Calculate average ASCII value in string
    
    Args:
        s (str): Input string
    
    Returns:
        float: Average ASCII value (None if empty string)
    """
    if not s:
        return None
    return sum_of_ascii_values(s) / len(s)

def find_ascii_range(s):
    """
    Find minimum and maximum ASCII values in string
    
    Args:
        s (str): Input string
    
    Returns:
        tuple: (min_ascii, max_ascii, min_char, max_char)
    """
    if not s:
        return None, None, None, None
    
    ascii_values = [ord(char) for char in s]
    min_ascii = min(ascii_values)
    max_ascii = max(ascii_values)
    min_char = chr(min_ascii)
    max_char = chr(max_ascii)
    
    return min_ascii, max_ascii, min_char, max_char

def ascii_frequency_analysis(s):
    """
    Analyze frequency of ASCII values in string
    
    Args:
        s (str): Input string
    
    Returns:
        dict: Dictionary with ASCII value frequencies
    """
    frequency = {}
    
    for char in s:
        ascii_val = ord(char)
        frequency[ascii_val] = frequency.get(ascii_val, 0) + 1
    
    return frequency

def shift_ascii_values(s, shift):
    """
    Shift ASCII values by a given amount (Caesar cipher style)
    
    Args:
        s (str): Input string
        shift (int): Amount to shift ASCII values
    
    Returns:
        str: String with shifted ASCII values
    """
    result = ""
    
    for char in s:
        new_ascii = ord(char) + shift
        # Keep within printable ASCII range (32-126)
        if 32 <= new_ascii <= 126:
            result += chr(new_ascii)
        else:
            result += char  # Keep original if out of range
    
    return result

def is_ascii_string(s):
    """
    Check if string contains only ASCII characters
    
    Args:
        s (str): Input string
    
    Returns:
        bool: True if all characters are ASCII, False otherwise
    """
    try:
        s.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

def filter_ascii_range(s, min_ascii=32, max_ascii=126):
    """
    Filter string to keep only characters in ASCII range
    
    Args:
        s (str): Input string
        min_ascii (int): Minimum ASCII value
        max_ascii (int): Maximum ASCII value
    
    Returns:
        str: Filtered string
    """
    return ''.join(char for char in s if min_ascii <= ord(char) <= max_ascii)

def ascii_to_binary(s):
    """
    Convert string to binary representation of ASCII values
    
    Args:
        s (str): Input string
    
    Returns:
        list: List of binary strings
    """
    return [bin(ord(char))[2:].zfill(8) for char in s]

def ascii_to_hex(s):
    """
    Convert string to hexadecimal representation of ASCII values
    
    Args:
        s (str): Input string
    
    Returns:
        list: List of hexadecimal strings
    """
    return [hex(ord(char))[2:].upper() for char in s]

def compare_strings_ascii(s1, s2):
    """
    Compare two strings based on ASCII values
    
    Args:
        s1 (str): First string
        s2 (str): Second string
    
    Returns:
        dict: Comparison results
    """
    ascii1 = string_to_ascii_list(s1)
    ascii2 = string_to_ascii_list(s2)
    
    return {
        'string1': s1,
        'string2': s2,
        'ascii1': ascii1,
        'ascii2': ascii2,
        'sum1': sum(ascii1),
        'sum2': sum(ascii2),
        'avg1': sum(ascii1) / len(ascii1) if ascii1 else 0,
        'avg2': sum(ascii2) / len(ascii2) if ascii2 else 0,
        'lexicographically_smaller': s1 < s2
    }

def main():
    # Test individual characters
    print("ASCII values of individual characters:")
    print("-" * 40)
    test_chars = ['A', 'a', '0', '9', ' ', '!', '@', 'Z', 'z']
    
    print(f"{'Character':<10} {'ASCII Value':<12} {'Binary':<10} {'Hex':<5}")
    print("-" * 40)
    
    for char in test_chars:
        ascii_val = get_ascii_value(char)
        binary = bin(ascii_val)[2:].zfill(8)
        hex_val = hex(ascii_val)[2:].upper()
        
        print(f"'{char}'        {ascii_val:<12} {binary:<10} {hex_val:<5}")
    
    # Test ASCII to character conversion
    print("\nASCII values to characters:")
    print("-" * 30)
    test_ascii_values = [65, 97, 48, 57, 32, 33, 64, 90, 122]
    
    for ascii_val in test_ascii_values:
        char = get_character_from_ascii(ascii_val)
        print(f"ASCII {ascii_val} -> '{char}'")
    
    # Test string to ASCII conversion
    print("\nString to ASCII conversion:")
    print("-" * 30)
    test_strings = [
        "Hello",
        "World!",
        "123",
        "ABC",
        "abc"
    ]
    
    for s in test_strings:
        ascii_list = string_to_ascii_list(s)
        print(f"'{s}' -> {ascii_list}")
    
    # Test ASCII analysis
    print("\nASCII analysis:")
    print("-" * 20)
    test_str = "Hello World!"
    
    ascii_sum = sum_of_ascii_values(test_str)
    ascii_avg = average_ascii_value(test_str)
    min_ascii, max_ascii, min_char, max_char = find_ascii_range(test_str)
    
    print(f"String: '{test_str}'")
    print(f"ASCII values: {string_to_ascii_list(test_str)}")
    print(f"Sum of ASCII values: {ascii_sum}")
    print(f"Average ASCII value: {ascii_avg:.2f}")
    print(f"Min ASCII: {min_ascii} ('{min_char}')")
    print(f"Max ASCII: {max_ascii} ('{max_char}')")
    
    # Test frequency analysis
    print("\nASCII frequency analysis:")
    print("-" * 30)
    frequency = ascii_frequency_analysis(test_str)
    
    print(f"String: '{test_str}'")
    print("ASCII frequencies:")
    for ascii_val, freq in sorted(frequency.items()):
        char = chr(ascii_val)
        print(f"  '{char}' (ASCII {ascii_val}): {freq} times")
    
    # Test ASCII shifting
    print("\nASCII shifting (Caesar cipher style):")
    print("-" * 40)
    shifts = [1, -1, 3, -3, 13]
    
    for shift in shifts:
        shifted = shift_ascii_values(test_str, shift)
        print(f"Shift by {shift:2d}: '{test_str}' -> '{shifted}'")
    
    # Test binary and hex conversion
    print("\nBinary and hexadecimal representation:")
    print("-" * 40)
    short_str = "Hi!"
    
    binary_repr = ascii_to_binary(short_str)
    hex_repr = ascii_to_hex(short_str)
    
    print(f"String: '{short_str}'")
    print(f"ASCII values: {string_to_ascii_list(short_str)}")
    print(f"Binary: {binary_repr}")
    print(f"Hexadecimal: {hex_repr}")
    
    # Test ASCII string validation
    print("\nASCII string validation:")
    print("-" * 25)
    validation_strings = [
        "Hello World",
        "Café",
        "naïve",
        "ASCII only!",
        "émoji 😀"
    ]
    
    for s in validation_strings:
        is_ascii = is_ascii_string(s)
        filtered = filter_ascii_range(s)
        
        print(f"'{s}': {'ASCII' if is_ascii else 'Non-ASCII'}")
        if not is_ascii:
            print(f"  Filtered: '{filtered}'")
    
    # Test string comparison
    print("\nString comparison based on ASCII:")
    print("-" * 35)
    comparison_pairs = [
        ("apple", "banana"),
        ("Hello", "hello"),
        ("123", "456"),
        ("ABC", "abc")
    ]
    
    for s1, s2 in comparison_pairs:
        comparison = compare_strings_ascii(s1, s2)
        
        print(f"'{s1}' vs '{s2}':")
        print(f"  ASCII sums: {comparison['sum1']} vs {comparison['sum2']}")
        print(f"  ASCII averages: {comparison['avg1']:.2f} vs {comparison['avg2']:.2f}")
        print(f"  Lexicographically: '{s1}' < '{s2}' is {comparison['lexicographically_smaller']}")
        print()
    
    # Interactive input
    print("Enter a string to analyze ASCII values (or 'quit' to exit):")
    while True:
        user_input = input("String: ")
        if user_input.lower() == 'quit':
            break
        
        print(f"Analyzing: '{user_input}'")
        
        # Basic ASCII analysis
        ascii_list = string_to_ascii_list(user_input)
        ascii_sum = sum_of_ascii_values(user_input)
        ascii_avg = average_ascii_value(user_input)
        
        print(f"ASCII values: {ascii_list}")
        print(f"Sum: {ascii_sum}")
        print(f"Average: {ascii_avg:.2f}")
        
        # Range analysis
        if user_input:
            min_ascii, max_ascii, min_char, max_char = find_ascii_range(user_input)
            print(f"Range: {min_ascii} ('{min_char}') to {max_ascii} ('{max_char}')")
        
        # ASCII validation
        is_ascii = is_ascii_string(user_input)
        print(f"Pure ASCII: {'Yes' if is_ascii else 'No'}")
        
        # Ask for operations
        print("\nOperations:")
        print("1. Show binary representation")
        print("2. Show hexadecimal representation")
        print("3. Shift ASCII values")
        print("4. Show frequency analysis")
        
        choice = input("Choose operation (1-4, or press Enter to skip): ").strip()
        
        if choice == '1':
            binary_repr = ascii_to_binary(user_input)
            print(f"Binary: {binary_repr}")
        elif choice == '2':
            hex_repr = ascii_to_hex(user_input)
            print(f"Hexadecimal: {hex_repr}")
        elif choice == '3':
            try:
                shift = int(input("Enter shift amount: "))
                shifted = shift_ascii_values(user_input, shift)
                print(f"Shifted by {shift}: '{shifted}'")
            except ValueError:
                print("Invalid shift amount!")
        elif choice == '4':
            frequency = ascii_frequency_analysis(user_input)
            print("Frequency analysis:")
            for ascii_val, freq in sorted(frequency.items()):
                char = chr(ascii_val)
                print(f"  '{char}' (ASCII {ascii_val}): {freq} times")
        
        print()

if __name__ == "__main__":
    main()