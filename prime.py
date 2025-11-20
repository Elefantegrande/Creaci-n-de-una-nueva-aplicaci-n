"""Prints all prime numbers less than 100."""

import math


def is_prime(n):
    """Return True if n is a prime number, otherwise False."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True


def main():
    """Print all prime numbers less than 100."""
    for i in range(100):
        if is_prime(i):
            print(i, end=' ')
    print()


if __name__ == '__main__':
    main()
