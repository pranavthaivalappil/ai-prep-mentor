"""
PrepInsta String Problem 4: Calculate string length
"""

def string_length_builtin(s):
    """
    Calculate string length using built-in len() function
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of string
    """
    return len(s)

def string_length_loop(s):
    """
    Calculate string length using loop
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of string
    """
    count = 0
    for char in s:
        count += 1
    return count

def string_length_recursive(s):
    """
    Calculate string length using recursion
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of string
    """
    if not s:
        return 0
    return 1 + string_length_recursive(s[1:])

def string_length_while_loop(s):
    """
    Calculate string length using while loop
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of string
    """
    count = 0
    i = 0
    try:
        while True:
            char = s[i]
            count += 1
            i += 1
    except IndexError:
        pass
    return count

def string_length_sum(s):
    """
    Calculate string length using sum() with generator
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of string
    """
    return sum(1 for char in s)

def string_length_without_spaces(s):
    """
    Calculate string length excluding spaces
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of string without spaces
    """
    return len(s.replace(' ', ''))

def string_length_alphabetic_only(s):
    """
    Calculate length of alphabetic characters only
    
    Args:
        s (str): Input string
    
    Returns:
        int: Count of alphabetic characters
    """
    return sum(1 for char in s if char.isalpha())

def string_length_numeric_only(s):
    """
    Calculate length of numeric characters only
    
    Args:
        s (str): Input string
    
    Returns:
        int: Count of numeric characters
    """
    return sum(1 for char in s if char.isdigit())

def string_length_alphanumeric_only(s):
    """
    Calculate length of alphanumeric characters only
    
    Args:
        s (str): Input string
    
    Returns:
        int: Count of alphanumeric characters
    """
    return sum(1 for char in s if char.isalnum())

def string_length_analysis(s):
    """
    Comprehensive string length analysis
    
    Args:
        s (str): Input string
    
    Returns:
        dict: Dictionary with various length measurements
    """
    return {
        'total_length': len(s),
        'without_spaces': len(s.replace(' ', '')),
        'alphabetic_only': sum(1 for char in s if char.isalpha()),
        'numeric_only': sum(1 for char in s if char.isdigit()),
        'alphanumeric_only': sum(1 for char in s if char.isalnum()),
        'uppercase_letters': sum(1 for char in s if char.isupper()),
        'lowercase_letters': sum(1 for char in s if char.islower()),
        'spaces': s.count(' '),
        'special_characters': sum(1 for char in s if not char.isalnum() and char != ' '),
        'vowels': sum(1 for char in s if char.lower() in 'aeiou'),
        'consonants': sum(1 for char in s if char.isalpha() and char.lower() not in 'aeiou')
    }

def longest_word_length(s):
    """
    Find the length of the longest word in string
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of longest word
    """
    words = s.split()
    return max(len(word) for word in words) if words else 0

def shortest_word_length(s):
    """
    Find the length of the shortest word in string
    
    Args:
        s (str): Input string
    
    Returns:
        int: Length of shortest word
    """
    words = s.split()
    return min(len(word) for word in words) if words else 0

def average_word_length(s):
    """
    Calculate average word length in string
    
    Args:
        s (str): Input string
    
    Returns:
        float: Average word length
    """
    words = s.split()
    return sum(len(word) for word in words) / len(words) if words else 0

def word_length_distribution(s):
    """
    Get distribution of word lengths
    
    Args:
        s (str): Input string
    
    Returns:
        dict: Dictionary with word length distribution
    """
    words = s.split()
    distribution = {}
    
    for word in words:
        length = len(word)
        distribution[length] = distribution.get(length, 0) + 1
    
    return distribution

def compare_string_lengths(strings):
    """
    Compare lengths of multiple strings
    
    Args:
        strings (list): List of strings
    
    Returns:
        dict: Comparison results
    """
    if not strings:
        return {}
    
    lengths = [len(s) for s in strings]
    
    return {
        'strings': strings,
        'lengths': lengths,
        'longest': max(strings, key=len),
        'shortest': min(strings, key=len),
        'max_length': max(lengths),
        'min_length': min(lengths),
        'average_length': sum(lengths) / len(lengths),
        'total_length': sum(lengths)
    }

