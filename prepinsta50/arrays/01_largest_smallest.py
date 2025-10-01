"""
PrepInsta Array Problem 1: Find largest and smallest elements in array
"""

def find_largest_smallest(arr):
    """
    Find largest and smallest elements in array
    
    Args:
        arr (list): Input array
    
    Returns:
        tuple: (largest, smallest) or (None, None) if array is empty
    """
    if not arr:
        return None, None
    
    largest = smallest = arr[0]
    
    for element in arr[1:]:
        if element > largest:
            largest = element
        if element < smallest:
            smallest = element
    
    return largest, smallest

def find_largest_smallest_builtin(arr):
    """
    Find largest and smallest using built-in functions
    
    Args:
        arr (list): Input array
    
    Returns:
        tuple: (largest, smallest) or (None, None) if array is empty
    """
    if not arr:
        return None, None
    
    return max(arr), min(arr)

def find_second_largest_smallest(arr):
    """
    Find second largest and second smallest elements
    
    Args:
        arr (list): Input array
    
    Returns:
        tuple: (second_largest, second_smallest) or (None, None) if not enough elements
    """
    if len(arr) < 2:
        return None, None
    
    # Remove duplicates and sort
    unique_elements = list(set(arr))
    if len(unique_elements) < 2:
        return None, None
    
    unique_elements.sort()
    return unique_elements[-2], unique_elements[1]

def find_kth_largest_smallest(arr, k):
    """
    Find kth largest and kth smallest elements
    
    Args:
        arr (list): Input array
        k (int): Position (1-indexed)
    
    Returns:
        tuple: (kth_largest, kth_smallest) or (None, None) if k is invalid
    """
    if not arr or k <= 0 or k > len(arr):
        return None, None
    
    # Sort array for kth elements
    sorted_arr = sorted(arr)
    kth_smallest = sorted_arr[k - 1]
    kth_largest = sorted_arr[-k]
    
    return kth_largest, kth_smallest

def find_largest_smallest_indices(arr):
    """
    Find indices of largest and smallest elements
    
    Args:
        arr (list): Input array
    
    Returns:
        tuple: (largest_index, smallest_index) or (None, None) if array is empty
    """
    if not arr:
        return None, None
    
    largest_idx = smallest_idx = 0
    
    for i in range(1, len(arr)):
        if arr[i] > arr[largest_idx]:
            largest_idx = i
        if arr[i] < arr[smallest_idx]:
            smallest_idx = i
    
    return largest_idx, smallest_idx

def find_range_and_difference(arr):
    """
    Find range (max - min) and other statistics
    
    Args:
        arr (list): Input array
    
    Returns:
        dict: Statistics about the array
    """
    if not arr:
        return None
    
    largest, smallest = find_largest_smallest(arr)
    
    return {
        'largest': largest,
        'smallest': smallest,
        'range': largest - smallest,
        'sum': sum(arr),
        'average': sum(arr) / len(arr),
        'count': len(arr)
    }

def main():
    # Test arrays
    test_arrays = [
        [3, 5, 1, 9, 2, 8],
        [10],
        [],
        [-5, -2, -10, -1],
        [5, 5, 5, 5],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]
    
    print("Finding largest and smallest elements:")
    print("-" * 45)
    print(f"{'Array':<25} {'Largest':<8} {'Smallest':<8}")
    print("-" * 45)
    
    for arr in test_arrays:
        largest, smallest = find_largest_smallest(arr)
        arr_str = str(arr) if len(str(arr)) <= 24 else str(arr)[:21] + "..."
        print(f"{arr_str:<25} {largest:<8} {smallest:<8}")
    
    # Test with built-in functions
    print("\nComparison with built-in functions:")
    print("-" * 40)
    test_arr = [3, 5, 1, 9, 2, 8]
    
    custom_result = find_largest_smallest(test_arr)
    builtin_result = find_largest_smallest_builtin(test_arr)
    
    print(f"Array: {test_arr}")
    print(f"Custom method: Largest = {custom_result[0]}, Smallest = {custom_result[1]}")
    print(f"Built-in method: Largest = {builtin_result[0]}, Smallest = {builtin_result[1]}")
    
    # Test second largest and smallest
    print("\nSecond largest and smallest:")
    print("-" * 35)
    for arr in test_arrays:
        if len(arr) >= 2:
            second_largest, second_smallest = find_second_largest_smallest(arr)
            print(f"{str(arr)[:30]:<30} 2nd Largest: {second_largest}, 2nd Smallest: {second_smallest}")
    
    # Test kth largest and smallest
    print("\nKth largest and smallest (k=3):")
    print("-" * 35)
    k = 3
    for arr in test_arrays:
        if len(arr) >= k:
            kth_largest, kth_smallest = find_kth_largest_smallest(arr, k)
            print(f"{str(arr)[:30]:<30} {k}rd Largest: {kth_largest}, {k}rd Smallest: {kth_smallest}")
    
    # Test indices
    print("\nIndices of largest and smallest:")
    print("-" * 35)
    for arr in test_arrays:
        if arr:
            largest_idx, smallest_idx = find_largest_smallest_indices(arr)
            print(f"{str(arr)[:30]:<30} Largest at index {largest_idx}, Smallest at index {smallest_idx}")
    
    # Test statistics
    print("\nArray statistics:")
    print("-" * 20)
    test_arr = [3, 5, 1, 9, 2, 8]
    stats = find_range_and_difference(test_arr)
    
    print(f"Array: {test_arr}")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")
    
    # Interactive input
    print("\nEnter array elements separated by spaces (or 'quit' to exit):")
    while True:
        user_input = input("Array: ")
        if user_input.lower() == 'quit':
            break
        try:
            arr = [float(x) for x in user_input.split()]
            if not arr:
                print("Please enter at least one number!")
                continue
            
            largest, smallest = find_largest_smallest(arr)
            largest_idx, smallest_idx = find_largest_smallest_indices(arr)
            stats = find_range_and_difference(arr)
            
            print(f"Largest: {largest} (at index {largest_idx})")
            print(f"Smallest: {smallest} (at index {smallest_idx})")
            print(f"Range: {stats['range']}")
            print(f"Average: {stats['average']:.2f}")
            
        except ValueError:
            print("Please enter valid numbers!")

if __name__ == "__main__":
    main()