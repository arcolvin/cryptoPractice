#!/usr/bin/env python3

import logging

logging.basicConfig(filename='prime.log', level='DEBUG', format='%(message)s', filemode='w')

'''
This Program will calculate wether a number is prime and print only prime numbers.
The program will then attempt to find the next prime number counting upwards from 1.
This will show that calculating very large primes as used in cryptography would take a very
long time.
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
        logging.debug(f'Prime Found!: {i}')
        # print(f'Prime Found!: {i}')
        continue
        
    if i % 2 == 0:
        # print(f"Not a prime: {i}")
        continue

    elif root_i == int(root_i):
        continue

    while n < i:
        
        if i % n == 0 and n != 1:
            # print(f"Not a prime: {i}")
            break
        elif n >= root_i: # Optimized 2
            logging.debug(f'Prime Found!: {i}')
            # print(f'Prime Found!: {i}')
            break         # Optimized 2
        
        n += 1 
