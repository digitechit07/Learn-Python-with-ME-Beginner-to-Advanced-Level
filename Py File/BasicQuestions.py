'''
#1). Check Python Version
import platform
print(platform.python_version)
print(platform.python_version_tuple)

#2). Python program to display the current date and time.
import datetime
print(datetime.datetime.now())

#3). Python program that calculates the area of a circle
from math import pi
x = int(input("Enter the radius: "))
print(pi*x**2)

#4). Python program that accepts the user's first and last name and prints them in reverse order with a space between them.
x = input("Enter you first and last name: ")
y = x[::-1]
print(y)

#5). Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
x = input("Enter a comma separated sequence: ")
y = x.split(",")
z = tuple(y)
print(y)
print(z)

#6). Python program that accepts a filename from the user and prints the extension of the file.
x = input("Enter the filename: ")
y = x.split(".")
print("The extension of file is:", repr(y[-1]))

#7). Python program to display the first and last colors from the following list.
x = input("Enter a comma separated sequence: ")
y = x.split(",")
print("First element:",y[0])
print("Last element:",y[-1])

#8). Python program to display the examination schedule.
x = (24,11,2024)
print("The exam will start from: %i/%i/%i"%x)

#9). Python program that accepts an integer (n) and computes the value of n+nn+nnn.
x = input("Enter the number: ")
a = int(x)
b = int(x+x)
c = int(x+x+x)
print(a+b+c)

#10). Python program that prints the calendar for a given month and year.
import calendar
x = int(input("Enter year: "))
y = int(input("Enter month: "))
print(calendar.month(x,y))

#11). Python program to calculate the number of days between two dates.
from datetime import date
x = date(2024,7,12)
y = date(2024,8,24)
da = y - x
print(da.days)

#12). Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
x = int(input("Enter the number: "))
if x > 17:
    print(2*(x-17))
else:
    print(17-x)

#13). Create a list with values ranging from 0 to 9.
print(list(range(9)))
'''