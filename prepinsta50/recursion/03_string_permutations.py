"""
PrepInsta Recursion Problem 3: Generate string permutations
"""

def permutations_recursive(s):
    """
    Generate all permutations of a string using recursion
    
    Args:
        s (str): Input string
    
    Returns:
        list: List of all permutations
    """
    # Base case
    if len(s) <= 1:
        return [s]
    
    result = []
    
    # For each character in the string
    for i in range(len(s)):
        # Extract the character
        char = s[i]
        # Get remaining characters
        remaining = s[:i] + s[i+1:]
        
        # Get permutations of remaining characters
        for perm in permutations_recursive(remaining):
            result.append(char + perm)
    
    return result

def permutations_iterative(s):
    """
    Generate all permutations using iterative approach
    
    Args:
        s (str): Input string
    
    Returns:
        list: List of all permutations
    """
    from itertools import permutations
    return [''.join(p) for p in permutations(s)]

def permutations_unique(s):
    """
    Generate unique permutations (handles duplicate characters)
    
    Args:
        s (str): Input string
    
    Returns:
        list: List of unique permutations
    """
    # Convert to list and sort to handle duplicates
    chars = sorted(list(s))
    result = []
    
    def backtrack(current_perm, remaining_chars):
        if not remaining_chars:
            result.append(''.join(current_perm))
            return
        
        prev_char = None
        for i, char in enumerate(remaining_chars):
            # Skip duplicates
            if char == prev_char:
                continue
            
            prev_char = char
            current_perm.append(char)
            new_remaining = remaining_chars[:i] + remaining_chars[i+1:]
            backtrack(current_perm, new_remaining)
            current_perm.pop()
    
    backtrack([], chars)
    return result

def permutations_with_repetition(chars, length):
    """
    Generate permutations with repetition allowed
    
    Args:
        chars (str): Available characters
        length (int): Length of each permutation
    
    Returns:
        list: List of permutations with repetition
    """
    if length == 0:
        return ['']
    
    result = []
    for char in chars:
        for perm in permutations_with_repetition(chars, length - 1):
            result.append(char + perm)
    
    return result

def count_permutations(s):
    """
    Count total number of permutations
    
    Args:
        s (str): Input string
    
    Returns:
        int: Number of permutations
    """
    from math import factorial
    from collections import Counter
    
    n = len(s)
    char_counts = Counter(s)
    
    # Calculate n! / (n1! * n2! * ... * nk!)
    result = factorial(n)
    for count in char_counts.values():
        result //= factorial(count)
    
    return result

def nth_permutation(s, n):
    """
    Find the nth permutation (0-indexed) without generating all
    
    Args:
        s (str): Input string
        n (int): Index of desired permutation
    
    Returns:
        str: The nth permutation
    """
    from math import factorial
    
    chars = sorted(list(s))
    result = []
    n = n % factorial(len(chars))  # Handle n >= total permutations
    
    while chars:
        factorial_val = factorial(len(chars) - 1)
        index = n // factorial_val
        result.append(chars.pop(index))
        n %= factorial_val
    
    return ''.join(result)

def next_permutation(s):
    """
    Find the next lexicographically greater permutation
    
    Args:
        s (str): Input string
    
    Returns:
        str or None: Next permutation or None if no greater permutation exists
    """
    chars = list(s)
    
    # Find the largest index i such that chars[i] < chars[i + 1]
    i = len(chars) - 2
    while i >= 0 and chars[i] >= chars[i + 1]:
        i -= 1
    
    if i == -1:
        return None  # No next permutation
    
    # Find the largest index j such that chars[i] < chars[j]
    j = len(chars) - 1
    while chars[j] <= chars[i]:
        j -= 1
    
    # Swap chars[i] and chars[j]
    chars[i], chars[j] = chars[j], chars[i]
    
    # Reverse the suffix starting at chars[i + 1]
    chars[i + 1:] = reversed(chars[i + 1:])
    
    return ''.join(chars)

