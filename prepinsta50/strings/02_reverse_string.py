"""
PrepInsta String Problem 2: Reverse a string
"""

def reverse_string_slicing(s):
    """
    Reverse string using slicing
    
    Args:
        s (str): Input string
    
    Returns:
        str: Reversed string
    """
    return s[::-1]

def reverse_string_builtin(s):
    """
    Reverse string using built-in reversed() function
    
    Args:
        s (str): Input string
    
    Returns:
        str: Reversed string
    """
    return ''.join(reversed(s))

def reverse_string_loop(s):
    """
    Reverse string using loop
    
    Args:
        s (str): Input string
    
    Returns:
        str: Reversed string
    """
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def reverse_string_recursive(s):
    """
    Reverse string using recursion
    
    Args:
        s (str): Input string
    
    Returns:
        str: Reversed string
    """
    if len(s) <= 1:
        return s
    return s[-1] + reverse_string_recursive(s[:-1])

def reverse_string_stack(s):
    """
    Reverse string using stack approach
    
    Args:
        s (str): Input string
    
    Returns:
        str: Reversed string
    """
    stack = []
    
    # Push all characters to stack
    for char in s:
        stack.append(char)
    
    # Pop all characters to create reversed string
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

def reverse_string_two_pointers(s):
    """
    Reverse string using two pointers (in-place for list)
    
    Args:
        s (str): Input string
    
    Returns:
        str: Reversed string
    """
    char_list = list(s)
    left = 0
    right = len(char_list) - 1
    
    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1
    
    return ''.join(char_list)

def reverse_words_in_string(s):
    """
    Reverse the order of words in a string
    
    Args:
        s (str): Input string
    
    Returns:
        str: String with words in reverse order
    """
    words = s.split()
    return ' '.join(reversed(words))

def reverse_each_word_in_string(s):
    """
    Reverse each word individually in the string
    
    Args:
        s (str): Input string
    
    Returns:
        str: String with each word reversed
    """
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def reverse_string_preserve_spaces(s):
    """
    Reverse string while preserving space positions
    
    Args:
        s (str): Input string
    
    Returns:
        str: Reversed string with spaces in original positions
    """
    # Get non-space characters
    chars = [char for char in s if char != ' ']
    chars.reverse()
    
    # Rebuild string with spaces in original positions
    result = []
    char_index = 0
    
    for char in s:
        if char == ' ':
            result.append(' ')
        else:
            result.append(chars[char_index])
            char_index += 1
    
    return ''.join(result)

def reverse_string_vowels_only(s):
    """
    Reverse only the vowels in the string
    
    Args:
        s (str): Input string
    
    Returns:
        str: String with only vowels reversed
    """
    vowels = set('aeiouAEIOU')
    char_list = list(s)
    
    # Find all vowel positions
    vowel_chars = []
    vowel_positions = []
    
    for i, char in enumerate(char_list):
        if char in vowels:
            vowel_chars.append(char)
            vowel_positions.append(i)
    
    # Reverse vowels and place them back
    vowel_chars.reverse()
    
    for i, pos in enumerate(vowel_positions):
        char_list[pos] = vowel_chars[i]
    
    return ''.join(char_list)

def reverse_string_consonants_only(s):
    """
    Reverse only the consonants in the string
    
    Args:
        s (str): Input string
    
    Returns:
        str: String with only consonants reversed
    """
    vowels = set('aeiouAEIOU')
    char_list = list(s)
    
    # Find all consonant positions
    consonant_chars = []
    consonant_positions = []
    
    for i, char in enumerate(char_list):
        if char.isalpha() and char not in vowels:
            consonant_chars.append(char)
            consonant_positions.append(i)
    
    # Reverse consonants and place them back
    consonant_chars.reverse()
    
    for i, pos in enumerate(consonant_positions):
        char_list[pos] = consonant_chars[i]
    
    return ''.join(char_list)

def is_string_rotation(s1, s2):
    """
    Check if one string is rotation of another using string reversal concept
    
    Args:
        s1 (str): First string
        s2 (str): Second string
    
    Returns:
        bool: True if s2 is rotation of s1, False otherwise
    """
    if len(s1) != len(s2):
        return False
    
    # If s2 is rotation of s1, then s2 will be substring of s1+s1
    return s2 in s1 + s1

