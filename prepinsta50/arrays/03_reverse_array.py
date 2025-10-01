"""
PrepInsta Array Problem 3: Reverse an array
"""

def reverse_array_slicing(arr):
    """
    Reverse array using slicing
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Reversed array
    """
    return arr[::-1]

def reverse_array_builtin(arr):
    """
    Reverse array using built-in reverse() method
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Reversed array
    """
    reversed_arr = arr.copy()
    reversed_arr.reverse()
    return reversed_arr

def reverse_array_loop(arr):
    """
    Reverse array using loop
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Reversed array
    """
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

def reverse_array_two_pointers(arr):
    """
    Reverse array in-place using two pointers
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Reversed array (modified in-place)
    """
    arr_copy = arr.copy()
    left = 0
    right = len(arr_copy) - 1
    
    while left < right:
        arr_copy[left], arr_copy[right] = arr_copy[right], arr_copy[left]
        left += 1
        right -= 1
    
    return arr_copy

def reverse_array_recursive(arr):
    """
    Reverse array using recursion
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Reversed array
    """
    if len(arr) <= 1:
        return arr
    return [arr[-1]] + reverse_array_recursive(arr[:-1])

def reverse_array_stack(arr):
    """
    Reverse array using stack approach
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Reversed array
    """
    stack = []
    
    # Push all elements to stack
    for element in arr:
        stack.append(element)
    
    # Pop all elements to create reversed array
    reversed_arr = []
    while stack:
        reversed_arr.append(stack.pop())
    
    return reversed_arr

def reverse_subarray(arr, start, end):
    """
    Reverse a subarray from start to end index
    
    Args:
        arr (list): Input array
        start (int): Start index
        end (int): End index
    
    Returns:
        list: Array with reversed subarray
    """
    if start < 0 or end >= len(arr) or start > end:
        return arr.copy()
    
    result = arr.copy()
    while start < end:
        result[start], result[end] = result[end], result[start]
        start += 1
        end -= 1
    
    return result

def reverse_words_in_array(arr):
    """
    Reverse each string element in the array
    
    Args:
        arr (list): Input array of strings
    
    Returns:
        list: Array with each string reversed
    """
    return [str(element)[::-1] if isinstance(element, str) else element for element in arr]

def rotate_array_left(arr, k):
    """
    Rotate array to the left by k positions
    
    Args:
        arr (list): Input array
        k (int): Number of positions to rotate
    
    Returns:
        list: Rotated array
    """
    if not arr or k == 0:
        return arr.copy()
    
    k = k % len(arr)  # Handle k > len(arr)
    return arr[k:] + arr[:k]

def rotate_array_right(arr, k):
    """
    Rotate array to the right by k positions
    
    Args:
        arr (list): Input array
        k (int): Number of positions to rotate
    
    Returns:
        list: Rotated array
    """
    if not arr or k == 0:
        return arr.copy()
    
    k = k % len(arr)  # Handle k > len(arr)
    return arr[-k:] + arr[:-k]

def main():
    # Test arrays
    test_arrays = [
        [1, 2, 3, 4, 5],
        ['a', 'b', 'c', 'd'],
        [10],
        [],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ['hello', 'world', 'python']
    ]
    
    print("Array reversal methods:")
    print("-" * 60)
    print(f"{'Original':<20} {'Slicing':<15} {'Built-in':<15} {'Loop':<15}")
    print("-" * 60)
    
    for arr in test_arrays:
        slicing_result = reverse_array_slicing(arr)
        builtin_result = reverse_array_builtin(arr)
        loop_result = reverse_array_loop(arr)
        
        orig_str = str(arr) if len(str(arr)) <= 19 else str(arr)[:16] + "..."
        slice_str = str(slicing_result) if len(str(slicing_result)) <= 14 else str(slicing_result)[:11] + "..."
        builtin_str = str(builtin_result) if len(str(builtin_result)) <= 14 else str(builtin_result)[:11] + "..."
        loop_str = str(loop_result) if len(str(loop_result)) <= 14 else str(loop_result)[:11] + "..."
        
        print(f"{orig_str:<20} {slice_str:<15} {builtin_str:<15} {loop_str:<15}")
    
    # Test two pointers and recursive methods
    print("\nTwo pointers and recursive methods:")
    print("-" * 45)
    test_arr = [1, 2, 3, 4, 5, 6]
    
    two_pointers_result = reverse_array_two_pointers(test_arr)
    recursive_result = reverse_array_recursive(test_arr)
    stack_result = reverse_array_stack(test_arr)
    
    print(f"Original: {test_arr}")
    print(f"Two pointers: {two_pointers_result}")
    print(f"Recursive: {recursive_result}")
    print(f"Stack: {stack_result}")
    
    # Test subarray reversal
    print("\nSubarray reversal:")
    print("-" * 25)
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8]
    
    print(f"Original: {test_arr}")
    print(f"Reverse subarray [2:5]: {reverse_subarray(test_arr, 2, 5)}")
    print(f"Reverse subarray [0:3]: {reverse_subarray(test_arr, 0, 3)}")
    print(f"Reverse subarray [4:7]: {reverse_subarray(test_arr, 4, 7)}")
    
    # Test string reversal in array
    print("\nReverse strings in array:")
    print("-" * 30)
    string_arr = ['hello', 'world', 'python', 'programming']
    reversed_strings = reverse_words_in_array(string_arr)
    
    print(f"Original: {string_arr}")
    print(f"Reversed strings: {reversed_strings}")
    
    # Test array rotation
    print("\nArray rotation:")
    print("-" * 20)
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8]
    
    print(f"Original: {test_arr}")
    print(f"Rotate left by 3: {rotate_array_left(test_arr, 3)}")
    print(f"Rotate right by 3: {rotate_array_right(test_arr, 3)}")
    print(f"Rotate left by 10: {rotate_array_left(test_arr, 10)}")  # k > len(arr)
    
    # Performance comparison for large array
    print("\nPerformance test (large array):")
    print("-" * 35)
    large_arr = list(range(1000))
    
    import time
    
    methods = [
        ("Slicing", reverse_array_slicing),
        ("Built-in", reverse_array_builtin),
        ("Two pointers", reverse_array_two_pointers),
        ("Stack", reverse_array_stack)
    ]
    
    for name, method in methods:
        start_time = time.time()
        result = method(large_arr)
        end_time = time.time()
        print(f"{name}: {(end_time - start_time) * 1000:.4f} ms")
    
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
            
            reversed_arr = reverse_array_slicing(arr)
            print(f"Original: {arr}")
            print(f"Reversed: {reversed_arr}")
            
            # Ask for rotation
            try:
                k = int(input("Enter rotation amount (0 to skip): "))
                if k != 0:
                    left_rotated = rotate_array_left(arr, k)
                    right_rotated = rotate_array_right(arr, k)
                    print(f"Rotated left by {k}: {left_rotated}")
                    print(f"Rotated right by {k}: {right_rotated}")
            except ValueError:
                pass
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()