def permutations_of_length_k(s, k):
    """
    Generate all permutations of length k from string s
    
    Args:
        s (str): Input string
        k (int): Length of permutations
    
    Returns:
        list: List of k-length permutations
    """
    if k == 0:
        return ['']
    if k > len(s):
        return []
    
    result = []
    
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]
        
        for perm in permutations_of_length_k(remaining, k - 1):
            result.append(char + perm)
    
    return result

def is_permutation(s1, s2):
    """
    Check if one string is a permutation of another
    
    Args:
        s1 (str): First string
        s2 (str): Second string
    
    Returns:
        bool: True if s2 is a permutation of s1
    """
    return sorted(s1) == sorted(s2)

def find_anagrams(word, word_list):
    """
    Find all anagrams of a word from a list
    
    Args:
        word (str): Target word
        word_list (list): List of words to check
    
    Returns:
        list: List of anagrams
    """
    return [w for w in word_list if is_permutation(word, w) and w != word]

def permutation_rank(s):
    """
    Find the rank (position) of a permutation in lexicographic order
    
    Args:
        s (str): Input permutation
    
    Returns:
        int: Rank of the permutation (1-indexed)
    """
    from math import factorial
    
    chars = list(s)
    sorted_chars = sorted(chars)
    rank = 1
    
    for i in range(len(chars)):
        # Count characters smaller than current character
        smaller_count = 0
        for char in sorted_chars:
            if char < chars[i]:
                smaller_count += 1
            elif char == chars[i]:
                sorted_chars.remove(char)
                break
        
        # Add to rank
        rank += smaller_count * factorial(len(chars) - i - 1)
    
    return rank

