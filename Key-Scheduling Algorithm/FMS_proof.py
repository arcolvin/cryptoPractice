#!/usr/bin/env python3

# Key Scheduling Algorithm for ARCFour

# Set Key for encoding ( Use decimal number between 0 and 255)
# This key should match the key from SBoxFinder.py
# Replace 'x' with one of the known good X values found by the SBoxFinder script
key = [3,255,'x',10,20,30,40,50]

# Example key from default values in SBoxFinder.py
# key = [3,255,151,10,20,30,40,50]

# Init Output List
S = []
# Measure Key Length
keylength = len(key)

# Init Key Array
for i in range(0,256):
    S.insert(i, i)


# Build Key Array
j = 0
for i in range(0,256):
    j = (j + S[i] + key[i % keylength]) % 256
    # swap values of S[i] and S[j]
    tmp = S[i]
    S[i] = S[j]
    S[j] = tmp
    
    # Print out each iteration of the S array build process
    # We are only printing the first 20 entries to simplify the output for the
    # viewer
    # If desired print all S values, but this will be harder to parse visually
    print(f'Iteration {i}: \t{S[:20]}')
    
    # Pause at the 3rd iteration to identify what our fixed values should
    # be for the remainder of the iterations
    if i == 3:
        print(f"First 4 bytes should be: {S[:2] + ['?'] + [S[3]]}")
        input("Press ENTER to continue...")

    # Once the application finishes scroll through the outputted values to
    # verify only the bytes other than those in the 0, 1, and 3 indexes have changed
