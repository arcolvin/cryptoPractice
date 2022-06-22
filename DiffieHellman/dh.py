#!/usr/bin/env python3

'''
This application will generate a private key using Diffie-Hellman methods.
It will show each of the calculated values along the way.
The intent of this application is to show the math being done by DH but is not
useful for proper encryption since all of the information is generated on a
single node.

Note that while this will work for small as well as large numbers, small numbers
have a much higher chance of colliding or having odd results as the possible
domain of values is very small. This would normally be done with extremely large
numbers in the 1024+ bit length range.

This script starts to struggle from a performance standpoint when we get into
modulus in the range of tens of thousands, but will eventually solve if the
user is patient enough.

gcd() and primeRoots() pulled from:
https://stackoverflow.com/questions/40190849/efficient-finding-primitive-roots-modulo-n-using-python
'''

import random

# See above link for source
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# This is inefficient but simple as to not make this script excessively long
# See link above for source
def primRoots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]

# Can be any number, better if prime
# This is person 1's secret
a = 17

# Can be any number, better if prime
# This is person 2's secret
b = 11

# Modulus, should be prime
mod = 23

# Leave as None if a generated value is desired
# Replace if predetermined g is available or preferred
# G must be a primitive root of the modulus
g = None

if g == None:
    # List of possible G values
    # Needs to be a primitive root of the modulus
    print('Please Wait. Generating a value for g based on provided mod\n')
    gLst = primRoots(mod)

    # Some numbers have no primitive roots
    # This will verify before any numbers are generated
    if len(gLst) == 0:
        print('Bad Modulus. Can\'t Generate G!')
        exit()

    g = random.choice(gLst)

# Calculate all values
ag = pow(g,a,mod)
bg = pow(g,b,mod)
abg = pow(bg, a, mod)
bag = pow(ag, b, mod)

# Report all values to the user

print(f'User 1 Secret (a): {a}')
print(f'User 2 Secret (b): {b}\n')
print(f'Public Initial Value (g): {g}\n')


print(f'User 1 Mixed Secret (Sent to User 2 in clear) (ag): {ag}')
print(f'User 2 Mixed Secret (Sent to user 1 in clear) (bg): {bg}\n')


print(f'Final symmetric key calculated by User 1 (abg): {abg}')
print(f'Final symmetric key calculated by User 2 (bag): {bag}\n')

if abg == bag:
    print('(abg) is equal to (bag). Key Generation Successful!\n')

else:
    print('(abg) does not equal (bag). Key Generation Failed!\n')