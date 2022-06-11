#!/usr/bin/python3
# Prime Template
import time

primes = [] # List of newly identified prime numbers
master = [] # List to contain known prime numbers

# start the timer
start = time.time_ns() # Gives sub second accuracy

#################################
## Do Not Edit Above This Line ##
#################################

'''
Recommend put code into for loop to ensure only primes inside
of first 100,000 numbers. This can be removed or modified if
a different method is used to limit to first 100,000 numbers
'''
for i in range(1,100000):
    
    n = 1
    root_i = i ** 0.5 # optimized 2

    if i == 2:
        print(f'Prime Found!: {i}')
        primes.append(i)
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
            print(f'Prime Found!: {i}')
            primes.append(i)
            break         # Optimized 2
        
        n += 1 


    # if a prime number is found save to the master list
    # primes.append(str(i))

#################################
## Do Not Edit Below This Line ##
#################################

# stop the timer
end = time.time_ns()

# Show the time required to calculate primes
print(f'{(end - start) / 1e9} seconds elapsed')

# Write found primes to a file for post runtime review
with open('primeList.txt', 'w') as f:
    for x in primes:
        f.write(str(x) + "\n")

# convert prime list to set for final comparison
primes = set(primes)

# Load Master Prime list for comparison to current prime run
# By Default primeMaster.txt holds 9592 values which is all
# known primes between 1 and 100,000
with open('primeMaster.txt', 'r') as f:
    master = set([int(l.rstrip('\n')) for l in f])
    
# Verify all primes in the master list also appear in the newly generated list
if primes == master:
    print('Newly generated numbers and master list match!')

# If sets are not the same print any discrepancies
else:
    newVsMstr = sorted(list(primes - master))
    mstrVsNew = sorted(list(master - primes))

    for x in newVsMstr:
        print(f'{x} found in newly generated file, ' \
            + 'but not found in master file!')

    for x in mstrVsNew:
        print(f'{x} found in master file, but not found in ' \
            + 'newly generated file!') 
