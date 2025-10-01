"""
PrepInsta Array Problem 5: Remove duplicates from array
"""

def remove_duplicates_set(arr):
    """
    Remove duplicates using set (doesn't preserve order)
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Array without duplicates
    """
    return list(set(arr))

def remove_duplicates_preserve_order(arr):
    """
    Remove duplicates while preserving order
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Array without duplicates (order preserved)
    """
    seen = set()
    result = []
    
    for element in arr:
        if element not in seen:
            seen.add(element)
            result.append(element)
    
    return result

def remove_duplicates_dict_fromkeys(arr):
    """
    Remove duplicates using dict.fromkeys() (preserves order in Python 3.7+)
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Array without duplicates (order preserved)
    """
    return list(dict.fromkeys(arr))

def remove_duplicates_two_loops(arr):
    """
    Remove duplicates using nested loops (O(n²) time complexity)
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Array without duplicates
    """
    result = []
    
    for i, element in enumerate(arr):
        is_duplicate = False
        for j in range(i):
            if arr[j] == element:
                is_duplicate = True
                break
        
        if not is_duplicate:
            result.append(element)
    
    return result

def remove_duplicates_sorted(arr):
    """
    Remove duplicates from sorted array efficiently
    
    Args:
        arr (list): Sorted input array
    
    Returns:
        list: Array without duplicates
    """
    if not arr:
        return []
    
    result = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result.append(arr[i])
    
    return result

def count_duplicates(arr):
    """
    Count occurrences of each element
    
    Args:
        arr (list): Input array
    
    Returns:
        dict: Dictionary with element counts
    """
    count_dict = {}
    
    for element in arr:
        count_dict[element] = count_dict.get(element, 0) + 1
    
    return count_dict

def find_duplicates(arr):
    """
    Find all duplicate elements
    
    Args:
        arr (list): Input array
    
    Returns:
        list: List of duplicate elements
    """
    count_dict = count_duplicates(arr)
    return [element for element, count in count_dict.items() if count > 1]

def find_unique_elements(arr):
    """
    Find elements that appear only once
    
    Args:
        arr (list): Input array
    
    Returns:
        list: List of unique elements
    """
    count_dict = count_duplicates(arr)
    return [element for element, count in count_dict.items() if count == 1]

def remove_specific_duplicates(arr, keep='first'):
    """
    Remove duplicates with option to keep first or last occurrence
    
    Args:
        arr (list): Input array
        keep (str): 'first' or 'last' occurrence to keep
    
    Returns:
        list: Array without duplicates
    """
    if keep == 'first':
        return remove_duplicates_preserve_order(arr)
    elif keep == 'last':
        # Reverse array, remove duplicates, then reverse again
        reversed_arr = arr[::-1]
        no_duplicates = remove_duplicates_preserve_order(reversed_arr)
        return no_duplicates[::-1]
    else:
        return arr

def remove_duplicates_in_place(arr):
    """
    Remove duplicates in-place (modifies original array)
    
    Args:
        arr (list): Input array to modify
    
    Returns:
        list: Modified array reference
    """
    seen = set()
    i = 0
    
    while i < len(arr):
        if arr[i] in seen:
            arr.pop(i)
        else:
            seen.add(arr[i])
            i += 1
    
    return arr

def find_first_duplicate(arr):
    """
    Find the first duplicate element in array
    
    Args:
        arr (list): Input array
    
    Returns:
        element or None: First duplicate element or None if no duplicates
    """
    seen = set()
    
    for element in arr:
        if element in seen:
            return element
        seen.add(element)
    
    return None

def find_most_frequent_element(arr):
    """
    Find the most frequently occurring element
    
    Args:
        arr (list): Input array
    
    Returns:
        tuple: (element, frequency) or (None, 0) if array is empty
    """
    if not arr:
        return None, 0
    
    count_dict = count_duplicates(arr)
    most_frequent = max(count_dict.items(), key=lambda x: x[1])
    
    return most_frequent

