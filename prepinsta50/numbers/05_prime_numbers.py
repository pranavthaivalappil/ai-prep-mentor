"""
PrepInsta Problem 5: Prime number operations
"""

import math

def is_prime(n):
    """
    Check if a number is prime
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_numbers_in_range(start, end):
    """
    Find all prime numbers in a given range
    
    Args:
        start (int): Start of range (inclusive)
        end (int): End of range (inclusive)
    
    Returns:
        list: List of prime numbers in range
    """
    primes = []
    for num in range(max(2, start), end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def sieve_of_eratosthenes(limit):
    """
    Find all prime numbers up to limit using Sieve of Eratosthenes
    
    Args:
        limit (int): Upper limit
    
    Returns:
        list: List of prime numbers up to limit
    """
    if limit < 2:
        return []
    
    # Create boolean array and initialize all as True
    is_prime_arr = [True] * (limit + 1)
    is_prime_arr[0] = is_prime_arr[1] = False
    
    p = 2
    while p * p <= limit:
        if is_prime_arr[p]:
            # Mark all multiples of p as not prime
            for i in range(p * p, limit + 1, p):
                is_prime_arr[i] = False
        p += 1
    
    # Collect all prime numbers
    return [i for i in range(2, limit + 1) if is_prime_arr[i]]

def nth_prime(n):
    """
    Find the nth prime number
    
    Args:
        n (int): Position of prime to find
    
    Returns:
        int: The nth prime number
    """
    if n <= 0:
        return None
    
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

def main():
    # Test prime checking
    print("Prime number checking:")
    print("-" * 25)
    test_numbers = [2, 3, 4, 17, 25, 29, 97, 100]
    
    for num in test_numbers:
        result = is_prime(num)
        print(f"{num} is {'prime' if result else 'not prime'}")
    
    # Test prime numbers in range
    print("\nPrime numbers in range 10-30:")
    print("-" * 30)
    primes_range = prime_numbers_in_range(10, 30)
    print(f"Primes: {primes_range}")
    
    # Test sieve of eratosthenes
    print("\nPrime numbers up to 50 (using sieve):")
    print("-" * 40)
    primes_sieve = sieve_of_eratosthenes(50)
    print(f"Primes: {primes_sieve}")
    print(f"Count: {len(primes_sieve)}")
    
    # Test nth prime
    print("\nFirst 10 prime numbers:")
    print("-" * 25)
    for i in range(1, 11):
        prime = nth_prime(i)
        print(f"{i}th prime: {prime}")
    
    # Interactive input
    print("\nEnter a number to check if prime (or 'quit' to exit):")
    while True:
        user_input = input("Number: ")
        if user_input.lower() == 'quit':
            break
        try:
            num = int(user_input)
            if num < 0:
                print("Please enter a non-negative number!")
                continue
            result = is_prime(num)
            print(f"{num} is {'prime' if result else 'not prime'}")
        except ValueError:
            print("Please enter a valid integer!")

if __name__ == "__main__":
    main()