def main():
    # Test strings
    test_strings = [
        "Hello",
        "Python Programming",
        "",
        "a",
        "The quick brown fox jumps over the lazy dog",
        "12345",
        "Hello123!@#",
        "   spaces   ",
        "MixedCASE123"
    ]
    
    print("String length calculation methods:")
    print("-" * 70)
    print(f"{'String':<25} {'Built-in':<10} {'Loop':<10} {'Recursive':<10} {'While':<10} {'Sum':<10}")
    print("-" * 70)
    
    for s in test_strings:
        builtin_len = string_length_builtin(s)
        loop_len = string_length_loop(s)
        # Only use recursion for short strings to avoid stack overflow
        recursive_len = string_length_recursive(s) if len(s) <= 20 else "Too long"
        while_len = string_length_while_loop(s)
        sum_len = string_length_sum(s)
        
        s_display = repr(s) if len(repr(s)) <= 24 else repr(s)[:21] + "..."
        rec_str = str(recursive_len)
        
        print(f"{s_display:<25} {builtin_len:<10} {loop_len:<10} {rec_str:<10} {while_len:<10} {sum_len:<10}")
    
    # Comprehensive analysis
    print("\nComprehensive string analysis:")
    print("-" * 35)
    test_str = "Hello World! Python123 Programming"
    
    analysis = string_length_analysis(test_str)
    
    print(f"String: '{test_str}'")
    print(f"Total length: {analysis['total_length']}")
    print(f"Without spaces: {analysis['without_spaces']}")
    print(f"Alphabetic characters: {analysis['alphabetic_only']}")
    print(f"Numeric characters: {analysis['numeric_only']}")
    print(f"Alphanumeric characters: {analysis['alphanumeric_only']}")
    print(f"Uppercase letters: {analysis['uppercase_letters']}")
    print(f"Lowercase letters: {analysis['lowercase_letters']}")
    print(f"Spaces: {analysis['spaces']}")
    print(f"Special characters: {analysis['special_characters']}")
    print(f"Vowels: {analysis['vowels']}")
    print(f"Consonants: {analysis['consonants']}")
    
    # Word length analysis
    print("\nWord length analysis:")
    print("-" * 25)
    
    longest_len = longest_word_length(test_str)
    shortest_len = shortest_word_length(test_str)
    avg_len = average_word_length(test_str)
    distribution = word_length_distribution(test_str)
    
    print(f"Longest word length: {longest_len}")
    print(f"Shortest word length: {shortest_len}")
    print(f"Average word length: {avg_len:.2f}")
    print(f"Word length distribution: {distribution}")
    
    # String comparison
    print("\nString length comparison:")
    print("-" * 30)
    comparison_strings = [
        "Short",
        "Medium length string",
        "This is a very long string with many words",
        "A",
        ""
    ]
    
    comparison = compare_string_lengths(comparison_strings)
    
    print("Strings and their lengths:")
    for i, (string, length) in enumerate(zip(comparison['strings'], comparison['lengths'])):
        print(f"  {i+1}. '{string}' -> {length}")
    
    print(f"\nLongest: '{comparison['longest']}' ({comparison['max_length']} chars)")
    print(f"Shortest: '{comparison['shortest']}' ({comparison['min_length']} chars)")
    print(f"Average length: {comparison['average_length']:.2f}")
    print(f"Total length: {comparison['total_length']}")
    
    # Performance comparison
    print("\nPerformance comparison (large string):")
    print("-" * 40)
    
    import time
    large_string = "a" * 100000
    
    methods = [
        ("Built-in len()", string_length_builtin),
        ("For loop", string_length_loop),
        ("While loop", string_length_while_loop),
        ("Sum with generator", string_length_sum)
    ]
    
    for name, method in methods:
        start_time = time.time()
        result = method(large_string)
        end_time = time.time()
        print(f"{name}: {(end_time - start_time) * 1000:.4f} ms (length: {result})")
    
    # Interactive input
    print("\nEnter a string to analyze length (or 'quit' to exit):")
    while True:
        user_input = input("String: ")
        if user_input.lower() == 'quit':
            break
        
        print(f"Analyzing: '{user_input}'")
        
        # Basic length
        length = string_length_builtin(user_input)
        print(f"Total length: {length}")
        
        if length > 0:
            # Comprehensive analysis
            analysis = string_length_analysis(user_input)
            
            print(f"Without spaces: {analysis['without_spaces']}")
            print(f"Alphabetic only: {analysis['alphabetic_only']}")
            print(f"Numeric only: {analysis['numeric_only']}")
            print(f"Alphanumeric only: {analysis['alphanumeric_only']}")
            
            # Word analysis if there are words
            words = user_input.split()
            if words:
                longest_len = longest_word_length(user_input)
                shortest_len = shortest_word_length(user_input)
                avg_len = average_word_length(user_input)
                
                print(f"Number of words: {len(words)}")
                print(f"Longest word length: {longest_len}")
                print(f"Shortest word length: {shortest_len}")
                print(f"Average word length: {avg_len:.2f}")
        
        print()

if __name__ == "__main__":
    main()