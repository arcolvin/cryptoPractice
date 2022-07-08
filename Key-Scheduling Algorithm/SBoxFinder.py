#!/usr/bin/env python3

# Key Scheduling Algorithm for ARCFour

# Set Key for encoding ( Use decimal number between 0 and 255)
# This key should have 3,255,'x' for its first three bytes
# Remaining bytes do not particularly matter, but will change the
# Final results of the S array
# 10, 20, 30, 40, 50 are provided as default values, These can be replaced with
# any number between 0 and 255, Only the first three IV values should remain
# undisturbed (3, 255, 'x')
key = [3,255,'x',10,20,30,40,50]

counter = {}
# Init Output List
S = []
# Measure Key Length
keylength = len(key)

# Initialize some counters to be used in the following loop
# These will track which x values result in an sbox where the 3 critical values
# do not change
counter["Good S[]"] = []

# Index position 0 is a counter the rest of the list will be found good S box values
counter["Good S[]"].append(0)

# Bad values are simply tallied, we dont care what the values are specifically,
# just how many bad values there were over all
counter["Invalid S[]"] = 0

# Set up loop to test all 256 possible x values
for g in range(0,256):
    key[2] = g
    
    # Normal KSA takes place in this loop
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
        
        # Add Checkpoint at loop 3 to save what our final array should start with        
        if i == 3:
            target = tuple(S[:2] + [S[3]]) 

        # Check final array against target array to see if this is good or bad output
        if i == 255:
            # If good incriment counter and add good array header to dictionary for tracking
            if target == tuple(S[:2] + [S[3]]):
                counter["Good S[]"][0] += 1
                counter["Good S[]"].append(tuple(S[:4]))

            # if not good simply count the attempt and move on
            else:
                counter["Invalid S[]"] +=1

# Prep values to calculate % of good vs bad attempts
goodSBox = counter["Good S[]"][0]
badSBox = counter["Invalid S[]"]

# Print % occurrence of possible x values (Should be around 5%)
print(f'Percentage of good S array found: {(goodSBox/badSBox)*100:.2f} %')
                    

# Show good array headers and probable related x values
print(f'Good S array values:\n')
print('x\t| S Array will start with')
print('---------------------------------')
for x in range(1, len(counter["Good S[]"])):
    calcX = counter["Good S[]"][x][3] - 6 - key[3]
    if calcX < 0:
        calcX = 256 + calcX
    print(f'{calcX}\t|', counter["Good S[]"][x])
