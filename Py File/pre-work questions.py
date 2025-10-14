# Question 1: Write a function to print "hello_username!" username is the input of the function.
#The first line of the code has been defined as below.

def hello_name(user_name):
        print(f"Hello {user_name}, it's nice to meet you!")
        return user_name
print("Hello, may i get your username? ")
hello_name(user_name=input())

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
        first_odds = list(range(1, 101, 2))
        print(first_odds)
        return first_odds

first_odds()

#Question 3:
#Please write a Python Function, max_num_in_list to return
#number of a given list.

def max_num_in_list(a_list):
        foods = a_list
        foods = ["chicken", "cheese", "pizza", "pasta"]

        for index in (range(len(foods))):
                print(index)
        print(foods)
        return  foods

max_num_in_list(a_list= (range))

#Question 4:
#write a function to return if the given year is a leap year. A leap year is divisible
#by 100,unless it is also divisible by 400.
#The return should be boolean Type (true/false).

def is_leap_year(a_year):
        a_year = 2020

        if (a_year % 400 == 0) and (a_year % 100 == 0):
                print("This is a leap year" )

        elif (a_year % 4 ==0) and (a_year % 100 != 0):
                print("This is a leap year" )

        else:
                print("This is not a leap year" )

        return a_year

is_leap_year(a_year= [2020])

#Question 5: Write a function to check to see if all numbers in list are consecutive numbers.
#For example,[2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#The return should be boolean Type.

def is_consecutive(a_list):
        foods = a_list
        foods = ["popcorn", "top ramen", "sushi", "fufu"]

        for index in (range(len(foods))):
                print(index)
        print(foods)

        if bool(foods) is is_consecutive:
                print(True)
        
        else :
                print(False)

        return  foods

is_consecutive(a_list= bool())