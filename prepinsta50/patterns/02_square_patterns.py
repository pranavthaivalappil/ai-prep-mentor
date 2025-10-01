"""
PrepInsta Pattern Problem 2: Square patterns
"""

def solid_square(n):
    """
    Print solid square pattern
    ****
    ****
    ****
    ****
    
    Args:
        n (int): Size of square
    """
    print("Solid Square:")
    for i in range(n):
        print('*' * n)
    print()

def hollow_square(n):
    """
    Print hollow square pattern
    ****
    *  *
    *  *
    ****
    
    Args:
        n (int): Size of square
    """
    print("Hollow Square:")
    for i in range(n):
        if i == 0 or i == n - 1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')
    print()

def diagonal_square(n):
    """
    Print square with diagonals
    *  *
     **
     **
    *  *
    
    Args:
        n (int): Size of square
    """
    print("Diagonal Square:")
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print()

def number_square_pattern1(n):
    """
    Print number square pattern
    1234
    1234
    1234
    1234
    
    Args:
        n (int): Size of square
    """
    print("Number Square Pattern 1:")
    for i in range(n):
        for j in range(1, n + 1):
            print(j, end='')
        print()
    print()

def number_square_pattern2(n):
    """
    Print number square pattern
    1111
    2222
    3333
    4444
    
    Args:
        n (int): Size of square
    """
    print("Number Square Pattern 2:")
    for i in range(1, n + 1):
        print(str(i) * n)
    print()

def number_square_pattern3(n):
    """
    Print number square pattern
    1234
    2341
    3412
    4123
    
    Args:
        n (int): Size of square
    """
    print("Number Square Pattern 3:")
    for i in range(n):
        for j in range(n):
            num = ((i + j) % n) + 1
            print(num, end='')
        print()
    print()

def alphabet_square_pattern1(n):
    """
    Print alphabet square pattern
    ABCD
    ABCD
    ABCD
    ABCD
    
    Args:
        n (int): Size of square
    """
    print("Alphabet Square Pattern 1:")
    for i in range(n):
        for j in range(n):
            print(chr(ord('A') + j), end='')
        print()
    print()

def alphabet_square_pattern2(n):
    """
    Print alphabet square pattern
    AAAA
    BBBB
    CCCC
    DDDD
    
    Args:
        n (int): Size of square
    """
    print("Alphabet Square Pattern 2:")
    for i in range(n):
        print(chr(ord('A') + i) * n)
    print()

def checkerboard_pattern(n):
    """
    Print checkerboard pattern
    * * 
     * *
    * * 
     * *
    
    Args:
        n (int): Size of square
    """
    print("Checkerboard Pattern:")
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()
    print()

def border_square_pattern(n):
    """
    Print border square pattern with numbers
    11111
    12221
    12321
    12221
    11111
    
    Args:
        n (int): Size of square
    """
    print("Border Square Pattern:")
    for i in range(n):
        for j in range(n):
            # Distance from border
            distance = min(i, j, n - 1 - i, n - 1 - j) + 1
            print(distance, end='')
        print()
    print()

def spiral_square_pattern(n):
    """
    Print spiral square pattern
    1234
    1234
    1234
    1234
    
    Args:
        n (int): Size of square
    """
    print("Spiral Square Pattern:")
    
    # Create matrix
    matrix = [[0] * n for _ in range(n)]
    
    # Fill spiral
    num = 1
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    
    while top <= bottom and left <= right:
        # Fill top row
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1
        
        # Fill right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # Fill bottom row
        if top <= bottom:
            for j in range(right, left - 1, -1):
                matrix[bottom][j] = num
                num += 1
            bottom -= 1
        
        # Fill left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
    
    # Print matrix
    for row in matrix:
        for num in row:
            print(f"{num:2d}", end=' ')
        print()
    print()

def cross_pattern(n):
    """
    Print cross pattern
      *
      *
    *****
      *
      *
    
    Args:
        n (int): Size of square (should be odd)
    """
    print("Cross Pattern:")
    mid = n // 2
    
    for i in range(n):
        for j in range(n):
            if i == mid or j == mid:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print()

