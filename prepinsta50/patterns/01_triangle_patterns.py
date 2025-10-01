"""
PrepInsta Pattern Problem 1: Triangle patterns
"""

def right_triangle_stars(n):
    """
    Print right triangle pattern with stars
    *
    **
    ***
    ****
    
    Args:
        n (int): Number of rows
    """
    print("Right Triangle (Stars):")
    for i in range(1, n + 1):
        print('*' * i)
    print()

def right_triangle_numbers(n):
    """
    Print right triangle pattern with numbers
    1
    12
    123
    1234
    
    Args:
        n (int): Number of rows
    """
    print("Right Triangle (Numbers):")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end='')
        print()
    print()

def right_triangle_same_numbers(n):
    """
    Print right triangle pattern with same numbers
    1
    22
    333
    4444
    
    Args:
        n (int): Number of rows
    """
    print("Right Triangle (Same Numbers):")
    for i in range(1, n + 1):
        print(str(i) * i)
    print()

def inverted_right_triangle(n):
    """
    Print inverted right triangle pattern
    ****
    ***
    **
    *
    
    Args:
        n (int): Number of rows
    """
    print("Inverted Right Triangle:")
    for i in range(n, 0, -1):
        print('*' * i)
    print()

def left_triangle_stars(n):
    """
    Print left triangle pattern with stars
       *
      **
     ***
    ****
    
    Args:
        n (int): Number of rows
    """
    print("Left Triangle (Stars):")
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * i)
    print()

def equilateral_triangle(n):
    """
    Print equilateral triangle pattern
       *
      ***
     *****
    *******
    
    Args:
        n (int): Number of rows
    """
    print("Equilateral Triangle:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    print()

def inverted_equilateral_triangle(n):
    """
    Print inverted equilateral triangle pattern
    *******
     *****
      ***
       *
    
    Args:
        n (int): Number of rows
    """
    print("Inverted Equilateral Triangle:")
    for i in range(n, 0, -1):
        spaces = ' ' * (n - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    print()

def hollow_right_triangle(n):
    """
    Print hollow right triangle pattern
    *
    **
    * *
    ****
    
    Args:
        n (int): Number of rows
    """
    print("Hollow Right Triangle:")
    for i in range(1, n + 1):
        if i == 1 or i == n:
            print('*' * i)
        else:
            print('*' + ' ' * (i - 2) + '*')
    print()

def hollow_equilateral_triangle(n):
    """
    Print hollow equilateral triangle pattern
       *
      * *
     *   *
    *******
    
    Args:
        n (int): Number of rows
    """
    print("Hollow Equilateral Triangle:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        if i == 1:
            print(spaces + '*')
        elif i == n:
            print(spaces + '*' * (2 * i - 1))
        else:
            print(spaces + '*' + ' ' * (2 * i - 3) + '*')
    print()

def pascal_triangle(n):
    """
    Print Pascal's triangle
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    
    Args:
        n (int): Number of rows
    """
    print("Pascal's Triangle:")
    
    def binomial_coefficient(n, k):
        if k == 0 or k == n:
            return 1
        return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)
    
    for i in range(n):
        # Print leading spaces
        print(' ' * (n - i - 1), end='')
        
        # Print numbers
        for j in range(i + 1):
            print(binomial_coefficient(i, j), end=' ')
        print()
    print()

def floyd_triangle(n):
    """
    Print Floyd's triangle
    1
    2 3
    4 5 6
    7 8 9 10
    
    Args:
        n (int): Number of rows
    """
    print("Floyd's Triangle:")
    num = 1
    for i in range(1, n + 1):
        for j in range(i):
            print(num, end=' ')
            num += 1
        print()
    print()

def number_triangle_pattern1(n):
    """
    Print number triangle pattern
    1
    1 2
    1 2 3
    1 2 3 4
    
    Args:
        n (int): Number of rows
    """
    print("Number Triangle Pattern 1:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()
    print()

def number_triangle_pattern2(n):
    """
    Print number triangle pattern
       1
      2 2
     3 3 3
    4 4 4 4
    
    Args:
        n (int): Number of rows
    """
    print("Number Triangle Pattern 2:")
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        numbers = (str(i) + ' ') * i
        print(spaces + numbers.rstrip())
    print()

def alphabet_triangle(n):
    """
    Print alphabet triangle pattern
    A
    AB
    ABC
    ABCD
    
    Args:
        n (int): Number of rows
    """
    print("Alphabet Triangle:")
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(ord('A') + j), end='')
        print()
    print()

def main():
    print("Triangle Pattern Demonstrations")
    print("=" * 40)
    
    n = 5  # Number of rows for demonstrations
    
    # Basic triangle patterns
    right_triangle_stars(n)
    right_triangle_numbers(n)
    right_triangle_same_numbers(n)
    inverted_right_triangle(n)
    left_triangle_stars(n)
    
    # Equilateral triangles
    equilateral_triangle(n)
    inverted_equilateral_triangle(n)
    
    # Hollow triangles
    hollow_right_triangle(n)
    hollow_equilateral_triangle(n)
    
    # Special triangles
    pascal_triangle(n)
    floyd_triangle(n)
    number_triangle_pattern1(n)
    number_triangle_pattern2(n)
    alphabet_triangle(n)
    
    # Interactive section
    print("Interactive Triangle Pattern Generator")
    print("=" * 40)
    
    while True:
        print("\nAvailable patterns:")
        print("1. Right Triangle (Stars)")
        print("2. Right Triangle (Numbers)")
        print("3. Left Triangle (Stars)")
        print("4. Equilateral Triangle")
        print("5. Inverted Equilateral Triangle")
        print("6. Hollow Right Triangle")
        print("7. Hollow Equilateral Triangle")
        print("8. Pascal's Triangle")
        print("9. Floyd's Triangle")
        print("10. Number Triangle Pattern 1")
        print("11. Number Triangle Pattern 2")
        print("12. Alphabet Triangle")
        print("0. Quit")
        
        try:
            choice = int(input("\nEnter your choice (0-12): "))
            
            if choice == 0:
                print("Goodbye!")
                break
            
            if choice < 1 or choice > 12:
                print("Invalid choice! Please enter a number between 0 and 12.")
                continue
            
            rows = int(input("Enter number of rows: "))
            
            if rows <= 0:
                print("Number of rows must be positive!")
                continue
            
            if rows > 20:
                print("Too many rows! Please enter a number <= 20.")
                continue
            
            print(f"\nPattern with {rows} rows:")
            print("-" * 30)
            
            if choice == 1:
                right_triangle_stars(rows)
            elif choice == 2:
                right_triangle_numbers(rows)
            elif choice == 3:
                left_triangle_stars(rows)
            elif choice == 4:
                equilateral_triangle(rows)
            elif choice == 5:
                inverted_equilateral_triangle(rows)
            elif choice == 6:
                hollow_right_triangle(rows)
            elif choice == 7:
                hollow_equilateral_triangle(rows)
            elif choice == 8:
                pascal_triangle(rows)
            elif choice == 9:
                floyd_triangle(rows)
            elif choice == 10:
                number_triangle_pattern1(rows)
            elif choice == 11:
                number_triangle_pattern2(rows)
            elif choice == 12:
                alphabet_triangle(rows)
            
        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()