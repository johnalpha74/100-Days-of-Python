'''
Write a program that works out whether if a given number is an odd or even number.
'''

number = input("Enter a number to test if Odd or if Even")

print("Even") if int(number) % 2 == 0 else print("Odd")