def main():
    # Test strings
    test_strings = [
        "hello",
        "Python",
        "12345",
        "racecar",
        "",
        "a",
        "Hello World!",
        "The quick brown fox"
    ]
    
    print("String reversal methods comparison:")
    print("-" * 80)
    print(f"{'Original':<20} {'Slicing':<15} {'Built-in':<15} {'Loop':<15} {'Recursive':<15}")
    print("-" * 80)
    
    for s in test_strings:
        slicing_result = reverse_string_slicing(s)
        builtin_result = reverse_string_builtin(s)
        loop_result = reverse_string_loop(s)
        # Only use recursion for short strings to avoid stack overflow
        recursive_result = reverse_string_recursive(s) if len(s) <= 20 else "Too long"
        
        orig_str = s if len(s) <= 19 else s[:16] + "..."
        slice_str = slicing_result if len(slicing_result) <= 14 else slicing_result[:11] + "..."
        builtin_str = builtin_result if len(builtin_result) <= 14 else builtin_result[:11] + "..."
        loop_str = loop_result if len(loop_result) <= 14 else loop_result[:11] + "..."
        rec_str = str(recursive_result) if len(str(recursive_result)) <= 14 else str(recursive_result)[:11] + "..."
        
        print(f"{orig_str:<20} {slice_str:<15} {builtin_str:<15} {loop_str:<15} {rec_str:<15}")
    
    # Test additional methods
    print("\nAdditional reversal methods:")
    print("-" * 40)
    test_str = "Hello World"
    
    stack_result = reverse_string_stack(test_str)
    two_pointers_result = reverse_string_two_pointers(test_str)
    
    print(f"Original: '{test_str}'")
    print(f"Stack method: '{stack_result}'")
    print(f"Two pointers: '{two_pointers_result}'")
    
    # Test word reversal
    print("\nWord reversal methods:")
    print("-" * 30)
    sentence = "The quick brown fox jumps"
    
    words_reversed = reverse_words_in_string(sentence)
    each_word_reversed = reverse_each_word_in_string(sentence)
    
    print(f"Original: '{sentence}'")
    print(f"Words reversed: '{words_reversed}'")
    print(f"Each word reversed: '{each_word_reversed}'")
    
    # Test space preservation
    print("\nSpace preservation:")
    print("-" * 25)
    spaced_string = "a b c d e"
    
    preserve_spaces = reverse_string_preserve_spaces(spaced_string)
    
    print(f"Original: '{spaced_string}'")
    print(f"Preserve spaces: '{preserve_spaces}'")
    
    # Test vowel/consonant reversal
    print("\nVowel and consonant reversal:")
    print("-" * 35)
    test_str = "hello world"
    
    vowels_reversed = reverse_string_vowels_only(test_str)
    consonants_reversed = reverse_string_consonants_only(test_str)
    
    print(f"Original: '{test_str}'")
    print(f"Vowels reversed: '{vowels_reversed}'")
    print(f"Consonants reversed: '{consonants_reversed}'")
    
    # Test string rotation
    print("\nString rotation check:")
    print("-" * 25)
    rotation_pairs = [
        ("abcde", "cdeab"),
        ("abcde", "abced"),
        ("hello", "llohe"),
        ("python", "thonpy")
    ]
    
    for s1, s2 in rotation_pairs:
        is_rotation = is_string_rotation(s1, s2)
        print(f"'{s1}' and '{s2}': {'Rotation' if is_rotation else 'Not rotation'}")
    
    # Performance comparison
    print("\nPerformance comparison (large string):")
    print("-" * 40)
    
    import time
    large_string = "a" * 10000
    
    methods = [
        ("Slicing", reverse_string_slicing),
        ("Built-in", reverse_string_builtin),
        ("Loop", reverse_string_loop),
        ("Stack", reverse_string_stack),
        ("Two pointers", reverse_string_two_pointers)
    ]
    
    for name, method in methods:
        start_time = time.time()
        result = method(large_string)
        end_time = time.time()
        print(f"{name}: {(end_time - start_time) * 1000:.4f} ms")
    
    # Interactive input
    print("\nEnter a string to reverse (or 'quit' to exit):")
    while True:
        user_input = input("String: ")
        if user_input.lower() == 'quit':
            break
        
        print(f"Original: '{user_input}'")
        print(f"Reversed: '{reverse_string_slicing(user_input)}'")
        
        # Ask for additional operations
        print("\nAdditional operations:")
        print("1. Reverse words order")
        print("2. Reverse each word")
        print("3. Reverse vowels only")
        print("4. Reverse consonants only")
        print("5. Preserve spaces")
        
        choice = input("Choose operation (1-5, or press Enter to skip): ").strip()
        
        if choice == '1':
            result = reverse_words_in_string(user_input)
            print(f"Words reversed: '{result}'")
        elif choice == '2':
            result = reverse_each_word_in_string(user_input)
            print(f"Each word reversed: '{result}'")
        elif choice == '3':
            result = reverse_string_vowels_only(user_input)
            print(f"Vowels reversed: '{result}'")
        elif choice == '4':
            result = reverse_string_consonants_only(user_input)
            print(f"Consonants reversed: '{result}'")
        elif choice == '5':
            result = reverse_string_preserve_spaces(user_input)
            print(f"Spaces preserved: '{result}'")
        
        print()

if __name__ == "__main__":
    main()