from math import isqrt


def is_prime(num):
    if num < 2:
        return False
    for prime in range(2, isqrt(num) + 1):
        if num % prime == 0:
            return False
    return True


def get_primes(numbers):
    for num in numbers:
        if is_prime(num):
            yield num


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))