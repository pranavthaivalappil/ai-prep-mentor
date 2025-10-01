"""
PrepInsta Array Problem 4: Sort an array
"""

def bubble_sort(arr):
    """
    Sort array using bubble sort algorithm
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Sorted array
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_copy[j] > arr_copy[j + 1]:
                arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr_copy

def selection_sort(arr):
    """
    Sort array using selection sort algorithm
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Sorted array
    """
    arr_copy = arr.copy()
    n = len(arr_copy)
    
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr_copy[j] < arr_copy[min_idx]:
                min_idx = j
        
        arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
    
    return arr_copy

def insertion_sort(arr):
    """
    Sort array using insertion sort algorithm
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Sorted array
    """
    arr_copy = arr.copy()
    
    for i in range(1, len(arr_copy)):
        key = arr_copy[i]
        j = i - 1
        
        while j >= 0 and arr_copy[j] > key:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        
        arr_copy[j + 1] = key
    
    return arr_copy

def merge_sort(arr):
    """
    Sort array using merge sort algorithm
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Sorted array
    """
    if len(arr) <= 1:
        return arr.copy()
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    """
    Merge two sorted arrays
    
    Args:
        left (list): Left sorted array
        right (list): Right sorted array
    
    Returns:
        list: Merged sorted array
    """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def quick_sort(arr):
    """
    Sort array using quick sort algorithm
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Sorted array
    """
    if len(arr) <= 1:
        return arr.copy()
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def counting_sort(arr):
    """
    Sort array using counting sort (for non-negative integers)
    
    Args:
        arr (list): Input array of non-negative integers
    
    Returns:
        list: Sorted array
    """
    if not arr:
        return []
    
    # Check if all elements are non-negative integers
    if not all(isinstance(x, int) and x >= 0 for x in arr):
        return sorted(arr)  # Fallback to built-in sort
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    # Count occurrences
    for num in arr:
        count[num] += 1
    
    # Build sorted array
    result = []
    for i, freq in enumerate(count):
        result.extend([i] * freq)
    
    return result

def builtin_sort(arr):
    """
    Sort array using built-in sorted() function
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Sorted array
    """
    return sorted(arr)

def sort_descending(arr):
    """
    Sort array in descending order
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Array sorted in descending order
    """
    return sorted(arr, reverse=True)

def sort_by_absolute_value(arr):
    """
    Sort array by absolute values
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Array sorted by absolute values
    """
    return sorted(arr, key=abs)

def sort_strings_by_length(arr):
    """
    Sort array of strings by length
    
    Args:
        arr (list): Input array of strings
    
    Returns:
        list: Array sorted by string length
    """
    return sorted(arr, key=len)

def is_sorted(arr):
    """
    Check if array is sorted in ascending order
    
    Args:
        arr (list): Input array
    
    Returns:
        bool: True if sorted, False otherwise
    """
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

def main():
    # Test arrays
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 4, 6, 1, 3],
        [1],
        [],
        [3, 3, 3, 3],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]
    ]
    
    print("Sorting algorithms comparison:")
    print("-" * 80)
    print(f"{'Original':<20} {'Bubble':<15} {'Selection':<15} {'Insertion':<15} {'Built-in':<15}")
    print("-" * 80)
    
    for arr in test_arrays:
        if len(arr) <= 10:  # Only test complex algorithms on small arrays
            bubble_result = bubble_sort(arr)
            selection_result = selection_sort(arr)
            insertion_result = insertion_sort(arr)
        else:
            bubble_result = "Too large"
            selection_result = "Too large"
            insertion_result = "Too large"
        
        builtin_result = builtin_sort(arr)
        
        orig_str = str(arr) if len(str(arr)) <= 19 else str(arr)[:16] + "..."
        bubble_str = str(bubble_result) if len(str(bubble_result)) <= 14 else str(bubble_result)[:11] + "..."
        selection_str = str(selection_result) if len(str(selection_result)) <= 14 else str(selection_result)[:11] + "..."
        insertion_str = str(insertion_result) if len(str(insertion_result)) <= 14 else str(insertion_result)[:11] + "..."
        builtin_str = str(builtin_result) if len(str(builtin_result)) <= 14 else str(builtin_result)[:11] + "..."
        
        print(f"{orig_str:<20} {bubble_str:<15} {selection_str:<15} {insertion_str:<15} {builtin_str:<15}")
    
    # Test advanced sorting algorithms
    print("\nAdvanced sorting algorithms:")
    print("-" * 50)
    test_arr = [38, 27, 43, 3, 9, 82, 10]
    
    merge_result = merge_sort(test_arr)
    quick_result = quick_sort(test_arr)
    counting_result = counting_sort(test_arr)
    
    print(f"Original: {test_arr}")
    print(f"Merge sort: {merge_result}")
    print(f"Quick sort: {quick_result}")
    print(f"Counting sort: {counting_result}")
    
    # Test special sorting
    print("\nSpecial sorting methods:")
    print("-" * 30)
    
    # Descending order
    desc_result = sort_descending(test_arr)
    print(f"Descending: {desc_result}")
    
    # Sort by absolute value
    mixed_arr = [-5, 3, -1, 4, -2, 6]
    abs_result = sort_by_absolute_value(mixed_arr)
    print(f"Original: {mixed_arr}")
    print(f"By absolute value: {abs_result}")
    
    # Sort strings by length
    string_arr = ['python', 'java', 'c', 'javascript', 'go']
    length_result = sort_strings_by_length(string_arr)
    print(f"Strings: {string_arr}")
    print(f"By length: {length_result}")
    
    # Test sorted check
    print("\nSorted array checking:")
    print("-" * 25)
    test_arrays_sorted = [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1, 3, 2, 4, 5],
        [1, 1, 1, 1],
        []
    ]
    
    for arr in test_arrays_sorted:
        sorted_check = is_sorted(arr)
        print(f"{str(arr):<20} {'Sorted' if sorted_check else 'Not sorted'}")
    
    # Performance comparison
    print("\nPerformance comparison (small array):")
    print("-" * 40)
    
    import time
    test_arr = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50, 42, 30, 18, 6]
    
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Selection Sort", selection_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Built-in Sort", builtin_sort)
    ]
    
    for name, algorithm in algorithms:
        start_time = time.time()
        result = algorithm(test_arr)
        end_time = time.time()
        print(f"{name}: {(end_time - start_time) * 1000:.4f} ms")
    
    # Interactive input
    print("\nEnter array elements separated by spaces (or 'quit' to exit):")
    while True:
        user_input = input("Array: ")
        if user_input.lower() == 'quit':
            break
        try:
            # Try to parse as numbers first
            try:
                arr = [float(x) for x in user_input.split()]
            except ValueError:
                arr = user_input.split()
            
            if not arr:
                print("Please enter at least one element!")
                continue
            
            print(f"Original: {arr}")
            
            # Choose sorting method
            print("Choose sorting method:")
            print("1. Built-in sort (fastest)")
            print("2. Bubble sort")
            print("3. Selection sort")
            print("4. Insertion sort")
            print("5. Merge sort")
            print("6. Quick sort")
            
            choice = input("Enter choice (1-6, default 1): ").strip()
            
            if choice == '2':
                result = bubble_sort(arr)
                method = "Bubble sort"
            elif choice == '3':
                result = selection_sort(arr)
                method = "Selection sort"
            elif choice == '4':
                result = insertion_sort(arr)
                method = "Insertion sort"
            elif choice == '5':
                result = merge_sort(arr)
                method = "Merge sort"
            elif choice == '6':
                result = quick_sort(arr)
                method = "Quick sort"
            else:
                result = builtin_sort(arr)
                method = "Built-in sort"
            
            print(f"{method}: {result}")
            
            # Ask for descending order
            desc_choice = input("Sort in descending order? (y/n): ").lower()
            if desc_choice == 'y':
                desc_result = sort_descending(arr)
                print(f"Descending: {desc_result}")
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()