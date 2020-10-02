# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

a = int(input("enter cofficient of x square"))
b = int(input("enter cofficient of x"))
c = int(input("enter constant "))
p = str(input("do you want roots or not (for yes y , for NO n )"))
#disciminant1


D = b**2 - 4*a*c
x = D**(1/2.0)

R1 = (-b + x) /  2*a
R2 = (-b - x) / 2*a
if p == "y" :
     print("your roots are")
     print(R1) 
     print(R2) 
else:
    print("")     
1
if D > 0 :
    print("roots are real and distinct ")
elif D == 0 :
    print("roots are real and equal ")
else:
    print("roots are imaginary or in complex conjugate pair")
    
print("thank you ")