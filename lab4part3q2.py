import random

A = random.randrange(1, 10)
B = random.randrange(1, 10)
C = random.randrange(1, 10)

print(A)
print(B)
print(C)

Largest = A

if B > Largest:
    Largest = B

if C >Largest:
    Largest = C

print("Largest number is:", Largest)