def main():
    # Test arrays
    test_arrays = [
        [1, 2, 3, 2, 4, 1, 5],
        ['a', 'b', 'c', 'b', 'd', 'a'],
        [1, 1, 1, 1],
        [1, 2, 3, 4, 5],
        [],
        [5, 3, 8, 3, 9, 5, 2, 8, 1]
    ]
    
    print("Remove duplicates methods comparison:")
    print("-" * 70)
    print(f"{'Original':<25} {'Set':<15} {'Preserve Order':<15} {'Dict Keys':<15}")
    print("-" * 70)
    
    for arr in test_arrays:
        set_result = remove_duplicates_set(arr)
        preserve_result = remove_duplicates_preserve_order(arr)
        dict_result = remove_duplicates_dict_fromkeys(arr)
        
        orig_str = str(arr) if len(str(arr)) <= 24 else str(arr)[:21] + "..."
        set_str = str(set_result) if len(str(set_result)) <= 14 else str(set_result)[:11] + "..."
        preserve_str = str(preserve_result) if len(str(preserve_result)) <= 14 else str(preserve_result)[:11] + "..."
        dict_str = str(dict_result) if len(str(dict_result)) <= 14 else str(dict_result)[:11] + "..."
        
        print(f"{orig_str:<25} {set_str:<15} {preserve_str:<15} {dict_str:<15}")
    
    # Test duplicate analysis
    print("\nDuplicate analysis:")
    print("-" * 30)
    test_arr = [1, 2, 3, 2, 4, 1, 5, 3, 6, 1]
    
    count_dict = count_duplicates(test_arr)
    duplicates = find_duplicates(test_arr)
    unique_elements = find_unique_elements(test_arr)
    first_duplicate = find_first_duplicate(test_arr)
    most_frequent = find_most_frequent_element(test_arr)
    
    print(f"Original array: {test_arr}")
    print(f"Element counts: {count_dict}")
    print(f"Duplicate elements: {duplicates}")
    print(f"Unique elements: {unique_elements}")
    print(f"First duplicate: {first_duplicate}")
    print(f"Most frequent: {most_frequent[0]} (appears {most_frequent[1]} times)")
    
    # Test keep first vs last
    print("\nKeep first vs last occurrence:")
    print("-" * 35)
    test_arr = ['a', 'b', 'c', 'b', 'd', 'a', 'e']
    
    keep_first = remove_specific_duplicates(test_arr, 'first')
    keep_last = remove_specific_duplicates(test_arr, 'last')
    
    print(f"Original: {test_arr}")
    print(f"Keep first: {keep_first}")
    print(f"Keep last: {keep_last}")
    
    # Test sorted array optimization
    print("\nSorted array duplicate removal:")
    print("-" * 35)
    sorted_arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    sorted_result = remove_duplicates_sorted(sorted_arr)
    
    print(f"Sorted array: {sorted_arr}")
    print(f"Without duplicates: {sorted_result}")
    
    # Test in-place removal
    print("\nIn-place duplicate removal:")
    print("-" * 30)
    test_arr_copy = [1, 2, 3, 2, 4, 1, 5].copy()
    original = test_arr_copy.copy()
    
    print(f"Before: {original}")
    remove_duplicates_in_place(test_arr_copy)
    print(f"After: {test_arr_copy}")
    
    # Performance comparison
    print("\nPerformance comparison (large array):")
    print("-" * 40)
    
    import time
    import random
    
    # Create large array with duplicates
    large_arr = [random.randint(1, 100) for _ in range(1000)]
    
    methods = [
        ("Set method", remove_duplicates_set),
        ("Preserve order", remove_duplicates_preserve_order),
        ("Dict fromkeys", remove_duplicates_dict_fromkeys),
        ("Two loops", remove_duplicates_two_loops)
    ]
    
    for name, method in methods:
        start_time = time.time()
        result = method(large_arr)
        end_time = time.time()
        print(f"{name}: {(end_time - start_time) * 1000:.4f} ms ({len(result)} unique elements)")
    
    # Interactive input
    print("\nEnter array elements separated by spaces (or 'quit' to exit):")
    while True:
        user_input = input("Array: ")
        if user_input.lower() == 'quit':
            break
        try:
            # Try to parse as numbers first, then as strings
            try:
                arr = [float(x) for x in user_input.split()]
            except ValueError:
                arr = user_input.split()
            
            if not arr:
                print("Please enter at least one element!")
                continue
            
            print(f"Original: {arr}")
            
            # Show different methods
            no_duplicates = remove_duplicates_preserve_order(arr)
            duplicates = find_duplicates(arr)
            count_dict = count_duplicates(arr)
            
            print(f"Without duplicates: {no_duplicates}")
            print(f"Duplicate elements: {duplicates}")
            print(f"Element counts: {count_dict}")
            
            if duplicates:
                first_dup = find_first_duplicate(arr)
                most_freq = find_most_frequent_element(arr)
                print(f"First duplicate: {first_dup}")
                print(f"Most frequent: {most_freq[0]} (appears {most_freq[1]} times)")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()