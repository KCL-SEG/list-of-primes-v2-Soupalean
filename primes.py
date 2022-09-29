"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


import math as m

def primes(number_of_primes):
    list = [2, 3]
    counter = 4

    if number_of_primes < 1:
        raise ValueError
    elif number_of_primes == 1:
        return [2]
    elif number_of_primes == 2:
        return [2, 3]
    while len(list) < number_of_primes:
        isPrime = True
        for i in range(2, int(m.sqrt(counter) + 1)):
            if counter % i == 0:
                isPrime = False
                break
        if isPrime:
            list.append(counter)
        counter += 1
    return list
