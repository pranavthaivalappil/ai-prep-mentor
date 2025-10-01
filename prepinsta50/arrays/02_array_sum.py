"""
PrepInsta Array Problem 2: Calculate sum of array elements
"""

def array_sum_iterative(arr):
    """
    Calculate sum of array elements using iteration
    
    Args:
        arr (list): Input array
    
    Returns:
        float: Sum of all elements
    """
    total = 0
    for element in arr:
        total += element
    return total

def array_sum_builtin(arr):
    """
    Calculate sum using built-in sum() function
    
    Args:
        arr (list): Input array
    
    Returns:
        float: Sum of all elements
    """
    return sum(arr)

def array_sum_recursive(arr):
    """
    Calculate sum using recursion
    
    Args:
        arr (list): Input array
    
    Returns:
        float: Sum of all elements
    """
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0]
    return arr[0] + array_sum_recursive(arr[1:])

def array_sum_positive_negative(arr):
    """
    Calculate sum of positive and negative elements separately
    
    Args:
        arr (list): Input array
    
    Returns:
        tuple: (positive_sum, negative_sum, total_sum)
    """
    positive_sum = 0
    negative_sum = 0
    
    for element in arr:
        if element > 0:
            positive_sum += element
        elif element < 0:
            negative_sum += element
    
    return positive_sum, negative_sum, positive_sum + negative_sum

def array_sum_even_odd_indices(arr):
    """
    Calculate sum of elements at even and odd indices
    
    Args:
        arr (list): Input array
    
    Returns:
        tuple: (even_index_sum, odd_index_sum)
    """
    even_sum = 0
    odd_sum = 0
    
    for i, element in enumerate(arr):
        if i % 2 == 0:
            even_sum += element
        else:
            odd_sum += element
    
    return even_sum, odd_sum

def array_sum_even_odd_values(arr):
    """
    Calculate sum of even and odd values
    
    Args:
        arr (list): Input array
    
    Returns:
        tuple: (even_values_sum, odd_values_sum)
    """
    even_sum = 0
    odd_sum = 0
    
    for element in arr:
        if isinstance(element, (int, float)) and element == int(element):
            if int(element) % 2 == 0:
                even_sum += element
            else:
                odd_sum += element
    
    return even_sum, odd_sum

def cumulative_sum(arr):
    """
    Calculate cumulative sum array
    
    Args:
        arr (list): Input array
    
    Returns:
        list: Array where each element is sum of all previous elements
    """
    if not arr:
        return []
    
    cum_sum = [arr[0]]
    for i in range(1, len(arr)):
        cum_sum.append(cum_sum[-1] + arr[i])
    
    return cum_sum

def array_average(arr):
    """
    Calculate average of array elements
    
    Args:
        arr (list): Input array
    
    Returns:
        float: Average of elements, None if array is empty
    """
    if not arr:
        return None
    
    return array_sum_builtin(arr) / len(arr)

def array_sum_statistics(arr):
    """
    Calculate comprehensive statistics about array sum
    
    Args:
        arr (list): Input array
    
    Returns:
        dict: Dictionary with various statistics
    """
    if not arr:
        return None
    
    total_sum = array_sum_builtin(arr)
    positive_sum, negative_sum, _ = array_sum_positive_negative(arr)
    even_idx_sum, odd_idx_sum = array_sum_even_odd_indices(arr)
    even_val_sum, odd_val_sum = array_sum_even_odd_values(arr)
    
    return {
        'total_sum': total_sum,
        'average': total_sum / len(arr),
        'positive_sum': positive_sum,
        'negative_sum': negative_sum,
        'even_index_sum': even_idx_sum,
        'odd_index_sum': odd_idx_sum,
        'even_values_sum': even_val_sum,
        'odd_values_sum': odd_val_sum,
        'count': len(arr)
    }

def main():
    # Test arrays
    test_arrays = [
        [1, 2, 3, 4, 5],
        [-1, -2, 3, 4, -5],
        [10],
        [],
        [1.5, 2.5, 3.5],
        [0, 0, 0, 0],
        [1, -1, 2, -2, 3, -3]
    ]
    
    print("Array sum calculations:")
    print("-" * 50)
    print(f"{'Array':<25} {'Iterative':<12} {'Built-in':<12} {'Recursive':<12}")
    print("-" * 50)
    
    for arr in test_arrays:
        iter_sum = array_sum_iterative(arr)
        builtin_sum = array_sum_builtin(arr)
        # Only use recursion for small arrays to avoid stack overflow
        rec_sum = array_sum_recursive(arr) if len(arr) <= 10 else "Stack limit"
        
        arr_str = str(arr) if len(str(arr)) <= 24 else str(arr)[:21] + "..."
        print(f"{arr_str:<25} {iter_sum:<12} {builtin_sum:<12} {rec_sum:<12}")
    
    # Test positive/negative sums
    print("\nPositive and negative sums:")
    print("-" * 40)
    print(f"{'Array':<25} {'Positive':<10} {'Negative':<10} {'Total':<10}")
    print("-" * 40)
    
    for arr in test_arrays:
        if arr:
            pos_sum, neg_sum, total = array_sum_positive_negative(arr)
            arr_str = str(arr) if len(str(arr)) <= 24 else str(arr)[:21] + "..."
            print(f"{arr_str:<25} {pos_sum:<10} {neg_sum:<10} {total:<10}")
    
    # Test even/odd index sums
    print("\nEven and odd index sums:")
    print("-" * 35)
    test_arr = [1, 2, 3, 4, 5, 6, 7, 8]
    even_idx_sum, odd_idx_sum = array_sum_even_odd_indices(test_arr)
    
    print(f"Array: {test_arr}")
    print(f"Even indices (0,2,4,6): {[test_arr[i] for i in range(0, len(test_arr), 2)]} = {even_idx_sum}")
    print(f"Odd indices (1,3,5,7): {[test_arr[i] for i in range(1, len(test_arr), 2)]} = {odd_idx_sum}")
    
    # Test even/odd value sums
    print("\nEven and odd value sums:")
    print("-" * 30)
    even_val_sum, odd_val_sum = array_sum_even_odd_values(test_arr)
    
    even_values = [x for x in test_arr if x % 2 == 0]
    odd_values = [x for x in test_arr if x % 2 == 1]
    
    print(f"Even values: {even_values} = {even_val_sum}")
    print(f"Odd values: {odd_values} = {odd_val_sum}")
    
    # Test cumulative sum
    print("\nCumulative sum:")
    print("-" * 20)
    test_arr = [1, 2, 3, 4, 5]
    cum_sum = cumulative_sum(test_arr)
    
    print(f"Original: {test_arr}")
    print(f"Cumulative: {cum_sum}")
    
    # Test comprehensive statistics
    print("\nComprehensive statistics:")
    print("-" * 30)
    test_arr = [1, -2, 3, -4, 5, 6, -7, 8]
    stats = array_sum_statistics(test_arr)
    
    print(f"Array: {test_arr}")
    for key, value in stats.items():
        if isinstance(value, float):
            print(f"{key.replace('_', ' ').title()}: {value:.2f}")
        else:
            print(f"{key.replace('_', ' ').title()}: {value}")
    
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
            
            total_sum = array_sum_builtin(arr)
            average = array_average(arr)
            pos_sum, neg_sum, _ = array_sum_positive_negative(arr)
            
            print(f"Sum: {total_sum}")
            print(f"Average: {average:.2f}")
            print(f"Positive sum: {pos_sum}")
            print(f"Negative sum: {neg_sum}")
            
        except ValueError:
            print("Please enter valid numbers!")

if __name__ == "__main__":
    main()