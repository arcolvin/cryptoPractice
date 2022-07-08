#!/usr/bin/env python3

# Key Scheduling Algorithm for ARCFour

# Set Key for encoding (Decimal number between 5 and 256 digits)
key = [3,255,0,20,30,40,50,60]

counter = {}
# Init Output List
S = []
# Measure Key Length
keylength = len(key)

for g in range(0,256):
    key.insert(2,g)
    # Init Key Array
    for i in range(0,256):
        S.insert(i, i)


    # Build Key Array
    j = 0
    for i in range(0,4): # Normally range to 256 but we only want to do the first 4 rounds
        j = (j + S[i] + key[i % keylength]) % 256
        # swap values of S[i] and S[j]
        tmp = S[i]
        S[i] = S[j]
        S[j] = tmp
        
        try:
            counter[tuple(S[:2] + [S[3]])] += 1

        except KeyError:
            counter[tuple(S[:2] + [S[3]])] = 1



for x in counter:
    print(x, counter[x])
