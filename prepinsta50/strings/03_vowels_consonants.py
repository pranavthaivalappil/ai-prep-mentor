"""
PrepInsta String Problem 3: Count vowels and consonants
"""

def count_vowels_consonants(s):
    """
    Count vowels and consonants in a string
    
    Args:
        s (str): Input string
    
    Returns:
        tuple: (vowel_count, consonant_count)
    """
    vowels = set('aeiouAEIOU')
    vowel_count = 0
    consonant_count = 0
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

def count_vowels_consonants_detailed(s):
    """
    Count vowels and consonants with detailed breakdown
    
    Args:
        s (str): Input string
    
    Returns:
        dict: Detailed count information
    """
    vowels = set('aeiouAEIOU')
    vowel_chars = []
    consonant_chars = []
    other_chars = []
    
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_chars.append(char)
            else:
                consonant_chars.append(char)
        else:
            other_chars.append(char)
    
    return {
        'vowel_count': len(vowel_chars),
        'consonant_count': len(consonant_chars),
        'vowel_chars': vowel_chars,
        'consonant_chars': consonant_chars,
        'other_chars': other_chars,
        'total_alphabetic': len(vowel_chars) + len(consonant_chars),
        'total_chars': len(s)
    }

def count_each_vowel(s):
    """
    Count each vowel individually
    
    Args:
        s (str): Input string
    
    Returns:
        dict: Count of each vowel
    """
    vowel_counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for char in s.lower():
        if char in vowel_counts:
            vowel_counts[char] += 1
    
    return vowel_counts

def find_vowel_positions(s):
    """
    Find positions of all vowels in string
    
    Args:
        s (str): Input string
    
    Returns:
        list: List of (position, vowel) tuples
    """
    vowels = set('aeiouAEIOU')
    positions = []
    
    for i, char in enumerate(s):
        if char in vowels:
            positions.append((i, char))
    
    return positions

def find_consonant_positions(s):
    """
    Find positions of all consonants in string
    
    Args:
        s (str): Input string
    
    Returns:
        list: List of (position, consonant) tuples
    """
    vowels = set('aeiouAEIOU')
    positions = []
    
    for i, char in enumerate(s):
        if char.isalpha() and char not in vowels:
            positions.append((i, char))
    
    return positions

def remove_vowels(s):
    """
    Remove all vowels from string
    
    Args:
        s (str): Input string
    
    Returns:
        str: String without vowels
    """
    vowels = set('aeiouAEIOU')
    return ''.join(char for char in s if char not in vowels)

def remove_consonants(s):
    """
    Remove all consonants from string
    
    Args:
        s (str): Input string
    
    Returns:
        str: String without consonants
    """
    vowels = set('aeiouAEIOU')
    return ''.join(char for char in s if not char.isalpha() or char in vowels)

def replace_vowels(s, replacement='*'):
    """
    Replace all vowels with a character
    
    Args:
        s (str): Input string
        replacement (str): Character to replace vowels with
    
    Returns:
        str: String with vowels replaced
    """
    vowels = set('aeiouAEIOU')
    return ''.join(replacement if char in vowels else char for char in s)

def replace_consonants(s, replacement='*'):
    """
    Replace all consonants with a character
    
    Args:
        s (str): Input string
        replacement (str): Character to replace consonants with
    
    Returns:
        str: String with consonants replaced
    """
    vowels = set('aeiouAEIOU')
    return ''.join(replacement if char.isalpha() and char not in vowels else char for char in s)

def vowel_consonant_ratio(s):
    """
    Calculate vowel to consonant ratio
    
    Args:
        s (str): Input string
    
    Returns:
        float: Vowel to consonant ratio (None if no consonants)
    """
    vowel_count, consonant_count = count_vowels_consonants(s)
    
    if consonant_count == 0:
        return None if vowel_count == 0 else float('inf')
    
    return vowel_count / consonant_count

def is_vowel_heavy(s, threshold=0.4):
    """
    Check if string is vowel-heavy (has high vowel percentage)
    
    Args:
        s (str): Input string
        threshold (float): Minimum vowel percentage to be considered vowel-heavy
    
    Returns:
        bool: True if vowel-heavy, False otherwise
    """
    vowel_count, consonant_count = count_vowels_consonants(s)
    total_alphabetic = vowel_count + consonant_count
    
    if total_alphabetic == 0:
        return False
    
    vowel_percentage = vowel_count / total_alphabetic
    return vowel_percentage >= threshold

def longest_vowel_substring(s):
    """
    Find the longest substring containing only vowels
    
    Args:
        s (str): Input string
    
    Returns:
        str: Longest vowel-only substring
    """
    vowels = set('aeiouAEIOU')
    longest = ""
    current = ""
    
    for char in s:
        if char in vowels:
            current += char
        else:
            if len(current) > len(longest):
                longest = current
            current = ""
    
    # Check the last substring
    if len(current) > len(longest):
        longest = current
    
    return longest

def longest_consonant_substring(s):
    """
    Find the longest substring containing only consonants
    
    Args:
        s (str): Input string
    
    Returns:
        str: Longest consonant-only substring
    """
    vowels = set('aeiouAEIOU')
    longest = ""
    current = ""
    
    for char in s:
        if char.isalpha() and char not in vowels:
            current += char
        else:
            if len(current) > len(longest):
                longest = current
            current = ""
    
    # Check the last substring
    if len(current) > len(longest):
        longest = current
    
    return longest

