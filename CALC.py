import sys

print("This ''calculator'' only works with addition (so put 1 number in, hit enter and put in another number)")

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

if float(num1) == 9 and float(num2) == 10:
    print("Whats nine plus ten?")
    sys.exit()

print(result)
print("Here you go!")
input()