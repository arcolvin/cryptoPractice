#!/usr/bin/env python3
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
    n = 1
    i += 1

    while n < i:
        if i % 2 == 0:
            # print(f"Not a prime: {i}")
            break
        
        elif i % n == 0 and n != 1:
            # print(f"Not a prime: {i}")
            break
        
        n += 1

    if n == i: # Original
        print(f'Prime Found!: {i}')