def main():
    # Test basic permutations
    print("String permutations:")
    print("-" * 25)
    
    test_strings = ["abc", "ab", "a", "xyz"]
    
    for s in test_strings:
        perms = permutations_recursive(s)
        count = count_permutations(s)
        
        print(f"String: '{s}'")
        print(f"Permutations ({count}): {perms}")
        print()
    
    # Test unique permutations
    print("Unique permutations (with duplicates):")
    print("-" * 40)
    
    duplicate_strings = ["aab", "abc", "aaa", "abcc"]
    
    for s in duplicate_strings:
        unique_perms = permutations_unique(s)
        total_count = count_permutations(s)
        
        print(f"String: '{s}'")
        print(f"Unique permutations ({total_count}): {unique_perms}")
        print()
    
    # Test permutations with repetition
    print("Permutations with repetition:")
    print("-" * 35)
    
    repetition_tests = [
        ("ab", 3),
        ("xyz", 2),
        ("12", 4)
    ]
    
    for chars, length in repetition_tests:
        perms_rep = permutations_with_repetition(chars, length)
        
        print(f"Characters: '{chars}', Length: {length}")
        print(f"Count: {len(perms_rep)}")
        print(f"First 10: {perms_rep[:10]}")
        print()
    
    # Test k-length permutations
    print("K-length permutations:")
    print("-" * 25)
    
    k_tests = [
        ("abcd", 2),
        ("xyz", 3),
        ("12345", 3)
    ]
    
    for s, k in k_tests:
        k_perms = permutations_of_length_k(s, k)
        
        print(f"String: '{s}', K: {k}")
        print(f"K-permutations ({len(k_perms)}): {k_perms}")
        print()
    
    # Test nth permutation
    print("Nth permutation:")
    print("-" * 20)
    
    test_string = "abcd"
    test_indices = [0, 5, 10, 23]  # 24 total permutations for "abcd"
    
    for n in test_indices:
        nth_perm = nth_permutation(test_string, n)
        print(f"String: '{test_string}', Index: {n} -> '{nth_perm}'")
    
    # Test next permutation
    print("\nNext permutation:")
    print("-" * 20)
    
    next_perm_tests = ["abc", "acb", "bca", "cba", "aab", "aba"]
    
    for s in next_perm_tests:
        next_perm = next_permutation(s)
        print(f"'{s}' -> {next_perm if next_perm else 'No next permutation'}")
    
    # Test permutation checking
    print("\nPermutation checking:")
    print("-" * 25)
    
    permutation_pairs = [
        ("abc", "bca"),
        ("abc", "def"),
        ("listen", "silent"),
        ("hello", "world"),
        ("aab", "aba")
    ]
    
    for s1, s2 in permutation_pairs:
        is_perm = is_permutation(s1, s2)
        print(f"'{s1}' and '{s2}': {'Permutation' if is_perm else 'Not permutation'}")
    
    # Test anagram finding
    print("\nAnagram finding:")
    print("-" * 20)
    
    word = "listen"
    word_list = ["silent", "enlist", "hello", "world", "tinsel", "inlets"]
    anagrams = find_anagrams(word, word_list)
    
    print(f"Word: '{word}'")
    print(f"Word list: {word_list}")
    print(f"Anagrams: {anagrams}")
    
    # Test permutation rank
    print("\nPermutation rank:")
    print("-" * 20)
    
    rank_tests = ["abc", "acb", "bac", "bca", "cab", "cba"]
    
    for s in rank_tests:
        rank = permutation_rank(s)
        print(f"'{s}' has rank: {rank}")
    
    # Performance comparison
    print("\nPerformance comparison:")
    print("-" * 25)
    
    import time
    
    test_str = "abcde"
    
    # Recursive method
    start_time = time.time()
    recursive_perms = permutations_recursive(test_str)
    recursive_time = time.time() - start_time
    
    # Iterative method (using itertools)
    start_time = time.time()
    iterative_perms = permutations_iterative(test_str)
    iterative_time = time.time() - start_time
    
    print(f"String: '{test_str}' ({len(recursive_perms)} permutations)")
    print(f"Recursive: {recursive_time*1000:.4f} ms")
    print(f"Iterative: {iterative_time*1000:.4f} ms")
    
    # Interactive input
    print("\nEnter a string to generate permutations (or 'quit' to exit):")
    while True:
        user_input = input("String: ")
        if user_input.lower() == 'quit':
            break
        
        if len(user_input) > 8:
            print("String too long! Please enter a string with 8 or fewer characters.")
            continue
        
        print(f"Analyzing: '{user_input}'")
        
        # Basic permutations
        perms = permutations_recursive(user_input)
        total_count = count_permutations(user_input)
        
        print(f"Total permutations: {total_count}")
        
        if len(perms) <= 50:
            print(f"All permutations: {perms}")
        else:
            print(f"First 20 permutations: {perms[:20]}")
            print(f"Last 20 permutations: {perms[-20:]}")
        
        # Additional operations
        print("\nAdditional operations:")
        print("1. Find nth permutation")
        print("2. Find next permutation")
        print("3. Find permutation rank")
        print("4. Generate k-length permutations")
        
        choice = input("Choose operation (1-4, or press Enter to skip): ").strip()
        
        if choice == '1':
            try:
                n = int(input(f"Enter index (0 to {total_count-1}): "))
                nth_perm = nth_permutation(user_input, n)
                print(f"Permutation at index {n}: '{nth_perm}'")
            except ValueError:
                print("Invalid index!")
        
        elif choice == '2':
            next_perm = next_permutation(user_input)
            print(f"Next permutation: {next_perm if next_perm else 'No next permutation'}")
        
        elif choice == '3':
            rank = permutation_rank(user_input)
            print(f"Rank of '{user_input}': {rank}")
        
        elif choice == '4':
            try:
                k = int(input(f"Enter k (1 to {len(user_input)}): "))
                k_perms = permutations_of_length_k(user_input, k)
                print(f"K-length permutations ({len(k_perms)}): {k_perms}")
            except ValueError:
                print("Invalid k value!")
        
        print()

if __name__ == "__main__":
    main()