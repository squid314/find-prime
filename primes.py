#!/usr/bin/env python

"""simple utility to find the closest prime number to a provided number"""

def isprime(number):
    "tests if a number is prime"

    if number < 2: return False
    if number == 2: return True
    if number % 2 == 0: return False

    return __isprime(number)

def __isprime(number):
    "internal test for primality; assumes input is an odd number greater than 1 to improve speed"

    for test in range(3, __lasttest(number), 2):
        if number % test == 0:
            return False
    return True

from math import sqrt
def __lasttest(number):
    """internal square root calculator to determine the last number which should be tested
    and provide a value greater than that for passing to range()"""

    return int(sqrt(number)) + 1

POSITIVE=1
NEGATIVE=-1
import itertools
def closestprimes(number, count=1, direction=POSITIVE):
    "determine up to count closest primes to the provided number, which may include the number itself"

    if count < 1: raise ArgumentError("count must be positive")
    if direction != POSITIVE and direction != NEGATIVE: raise ArgumentError("direction must be POSITIVE or NEGATIVE")
    if number < 2:
        if dir == NEGATIVE:
            raise ArgumentError("no primes less than 2")
        number = 2

    if number == 2:
        yield 2
        # there are no numbers less than 2 which are prime; also if they only asked for 1 number, we are done
        if direction == NEGATIVE or count == 1: raise StopIteration()
        # now that we've taken care of the edge case, we continue from 3
        number = 3
        count -= 1
    elif number % 2 == 0:
        # if the number is even, just add 1 in the proper direction and it will be odd, then iteration can proceed normally
        number += direction

    for primetest in itertools.count(number, 2*direction):
        if primetest < 1: raise StopIteration()
        if __isprime(primetest):
            yield primetest
            count -= 1
        if count == 0: raise StopIteration()

if __name__ == "__main__":
    from sys import argv

    number = int(argv[1])
    count = 1
    if len(argv) > 2: count = int(argv[2])
    direction = POSITIVE
    if len(argv) > 3:
        direction = argv[3].upper()
        if direction == "POSITIVE":
            direction = POSITIVE
        elif direction == "NEGATIVE":
            direction = NEGATIVE
        else:
            print 'direction must be "positive" or "negative"'
            exit(1)

    for prime in closestprimes(number, count, direction):
        print prime
