"""
PrepInsta Pattern Problem 3: Diamond patterns
"""

def solid_diamond(n):
    """
    Print solid diamond pattern
       *
      ***
     *****
    *******
     *****
      ***
       *
    
    Args:
        n (int): Half size of diamond (should be odd for best results)
    """
    print("Solid Diamond:")
    
    # Upper half (including middle)
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    
    # Lower half
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)
    print()

def hollow_diamond(n):
    """
    Print hollow diamond pattern
       *
      * *
     *   *
    *     *
     *   *
      * *
       *
    
    Args:
        n (int): Half size of diamond
    """
    print("Hollow Diamond:")
    
    # Upper half (including middle)
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        if i == 0:
            print(spaces + '*')
        else:
            inner_spaces = ' ' * (2 * i - 1)
            print(spaces + '*' + inner_spaces + '*')
    
    # Lower half
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)
        if i == 0:
            print(spaces + '*')
        else:
            inner_spaces = ' ' * (2 * i - 1)
            print(spaces + '*' + inner_spaces + '*')
    print()

def number_diamond(n):
    """
    Print number diamond pattern
       1
      121
     12321
    1234321
     12321
      121
       1
    
    Args:
        n (int): Half size of diamond
    """
    print("Number Diamond:")
    
    # Upper half (including middle)
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        
        # Ascending numbers
        ascending = ''.join(str(j) for j in range(1, i + 2))
        # Descending numbers
        descending = ''.join(str(j) for j in range(i, 0, -1))
        
        print(spaces + ascending + descending)
    
    # Lower half
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)
        
        # Ascending numbers
        ascending = ''.join(str(j) for j in range(1, i + 2))
        # Descending numbers
        descending = ''.join(str(j) for j in range(i, 0, -1))
        
        print(spaces + ascending + descending)
    print()

def alphabet_diamond(n):
    """
    Print alphabet diamond pattern
       A
      ABA
     ABCBA
    ABCDCBA
     ABCBA
      ABA
       A
    
    Args:
        n (int): Half size of diamond
    """
    print("Alphabet Diamond:")
    
    # Upper half (including middle)
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        
        # Ascending letters
        ascending = ''.join(chr(ord('A') + j) for j in range(i + 1))
        # Descending letters
        descending = ''.join(chr(ord('A') + j) for j in range(i - 1, -1, -1))
        
        print(spaces + ascending + descending)
    
    # Lower half
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)
        
        # Ascending letters
        ascending = ''.join(chr(ord('A') + j) for j in range(i + 1))
        # Descending letters
        descending = ''.join(chr(ord('A') + j) for j in range(i - 1, -1, -1))
        
        print(spaces + ascending + descending)
    print()

def diamond_with_numbers_pattern1(n):
    """
    Print diamond with numbers pattern
       1
      222
     33333
    4444444
     33333
      222
       1
    
    Args:
        n (int): Half size of diamond
    """
    print("Diamond with Numbers Pattern 1:")
    
    # Upper half (including middle)
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        numbers = str(i + 1) * (2 * i + 1)
        print(spaces + numbers)
    
    # Lower half
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)
        numbers = str(i + 1) * (2 * i + 1)
        print(spaces + numbers)
    print()

def diamond_with_numbers_pattern2(n):
    """
    Print diamond with numbers pattern
       1
      1 2
     1 2 3
    1 2 3 4
     1 2 3
      1 2
       1
    
    Args:
        n (int): Half size of diamond
    """
    print("Diamond with Numbers Pattern 2:")
    
    # Upper half (including middle)
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        numbers = ' '.join(str(j) for j in range(1, i + 2))
        print(spaces + numbers)
    
    # Lower half
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)
        numbers = ' '.join(str(j) for j in range(1, i + 2))
        print(spaces + numbers)
    print()

def butterfly_pattern(n):
    """
    Print butterfly pattern (two diamonds side by side)
    *      *
    **    **
    ***  ***
    ********
    ***  ***
    **    **
    *      *
    
    Args:
        n (int): Half size of butterfly
    """
    print("Butterfly Pattern:")
    
    # Upper half
    for i in range(1, n + 1):
        # Left stars
        left_stars = '*' * i
        # Middle spaces
        middle_spaces = ' ' * (2 * (n - i))
        # Right stars
        right_stars = '*' * i
        
        print(left_stars + middle_spaces + right_stars)
    
    # Lower half
    for i in range(n - 1, 0, -1):
        # Left stars
        left_stars = '*' * i
        # Middle spaces
        middle_spaces = ' ' * (2 * (n - i))
        # Right stars
        right_stars = '*' * i
        
        print(left_stars + middle_spaces + right_stars)
    print()

