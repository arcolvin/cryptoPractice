#!/usr/bin/env python3
'''
This program will encrypt a user provided text file against a random key.
This is intended to offer practice to the user for frequency analyses decryption
of a substitution cypher
'''

import random

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key = ''
keygen = list(alph)
mapper = {}

for l in range(len(alph)):
    key += random.choice(keygen)
    keygen.remove(key[-1])

i = 0
for x in key:
    mapper[x] = alph[i]
    i +=1

# Swap these lines if a dynamic PT is desired
pt = 'pt.txt'
# pt = input("What is the name of the plaintext file?: ")
with open(pt) as f:
    ptstring = f.read()

ct = ''
for let in ptstring.upper():
    if let in alph:
        ct += mapper[let]

i = 0
fin = ''
for let in ct:
    if i % 5 == 0:
       fin += ' ' + let 

    else:
        fin += let
    
    i += 1
    

with open('out.txt', 'w') as f:
    f.write(fin)