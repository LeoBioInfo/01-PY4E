45
# -*- coding: utf-8 -*-

"""
Variables, expressions, and statements
"""
"""
2.3 Write a program to prompt the user for hours and rate per hour using input 
to compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the 
program (the pay should be 96.25). You should use input to read a string and 
float() to convert the string to a number. Do not worry about error checking 
or bad user data.
"""
"""
hrs = input("Enter Hours:")
rate = input("Enter rate:")
pay = float(hrs) * float(rate)
print ("Pay:", pay)
"""
"""
3.1 Conditional Execution
"""
"""
< less than
<= less than or equal to
== equal to
>= greater than or equal to
> greater thanrate = input("Enter rate:")
!= not equal 
"""
"""
3.1 Write a program to prompt the user for hours and rate per hour using input 
to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times 
the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of
 10.50 per hour to test the program (the pay should be 498.75). You should use 
 input to read a string and float() to convert the string to a number. Do not 
 worry about error checking the user input - assume the user types numbers 
 properly. 
"""
"""

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)
extra = 0
if h <= 40 :
    pay = h * r
    print (pay)
else:
    pay = (h - 40)*(r * 1.5) + (40 * r)
    print (pay)
"""
"""
3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is
 out of range, print an error. If the score is between 0.0 and 1.0, print a 
 grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and 
exit. For the test, enter a score of 0.85.
"""
"""
s = input("Enter score:")
fs = float(s)
print(fs)
try:
    #float(s)  0.0 or float(s) > 1.0
    fs < 1.0 
except:
    print("suitable error message")
"""
"""
score = input("Enter Score: ")
s = float(score)
if s < 0.0 or s > 1.0:
    print("suitable error message")
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.6:
    print("F")
"""
"""   
    Functions
4.6 Write a program to prompt the user for hours and rate per hour using input 
to compute gross pay. Pay should be the normal rate for hours up to 40 and 
time-and-a-half for the hourly rate for all hours worked above 40 hours. 
Put the logic to do the computation of pay in a function called computepay() 
and use the function to do the computation. The function should return a value. 
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should 
be 498.75). You should use input to read a string and float() to convert the 
string to a number. Do not worry about error checking the user input unless
 you want to - you can assume the user types numbers properly. Do not name 
 your variable sum or use the sum() function.    
"""
"""    
def computepay(h,r):
    if h <= 40:
        gp = h * r
        return gp
    else:
        gp = (h - 40)*(r * 1.5) + (40 * r)
        return gp
    
hrs = float(input("Enter Hours:"))
rate = float(input("enter rate:"))
p = computepay(hrs,rate)
print(p)
"""
"""
5.1 - Loops and Iteration

5.2 Write a program that repeatedly prompts a user for integer numbers until 
the user enters 'done'. Once 'done' is entered, print out the largest and 
smallest of the numbers. If the user enters anything other than a valid number 
catch it with a try/except and put out an appropriate message and ignore the 
number. Enter 7, 2, bob, 10, and 4 and match the output below. 

"""

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
        print("Invalid input")
    if largest is None:
        largest = inum
        smallest = inum
    elif largest < inum:
        largest = inum
    elif smallest > inum:
        smallest = inum
"""
"""
Strings
"""
"""
text = "X-DSPAM-Confidence:    0.8475";

print(text[text.find(' '):-1].strip())
"""
"""

7.2 Write a program that prompts for a file name, then opens that file and 
reads through the file, looking for lines of the form:

X-DSPAM-Confidence:    0.8475

Count these lines and extract the floating point values from each of the lines
 and compute the average of those values and produce an output as shown below.
 Do not use the sum() function or a variable named sum in your solution.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
when you are testing below enter mbox-short.txt as the file name
"""
"""
# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    else:
        count = count + 1
        total = total + float(line[line.find(' '):-1].strip())

print("Average spam confidence:", total/count)
""" 

"""
8 List


8.4 Open the file romeo.txt and read it line by line. For each line, split the
 line into a list of words using the split() method. The program should build 
 a list of words. For each word on each line check to see if the word is
 already in the list and if not append it to the list. When the program
 completes, sort and print the resulting words in alphabetical order.

You can download the sample data at http://www.py4e.com/code3/romeo.txt

['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 
'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 
'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']
"""
"""
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line_list= line.split()
    for word in line_list:
        if word not in lst:
            lst.append(word)
lst.sort()
print (lst) 
"""

"""
8.5 Open the file mbox-short.txt and read it line by line. When you find a 
line that starts with 'From ' like the following line:

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

You will parse the From line using split() and print out the second word in 
the line (i.e. the entire address of the person who sent the message). Then 
print out a count at the end.

Hint: make sure not to include the lines that start with 'From:'.

You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

stephen.marquard@uct.ac.za
louis@media.berkeley.edu
zqian@umich.edu
rjlowe@iupui.edu
zqian@umich.edu
rjlowe@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
gsilver@umich.edu
gsilver@umich.edu
zqian@umich.edu
gsilver@umich.edu
wagnermr@iupui.edu
zqian@umich.edu
antranig@caret.cam.ac.uk
gopal.ramasammycook@gmail.com
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
david.horwitz@uct.ac.za
stephen.marquard@uct.ac.za
louis@media.berkeley.edufname = "mbox-short.txt"
louis@media.berkeley.edu
ray@media.berkeley.edu
cwen@iupui.edu
cwen@iupui.edu
cwen@iupui.edu
There were 27 lines in the file with From as the first word
"""


fname = input("Enter file name: ")
if len(fname) < 1 :
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
for line in fh:
    if line.startswith('From '):
        spline = line.split()
        count = count + 1
        print(spline[1])
print("There were", count, "lines in the file with From as the first word")



