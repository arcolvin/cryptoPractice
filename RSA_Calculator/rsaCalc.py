#!/usr/bin/python3

p =  11  # Must Be Prime, should be close ish to q
q =  17 # Must Be Prime, should be close ish to p 

n = p * q # Modulus

Φ = (p-1) * (q-1) # (Phi) Used to calculate d

e = 23 # Must be Smaller than Φ, must be odd, Better if prime. Typically 65537.

if e > Φ:
    print("e is too big! Must be smaller than Φ")
    print(f"e: {e}")
    print(f"Φ: {Φ}")
    exit()

d = None

# This will find our d which is a Modular Inverse
d = pow(e, -1, Φ)

# Verify D is smaller than Φ
if d > Φ:
    print("d is too big! Must be smaller than Φ")
    print(f"d: {d}")
    print(f"Φ: {Φ}")
    exit()

# Initialize x and y for GCD Calculation
x = e
y = d

# Verify GCD of d and e is 1 (If e is prime this should be true)
while(y):
   x, y = y, x % y

x = abs(x)

# Warn User if numbers are not relatively Prime
if x != 1:
    print("e and d are not relatively prime!")
    exit()

# Return all calculated Values
print("Calculated Values: ")
print(f'p: {p}\nq: {q}\nn: {n}\nΦ: {Φ}\ne: {e}\nd: {d}')
