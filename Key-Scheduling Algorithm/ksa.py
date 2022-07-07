#!/usr/bin/env python3

# Key Scheduling Algorithm for ARCFour

#Set Key for encoding (Decimal number between 5 and 256 digits)
key = '8675309'

# Init Output List
S = []
# Measure Key Length
keylength = len(str(key))

# Init Key Array
for i in range(0,256):
    S.insert(i, i)


# Build Key Array
j = 0
for i in range(0,256):
    j = (j + S[i] + int(key[i % keylength])) % 256
    # swap values of S[i] and S[j]
    tmp = S[i]
    S[i] = S[j]
    S[j] = tmp

# Convert Decimal Key to Binary
binKey = ''
for x in S:
    binKey += bin(x)[2:].zfill(8)

# Print Results
print(f"Count of key elements: {len(S)}")
print(f"Raw Decimal Key List: {S}")
print(f"Binary Key of 256 Bytes: {binKey}")