def main():
    # Test strings
    test_strings = [
        "Hello World",
        "Python Programming",
        "aeiou",
        "bcdfg",
        "The quick brown fox",
        "12345!@#",
        "",
        "Education",
        "Rhythm"
    ]
    
    print("Vowel and consonant counting:")
    print("-" * 50)
    print(f"{'String':<20} {'Vowels':<8} {'Consonants':<12} {'Ratio':<8}")
    print("-" * 50)
    
    for s in test_strings:
        vowel_count, consonant_count = count_vowels_consonants(s)
        ratio = vowel_consonant_ratio(s)
        ratio_str = f"{ratio:.2f}" if ratio is not None and ratio != float('inf') else "N/A"
        
        s_display = s if len(s) <= 19 else s[:16] + "..."
        print(f"{s_display:<20} {vowel_count:<8} {consonant_count:<12} {ratio_str:<8}")
    
    # Detailed analysis
    print("\nDetailed vowel/consonant analysis:")
    print("-" * 40)
    test_str = "Hello World Programming"
    
    detailed = count_vowels_consonants_detailed(test_str)
    vowel_counts = count_each_vowel(test_str)
    vowel_positions = find_vowel_positions(test_str)
    consonant_positions = find_consonant_positions(test_str)
    
    print(f"String: '{test_str}'")
    print(f"Total characters: {detailed['total_chars']}")
    print(f"Alphabetic characters: {detailed['total_alphabetic']}")
    print(f"Vowels: {detailed['vowel_count']} {detailed['vowel_chars']}")
    print(f"Consonants: {detailed['consonant_count']} {detailed['consonant_chars']}")
    print(f"Other characters: {detailed['other_chars']}")
    print(f"Individual vowel counts: {vowel_counts}")
    print(f"Vowel positions: {vowel_positions}")
    print(f"Consonant positions: {consonant_positions}")
    
    # String manipulation
    print("\nString manipulation:")
    print("-" * 25)
    
    no_vowels = remove_vowels(test_str)
    no_consonants = remove_consonants(test_str)
    vowels_replaced = replace_vowels(test_str, '*')
    consonants_replaced = replace_consonants(test_str, '#')
    
    print(f"Original: '{test_str}'")
    print(f"Remove vowels: '{no_vowels}'")
    print(f"Remove consonants: '{no_consonants}'")
    print(f"Replace vowels with *: '{vowels_replaced}'")
    print(f"Replace consonants with #: '{consonants_replaced}'")
    
    # Vowel-heavy analysis
    print("\nVowel-heavy analysis:")
    print("-" * 25)
    vowel_test_strings = [
        "beautiful",
        "education",
        "programming",
        "aeiou",
        "bcdfg",
        "queue"
    ]
    
    for s in vowel_test_strings:
        is_heavy = is_vowel_heavy(s)
        vowel_count, consonant_count = count_vowels_consonants(s)
        total = vowel_count + consonant_count
        percentage = (vowel_count / total * 100) if total > 0 else 0
        
        print(f"'{s}': {percentage:.1f}% vowels - {'Vowel-heavy' if is_heavy else 'Not vowel-heavy'}")
    
    # Longest substrings
    print("\nLongest vowel/consonant substrings:")
    print("-" * 40)
    substring_test_strings = [
        "beautiful",
        "programming",
        "aeiouaeiou",
        "bcdfghjklmnp",
        "hello world"
    ]
    
    for s in substring_test_strings:
        longest_vowel = longest_vowel_substring(s)
        longest_consonant = longest_consonant_substring(s)
        
        print(f"'{s}':")
        print(f"  Longest vowel substring: '{longest_vowel}' (length: {len(longest_vowel)})")
        print(f"  Longest consonant substring: '{longest_consonant}' (length: {len(longest_consonant)})")
    
    # Interactive input
    print("\nEnter a string to analyze vowels and consonants (or 'quit' to exit):")
    while True:
        user_input = input("String: ")
        if user_input.lower() == 'quit':
            break
        
        print(f"Analyzing: '{user_input}'")
        
        # Basic counts
        vowel_count, consonant_count = count_vowels_consonants(user_input)
        detailed = count_vowels_consonants_detailed(user_input)
        vowel_counts = count_each_vowel(user_input)
        
        print(f"Vowels: {vowel_count}")
        print(f"Consonants: {consonant_count}")
        print(f"Individual vowel counts: {vowel_counts}")
        
        # Ratio and percentage
        ratio = vowel_consonant_ratio(user_input)
        total_alphabetic = vowel_count + consonant_count
        if total_alphabetic > 0:
            vowel_percentage = vowel_count / total_alphabetic * 100
            print(f"Vowel percentage: {vowel_percentage:.1f}%")
            if ratio is not None and ratio != float('inf'):
                print(f"Vowel to consonant ratio: {ratio:.2f}")
        
        # Vowel-heavy check
        is_heavy = is_vowel_heavy(user_input)
        print(f"Vowel-heavy: {'Yes' if is_heavy else 'No'}")
        
        # Longest substrings
        longest_vowel = longest_vowel_substring(user_input)
        longest_consonant = longest_consonant_substring(user_input)
        
        if longest_vowel:
            print(f"Longest vowel substring: '{longest_vowel}'")
        if longest_consonant:
            print(f"Longest consonant substring: '{longest_consonant}'")
        
        print()

if __name__ == "__main__":
    main()