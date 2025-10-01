"""
PrepInsta String Problem 1: Check if string is palindrome
"""

def is_palindrome_simple(s):
    """
    Check if string is palindrome using simple string reversal
    
    Args:
        s (str): Input string
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    return s == s[::-1]

def is_palindrome_case_insensitive(s):
    """
    Check if string is palindrome (case insensitive)
    
    Args:
        s (str): Input string
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    s = s.lower()
    return s == s[::-1]

def is_palindrome_alphanumeric_only(s):
    """
    Check if string is palindrome considering only alphanumeric characters
    
    Args:
        s (str): Input string
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def is_palindrome_two_pointers(s):
    """
    Check if string is palindrome using two pointers approach
    
    Args:
        s (str): Input string
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

def is_palindrome_recursive(s):
    """
    Check if string is palindrome using recursion
    
    Args:
        s (str): Input string
    
    Returns:
        bool: True if palindrome, False otherwise
    """
    if len(s) <= 1:
        return True
    
    if s[0] != s[-1]:
        return False
    
    return is_palindrome_recursive(s[1:-1])

def longest_palindromic_substring(s):
    """
    Find the longest palindromic substring
    
    Args:
        s (str): Input string
    
    Returns:
        str: Longest palindromic substring
    """
    if not s:
        return ""
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    longest = ""
    
    for i in range(len(s)):
        # Check for odd length palindromes
        palindrome1 = expand_around_center(i, i)
        # Check for even length palindromes
        palindrome2 = expand_around_center(i, i + 1)
        
        # Update longest palindrome
        for palindrome in [palindrome1, palindrome2]:
            if len(palindrome) > len(longest):
                longest = palindrome
    
    return longest

def count_palindromic_substrings(s):
    """
    Count all palindromic substrings
    
    Args:
        s (str): Input string
    
    Returns:
        int: Number of palindromic substrings
    """
    def expand_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    total_count = 0
    
    for i in range(len(s)):
        # Count odd length palindromes
        total_count += expand_around_center(i, i)
        # Count even length palindromes
        total_count += expand_around_center(i, i + 1)
    
    return total_count

def find_all_palindromic_substrings(s):
    """
    Find all palindromic substrings
    
    Args:
        s (str): Input string
    
    Returns:
        list: List of all palindromic substrings
    """
    palindromes = set()
    
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substring = s[i:j]
            if is_palindrome_simple(substring):
                palindromes.add(substring)
    
    return sorted(list(palindromes))

def make_palindrome(s):
    """
    Make string palindrome by adding minimum characters at the beginning
    
    Args:
        s (str): Input string
    
    Returns:
        str: Palindromic string
    """
    for i in range(len(s)):
        # Check if s[i:] can form a palindrome with prefix
        candidate = s[:i][::-1] + s
        if is_palindrome_simple(candidate):
            return candidate
    
    return s + s[::-1]  # Fallback

def is_palindrome_permutation(s):
    """
    Check if string can be rearranged to form a palindrome
    
    Args:
        s (str): Input string
    
    Returns:
        bool: True if can form palindrome, False otherwise
    """
    char_count = {}
    
    for char in s.lower():
        if char.isalnum():
            char_count[char] = char_count.get(char, 0) + 1
    
    odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
    
    # For palindrome, at most one character can have odd count
    return odd_count <= 1

def palindrome_pairs(words):
    """
    Find pairs of words that form palindromes when concatenated
    
    Args:
        words (list): List of words
    
    Returns:
        list: List of palindromic pairs
    """
    pairs = []
    
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                combined = words[i] + words[j]
                if is_palindrome_simple(combined):
                    pairs.append((words[i], words[j]))
    
    return pairs

def main():
    # Test basic palindrome checking
    test_strings = [
        "racecar",
        "hello",
        "A man a plan a canal Panama",
        "race a car",
        "Madam",
        "12321",
        "12345",
        "",
        "a"
    ]
    
    print("Palindrome checking methods:")
    print("-" * 60)
    print(f"{'String':<25} {'Simple':<8} {'Case Insens.':<12} {'Alphanumeric':<12} {'Two Pointers':<12}")
    print("-" * 60)
    
    for s in test_strings:
        simple = is_palindrome_simple(s)
        case_insens = is_palindrome_case_insensitive(s)
        alphanum = is_palindrome_alphanumeric_only(s)
        two_pointers = is_palindrome_two_pointers(s)
        
        s_display = s if len(s) <= 24 else s[:21] + "..."
        print(f"{s_display:<25} {simple:<8} {case_insens:<12} {alphanum:<12} {two_pointers:<12}")
    
    # Test recursive method
    print("\nRecursive palindrome checking:")
    print("-" * 35)
    for s in ["racecar", "hello", "madam", "python"]:
        recursive_result = is_palindrome_recursive(s)
        print(f"'{s}' is {'palindrome' if recursive_result else 'not palindrome'}")
    
    # Test longest palindromic substring
    print("\nLongest palindromic substrings:")
    print("-" * 35)
    test_strings_long = [
        "babad",
        "cbbd",
        "racecar",
        "abcdef",
        "abacabad"
    ]
    
    for s in test_strings_long:
        longest = longest_palindromic_substring(s)
        print(f"'{s}' -> '{longest}' (length: {len(longest)})")
    
    # Test palindromic substring counting
    print("\nPalindromic substring analysis:")
    print("-" * 35)
    for s in ["abc", "aaa", "racecar"]:
        count = count_palindromic_substrings(s)
        all_palindromes = find_all_palindromic_substrings(s)
        print(f"'{s}': {count} palindromic substrings")
        print(f"  All palindromes: {all_palindromes}")
    
    # Test palindrome creation
    print("\nMaking palindromes:")
    print("-" * 25)
    for s in ["abc", "ab", "race"]:
        palindrome = make_palindrome(s)
        print(f"'{s}' -> '{palindrome}'")
    
    # Test palindrome permutation
    print("\nPalindrome permutation check:")
    print("-" * 35)
    perm_test_strings = [
        "aab",
        "carerac",
        "abc",
        "Aab",
        "tactcoa"
    ]
    
    for s in perm_test_strings:
        can_form = is_palindrome_permutation(s)
        print(f"'{s}' can {'form' if can_form else 'not form'} a palindrome")
    
    # Test palindrome pairs
    print("\nPalindrome pairs:")
    print("-" * 20)
    word_lists = [
        ["race", "car", "hello"],
        ["lls", "s", "sssll"],
        ["abc", "cba", "def"]
    ]
    
    for words in word_lists:
        pairs = palindrome_pairs(words)
        print(f"Words: {words}")
        print(f"Palindromic pairs: {pairs}")
        print()
    
    # Interactive input
    print("Enter a string to check for palindrome (or 'quit' to exit):")
    while True:
        user_input = input("String: ")
        if user_input.lower() == 'quit':
            break
        
        print(f"Input: '{user_input}'")
        print(f"Simple check: {is_palindrome_simple(user_input)}")
        print(f"Case insensitive: {is_palindrome_case_insensitive(user_input)}")
        print(f"Alphanumeric only: {is_palindrome_alphanumeric_only(user_input)}")
        
        if len(user_input) <= 100:  # Avoid long computation
            longest = longest_palindromic_substring(user_input)
            count = count_palindromic_substrings(user_input)
            can_form = is_palindrome_permutation(user_input)
            
            print(f"Longest palindromic substring: '{longest}'")
            print(f"Total palindromic substrings: {count}")
            print(f"Can form palindrome by rearranging: {can_form}")
        
        print()

if __name__ == "__main__":
    main()