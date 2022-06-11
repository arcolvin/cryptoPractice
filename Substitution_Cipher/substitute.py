#!/usr/bin/env python3
'''
This program will encrypt a user provided text file against a random key.
This is intended to offer practice to the user for frequency analyses decryption
of a substitution cypher
'''

import random

# Define the alphabet to be used by the rest of the script
# Add additional characters or spaces if desired, though this
# will change the normal frequency of each character!
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = ''
keygen = list(alph)
mapper = {}

# Generate a random key for the encryption based on the alphabet defined above
for l in range(len(alph)):
    key += random.choice(keygen)
    keygen.remove(key[-1])

# Create mapper dictionary for the encryption
i = 0
for x in key:
    mapper[x] = alph[i]
    i +=1

# Swap these lines if a dynamic PT is desired
# pt = 'pt.txt'
pt = input("What is the name of the plaintext file?: ")

# Save Plaintext as a string
with open(pt) as f:
    ptstring = f.read()

# Create cypher text using plaintext string and mapper dictionary
ct = ''
for let in ptstring.upper():
    if let in alph:
        ct += mapper[let]

# add spaces to final out string so it is in groups of 5 letters
i = 0
fin = ''
for let in ct:
    if i % 5 == 0:
       fin += ' ' + let 

    else:
        fin += let
    
    i += 1
    
# Save out string to a file for review
with open('out.txt', 'w') as f:
    f.write(fin)