def x_pattern(n):
    """
    Print X pattern
    *   *
     * *
      *
     * *
    *   *
    
    Args:
        n (int): Size of square
    """
    print("X Pattern:")
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
    print()

def plus_pattern(n):
    """
    Print plus pattern (similar to cross but with specific spacing)
      *
      *
    *****
      *
      *
    
    Args:
        n (int): Size of square (should be odd)
    """
    print("Plus Pattern:")
    mid = n // 2
    
    for i in range(n):
        if i == mid:
            print('*' * n)
        else:
            print(' ' * mid + '*')
    print()

def diamond_in_square(n):
    """
    Print diamond pattern inside square
       *
      ***
     *****
      ***
       *
    
    Args:
        n (int): Size of square (should be odd)
    """
    print("Diamond in Square:")
    mid = n // 2
    
    for i in range(n):
        spaces = abs(mid - i)
        stars = n - 2 * spaces
        
        if stars > 0:
            print(' ' * spaces + '*' * stars)
        else:
            print()
    print()

def main():
    print("Square Pattern Demonstrations")
    print("=" * 40)
    
    n = 5  # Size of square for demonstrations
    
    # Basic square patterns
    solid_square(n)
    hollow_square(n)
    diagonal_square(n)
    
    # Number patterns
    number_square_pattern1(n)
    number_square_pattern2(n)
    number_square_pattern3(n)
    
    # Alphabet patterns
    alphabet_square_pattern1(n)
    alphabet_square_pattern2(n)
    
    # Special patterns
    checkerboard_pattern(n)
    border_square_pattern(n)
    spiral_square_pattern(n)
    cross_pattern(n)
    x_pattern(n)
    plus_pattern(n)
    diamond_in_square(n)
    
    # Interactive section
    print("Interactive Square Pattern Generator")
    print("=" * 40)
    
    while True:
        print("\nAvailable patterns:")
        print("1. Solid Square")
        print("2. Hollow Square")
        print("3. Diagonal Square")
        print("4. Number Square Pattern 1")
        print("5. Number Square Pattern 2")
        print("6. Number Square Pattern 3")
        print("7. Alphabet Square Pattern 1")
        print("8. Alphabet Square Pattern 2")
        print("9. Checkerboard Pattern")
        print("10. Border Square Pattern")
        print("11. Spiral Square Pattern")
        print("12. Cross Pattern")
        print("13. X Pattern")
        print("14. Plus Pattern")
        print("15. Diamond in Square")
        print("0. Quit")
        
        try:
            choice = int(input("\nEnter your choice (0-15): "))
            
            if choice == 0:
                print("Goodbye!")
                break
            
            if choice < 1 or choice > 15:
                print("Invalid choice! Please enter a number between 0 and 15.")
                continue
            
            size = int(input("Enter size of square: "))
            
            if size <= 0:
                print("Size must be positive!")
                continue
            
            if size > 20:
                print("Size too large! Please enter a number <= 20.")
                continue
            
            # Some patterns work better with odd sizes
            if choice in [12, 14, 15] and size % 2 == 0:
                print(f"Pattern works better with odd size. Using {size + 1} instead.")
                size += 1
            
            print(f"\nPattern with size {size}:")
            print("-" * 30)
            
            if choice == 1:
                solid_square(size)
            elif choice == 2:
                hollow_square(size)
            elif choice == 3:
                diagonal_square(size)
            elif choice == 4:
                number_square_pattern1(size)
            elif choice == 5:
                number_square_pattern2(size)
            elif choice == 6:
                number_square_pattern3(size)
            elif choice == 7:
                alphabet_square_pattern1(size)
            elif choice == 8:
                alphabet_square_pattern2(size)
            elif choice == 9:
                checkerboard_pattern(size)
            elif choice == 10:
                border_square_pattern(size)
            elif choice == 11:
                spiral_square_pattern(size)
            elif choice == 12:
                cross_pattern(size)
            elif choice == 13:
                x_pattern(size)
            elif choice == 14:
                plus_pattern(size)
            elif choice == 15:
                diamond_in_square(size)
            
        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()