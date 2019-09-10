"""
5.2 Write a program that repeatedly prompts a user for integer numbers until 
the user enters 'done'. Once 'done' is entered, print out the largest and 
smallest of the numbers. If the user enters anything other than a valid number 
catch it with a try/except and put out an appropriate message and ignore the 
number. Enter 7, 2, bob, 10, and 4 and match the output below. 

"""


largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" :
        print("Maximum is", largest)
        print("Minimum is", smallest)
        break
    try:
        inum = int(num)
    except:
        print("Invalid input")15: Object-Oriented Programming
    if largest is None:
        largest = inum
        smallest = inum
    elif largest < inum:
        largest = inum
    elif smallest > inum:
        smallest = inum