def hourglass_pattern(n):
    """
    Print hourglass pattern
    *******
     *****
      ***
       *
      ***
     *****
    *******
    
    Args:
        n (int): Half size of hourglass
    """
    print("Hourglass Pattern:")
    
    # Upper half (including middle)
    for i in range(n):
        spaces = ' ' * i
        stars = '*' * (2 * (n - i) - 1)
        print(spaces + stars)
    
    # Lower half
    for i in range(n - 2, -1, -1):
        spaces = ' ' * i
        stars = '*' * (2 * (n - i) - 1)
        print(spaces + stars)
    print()

def rhombus_pattern(n):
    """
    Print rhombus pattern
     ****
    ******
   ********
  **********
   ********
    ******
     ****
    
    Args:
        n (int): Half size of rhombus
    """
    print("Rhombus Pattern:")
    
    # Upper half (including middle)
    for i in range(n):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * n + 2 * i)
        print(spaces + stars)
    
    # Lower half
    for i in range(n - 2, -1, -1):
        spaces = ' ' * (n - i - 1)
        stars = '*' * (2 * n + 2 * i)
        print(spaces + stars)
    print()

def diamond_with_border(n):
    """
    Print diamond with border
    *********
    *   *   *
    *  ***  *
    * ***** *
    *  ***  *
    *   *   *
    *********
    
    Args:
        n (int): Half size of inner diamond
    """
    print("Diamond with Border:")
    
    total_width = 2 * n + 3
    
    # Top border
    print('*' * total_width)
    
    # Upper half of diamond
    for i in range(n):
        if i == 0:
            inner = ' ' * (2 * n - 1)
        else:
            spaces_before = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            spaces_after = ' ' * (n - i)
            inner = spaces_before + stars + spaces_after
        
        print('*' + inner + '*')
    
    # Lower half of diamond
    for i in range(n - 2, -1, -1):
        if i == 0:
            inner = ' ' * (2 * n - 1)
        else:
            spaces_before = ' ' * (n - i)
            stars = '*' * (2 * i - 1)
            spaces_after = ' ' * (n - i)
            inner = spaces_before + stars + spaces_after
        
        print('*' + inner + '*')
    
    # Bottom border
    print('*' * total_width)
    print()

def main():
    print("Diamond Pattern Demonstrations")
    print("=" * 40)
    
    n = 4  # Half size for demonstrations
    
    # Basic diamond patterns
    solid_diamond(n)
    hollow_diamond(n)
    number_diamond(n)
    alphabet_diamond(n)
    
    # Special diamond patterns
    diamond_with_numbers_pattern1(n)
    diamond_with_numbers_pattern2(n)
    butterfly_pattern(n)
    hourglass_pattern(n)
    rhombus_pattern(n)
    diamond_with_border(n)
    
    # Interactive section
    print("Interactive Diamond Pattern Generator")
    print("=" * 40)
    
    while True:
        print("\nAvailable patterns:")
        print("1. Solid Diamond")
        print("2. Hollow Diamond")
        print("3. Number Diamond")
        print("4. Alphabet Diamond")
        print("5. Diamond with Numbers Pattern 1")
        print("6. Diamond with Numbers Pattern 2")
        print("7. Butterfly Pattern")
        print("8. Hourglass Pattern")
        print("9. Rhombus Pattern")
        print("10. Diamond with Border")
        print("0. Quit")
        
        try:
            choice = int(input("\nEnter your choice (0-10): "))
            
            if choice == 0:
                print("Goodbye!")
                break
            
            if choice < 1 or choice > 10:
                print("Invalid choice! Please enter a number between 0 and 10.")
                continue
            
            size = int(input("Enter half-size of diamond: "))
            
            if size <= 0:
                print("Size must be positive!")
                continue
            
            if size > 15:
                print("Size too large! Please enter a number <= 15.")
                continue
            
            print(f"\nPattern with half-size {size}:")
            print("-" * 30)
            
            if choice == 1:
                solid_diamond(size)
            elif choice == 2:
                hollow_diamond(size)
            elif choice == 3:
                number_diamond(size)
            elif choice == 4:
                alphabet_diamond(size)
            elif choice == 5:
                diamond_with_numbers_pattern1(size)
            elif choice == 6:
                diamond_with_numbers_pattern2(size)
            elif choice == 7:
                butterfly_pattern(size)
            elif choice == 8:
                hourglass_pattern(size)
            elif choice == 9:
                rhombus_pattern(size)
            elif choice == 10:
                diamond_with_border(size)
            
        except ValueError:
            print("Please enter a valid number!")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()