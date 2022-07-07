#!/usr/bin/env python3

####################
# Start Generate S #
####################

# Key Scheduling Algorithm for ARCFour

# Set Key for encoding (Decimal number between 5 and 256 digits)
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

##################
# END GENERATE S #
##################

# Pseudo-Random Generation Algorithm

i = 0
j = 0

while True:
    i = (i + 1) % 256
    j = (j + S[i]) % 256

    tmp = S[i]
    S[i] = S[j]
    S[j] = tmp

    print(S[(S[i] + S[j]) % 256])