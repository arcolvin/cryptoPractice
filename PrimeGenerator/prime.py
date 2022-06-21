#!/usr/bin/env python3

import logging

pr = True   # Set to True to have results printed to screen in real time (Slow)
lg = False  # Set to True to have results logged to file (Faster)

if lg: logging.basicConfig(filename='prime.log',
                            level='DEBUG',
                            format='%(message)s',
                            filemode='w')


'''
This Program will calculate wether a number is prime and print only prime
numbers. The program will then attempt to find the next prime number counting
upwards from 1. This will show that calculating very large primes as used in
cryptography would take a very long time.

In reality we dont fully factor every prime we use, instead using an algorithm
to predict probable primes.

Also Sieve algorithm would likely be much faster than the brute force we are
doing here, but even with Sieve it would still take a very long time to
test all possible factors of a 1024 bit RSA prime.

Python printing and logging can be very resource intensive as well. By
eliminating one or both of these functions we can dramatically improve our
script's performance, but we then lose the ability to see what the program is
doing!

Sieve of Eratosthenes:
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
'''

# Start and end point if limited run is needed
i = 0
fin = 100000

# Swap next two lines depending on of you want the
# program to run forever or for a limited time

# while i < fin: # end at fin point
while True: # Endless
    i += 1 # For while loop use only
    n = 1
    root_i = i ** 0.5 # optimized 2

    if i == 2:
        if lg: logging.debug(f'Prime Found!: {i}')
        if pr: print(f'Prime Found!: {i}')
        continue
        
    if i % 2 == 0:
        # logging.debug(f'Not a Prime: {i}) # Un-comment to log non-primes
        # print(f'Not a prime: {i}')        # Un-comment to print non-primes
        continue

    elif root_i == int(root_i):
        continue

    while n < i:
        
        if i % n == 0 and n != 1:

            # print(f"Not a prime: {i}") # Un-comment to print non-primes
            break
        elif n >= root_i:
            if lg: logging.debug(f'Prime Found!: {i}')
            if pr: print(f'Prime Found!: {i}')
            break
        
        n += 1 
