import math
import sys
import os

rep = "Would you like to go back? (y/n)\n"
print("Welcome to calc v2 \n Select Function:")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exponents\n6. Square root\n7. Cube root\n8. Factorial")
type = input("Enter Func Number: ")

if type == "1":
    print("Addition selected")
    add1 = input("Enter first number\n")
    add2 = input("Enter second number\n")
    print(float(add1) + float(add2))
    

if type == "2":
    print("Subtraction selected")
    sub1 = input("Enter first number\n")
    sub2 = input("Enter second number\n")
    print(float(sub1) - float(sub2))
    

if type == "3":
    print("Multiplication selected")
    mult1 = input("Enter first number\n")
    mult2 = input("Enter second number\n")
    print(float(mult1) * float(mult2))
    

if type == "4":
    print("Division selected")
    div1 = input("Enter first number\n")
    div2 = input("Enter second number\n")
    print(float(div1) / float(div2))
    

if type == "5":
    print("Exponent slelected")
    exp1 = input("Enter base number\n")
    exp2 = input("Enter exponent\n")
    print(float(exp1) ** float(exp2))
    

if type == "6":
    print("Square root selected")
    sqr = input("Enter number\n")
    print(math.sqrt(float(sqr)))
    

if type == "7":
    print("Cube root selected")
    cbr = input("Enter number\n")
    print(math.cbrt(float(cbr)))
    
    
if type == "8":
    print("Factorial selected")
    fac = input("Enter number\n")
    print(math.factorial(int(fac)))
    
    
rep_ans = input(rep)

# A repeat, but I can't figure out how to actually repeat the whole file- (so good luck with that)
if rep_ans == "y":
    NotImplemented #Will be updated eventually (CALC_V2.3)