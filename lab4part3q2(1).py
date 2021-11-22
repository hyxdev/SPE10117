import math


A = int(input("enter a postive integer:"))	
B = int(input("enter a postive integer:"))	
C = int(input("enter a postive integer:"))	

print(A)
print(B)
print(C)

Largest = A

if B > Largest:
    Largest = B

if C >Largest:
    Largest = C

print("Largest number is:", Largest)    