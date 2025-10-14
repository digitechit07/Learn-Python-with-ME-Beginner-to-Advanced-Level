#!/usr/bin/env python
# coding: utf-8

# # 1. User will input (3ages). Find the oldest one.

# In[7]:


age_1=int(input('Enter age_1: '))
age_2=int(input('Enter age_2: '))
age_3=int(input('Enter age_3: '))

if age_1>age_2 and age_1>age_3: 
    print('age_1 is the oldest')

        
elif age_2>age_1 and age_2>age_3:
    print('age_2 is the oldest')
 
else:
    print('age_3 is the oldest')   


# # 2. Write a program that will convert celsius value to fahrenheit.

# In[ ]:


###  F=(C*9/5)+32


# In[20]:


celsius=float(input("Enter celsius : "))

def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit 

print(f" fahrenheit value is :{celsius_to_fahrenheit(celsius)}")


# # 3. User will input (2numbers). Write a program to swap the numbers.

# In[27]:


num_1=int(input("Enter number 1 :" ))
num_2=int(input("Enter number 2 :" ))

print(f"Before swapping----> num_1 = {num_1} and num_2 = {num_2}")

temp=num_1
num_1=num_2
num_2=temp

print(f"After swapping----> num_1 = {num_1} and num_2 = {num_2}")


# # 4. Write a program that will give you the sum of 3 digits.

# In[28]:


num_1=int(input("Enter number 1 :" ))
num_2=int(input("Enter number 2 :" ))
num_3=int(input("Enter number 3 :" ))

def sum_of_three_digits(sum):
    sum=num_1+num_2+num_3
    return sum

sum_of_three_digits(sum)


# # 5. Write a program that will reverse a four digit number. Also it checks whether the reverse is true.

# In[69]:


(4321%10)//1


# In[59]:


(4321%100)//10


# In[60]:


(4321%1000)//100


# In[75]:


(4321%10000)//1000


# In[ ]:





# In[76]:


((4321%10)//1)*1000


# In[79]:


(((4321%10)//1)*1000)+(((4321%100)//10)*100)


# In[80]:


(((4321%10)//1)*1000)+(((4321%100)//10)*100)+(((4321%1000)//100)*10)


# In[81]:


(((4321%10)//1)*1000)+(((4321%100)//10)*100)+(((4321%1000)//100)*10)+((4321%10000)//1000)


# In[82]:


# This is the logic


# In[ ]:


if num<1000 or num>9999:
    print("Please enter a valid four-digit number")
else:
    print("Correct")


# In[86]:


num=int(input("Enter a four-digit number: " ))


def reverse(num):
    a=((num%10000)//1000)
    b=((num%1000)//100)*10
    c=((num%100)//10)*100
    d=((num%10)//1)*1000
    return a+b+c+d

if num<1000 or num>9999:
    print("Please enter a valid four-digit number")
else:
    print(f"The reverse of {num} is {reverse(num)}")


# # 6. Write a program that will tell whether the number entered by the user is odd or even.

# In[2]:


num=int(input("Enter a number  : "))

def odd_or_even(num):
    if num%2==0:
        print(f'The number {num} is even')
    else:
        print(f'The number {num} is odd')
        
odd_or_even(num)


# # 7. Write a program that will tell whether the given year is a leap year or not.

# In[ ]:


# year%4 == 0 then it is a leap year
# year%100 == 0 then it is not a leap year
# year%400 == 0 then it is a leap year


# In[7]:


year=int(input("Enter no.of years : "))

def leap_year_or_not(year):
    if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

leap_year_or_not(year)


# # 8. Write a program to find the euclidean distance between two coordinates.

# In[8]:


# (x1,y1) and (x2,y2) are two coordinates
# Euclidean distance= square_root((x2-x1)**2 + (y2-y1)**2)


# In[7]:


import math

x1=float(input("Enter the x-coordinate of first point :" ))
y1=float(input("Enter the y-coordinate of first point :" ))
x2=float(input("Enter the x-coordinate of second point: "))
y2=float(input("Enter the y-coordinate of second point : "))


def euclidean_distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
    

print(f"The euclidean distance between ({x1},{y1}) and ({x2},{y2}) is {euclidean_distance(x1,y1,x2,y2)}")


# In[16]:


import math
math.sqrt(4)


# # 9. Write a program that takes a user input of three angles and will find out whether it can form a triangle or not.

# In[8]:


# A+B+C=180 degree


# In[12]:


A=float(input("Enter first angle : "))
B=float(input("Enter second angle : "))
C=float(input("Enter third angle : "))

def is_triangle(A,B,C):
    if A+B+C==180:
        print(f"Angles {A},{B} and {C} form a traingle")
    else:
        print(f"Angles {A},{B} and {C} does not form a traingle")
    
is_triangle(A,B,C)    


# # 10. Write a program that take a user input of cost price and selling price and determines whether its a loss or a profit.

# In[13]:


# profit=s.p-c.p
# loss= c.p-s.p

# It means if c.p>s.p then loss
#             c.p<s.p then profit


# In[17]:


C_P=float(input("Enter the cost price Rs "))
S_P=float(input("Enter the selling price Rs "))

def loss_or_profit(C_P,S_P):
    if C_P>S_P:
        return (f"It's a loss and the loss is Rs {C_P-S_P}")
    else:
        return (f"It's a profit and the profit is Rs {S_P-C_P}")
 
loss_or_profit(C_P,S_P)


# # 11. Write a program to find the simple interest when the value of principle, rate of interest and time period is given.

# In[ ]:


# SI=(P*R*T)/100


# In[28]:


P=float(input("Enter principal :  "))
R=float(input("Enter rate of interest : "))
T=float(input("Enter time period : "))

def simple_interest(P,R,T):
    return (P*R*T)/100

print(f"The simple interest when Principle is Rs {P} , rate of interest is {R} % and the time period is {T} years is Rs {simple_interest(P,R,T)}")


# # 12. Write a program to find the volume of the cylinder. Also find the cost when the cost of 1 litre milk is 40Rs.

# In[29]:


# V = pi * r**2 * h


# In[30]:


import math
math.pi


# In[34]:


# Cost=Volume(Or quantity) * Cost_per_litre

# Cost of 25litres of milk : 25*40 = Rs 100


# In[45]:


# 1 litre = 1000 cm**3
# 1/1000 litre = 1 cm**3


# In[49]:


r=float(input("Enter radius in cm : "))
h=float(input("Enter height in cm : "))

import math

def volume_of_cylinder(r,h):
    volume=math.pi * r**2 * h
    return volume
print(f"Volume of cylinder is {volume_of_cylinder(r,h)} cm**3 = {volume_of_cylinder(r,h)/1000} litres when radius is {r} cm  and the height is {h} cm ")

print(f"The total cost is Rs {volume_of_cylinder(r,h) / 1000 * 40} when the cost of 1 litre milk is Rs 40 " )
    
    


# # 13.Write a program that will tell whether the given number is divisible by 3 and 6 .

# In[5]:


num=int(input("Enter a number : "))

if num%3==0 and num%6==0:
    print(f"{num} is divisble by 3 and 6")
else:
    print(f"{num} is not divisible by 3 and 6")


# # 14. Calculate the angle between the hour hand and minute hand.

# In[6]:


# Angle = | 30H - (11M/2) |

# where H is the hour in 12-hour format(if it's greater than 12 ,subtract 12)
# M is the minutes


# In[14]:


# Example;
# 19 hour means 7 o'clock
# 19 hours= 19%12 = 7  = 7 o'clock  
# 24 hours = 24%12= 0 = 12 o'clock
# 25 hours = 25%12= 1 = 1 o'clock


# In[16]:


H=float(input("Enter no.of hours: "))
M=float(input("Enter no.of minutes: "))

def calculate_angle(H,M):
    # Ensure hour is in 12-hour format
    H=H%12
    
    # Calculate angle between hour and minute hand
    angle=abs(30*H - (11/2)*M)
    
    # Ensure angle is within 0 to 180 degrees
    angle=min(angle,360-angle)
    
    return angle
print(f" The angle between the hour hand and minute hand is {calculate_angle(H,M)} degree")


# # 15.

# # 16. Write a program that will determine weather when the value of temperature and humidity is provided by the user.
TEMPERATURE(C)      HUMIDITY(%)       WEATHER


   >=30                >=90           Hot and Humid
   >=30                <90            Hot
   <30                 >=90           Cool and Humid
   <30                 <90            Cool        
# In[5]:


temperature=float(input("Enter temperature in C : "))
humidity=float(input("Enter humidity in % : "))

if temperature>=30 and humidity>=90:
    print(" The weather is Hot and Humid ")
elif temperature>=30 and humidity<90:
    print(" The weather is Hot ")
elif temperature<30 and humidity>=90:
    print(" The weather is Cool and Humid ")
else:
    print("The weather is Cool")


# # 17. Write a program that will take three digits from the user and add the square of each digit.

# In[25]:


# Integer division ----> //
# example; 10//3=3
#           4//2=2


# In[6]:


321%10     # accesses the last element 


# In[13]:


(321%100)


# In[14]:


(321%100)//10     # accesses the middle element 


# In[15]:


321//10


# In[16]:


321//100      # accesses the first element 


# In[17]:


321//1


# In[42]:


num=int(input("Enter a 3 digit number : "))

def sum_of_square_of_3_digit(num):        
        a=num//100
        b=(num%100)//10
        c=num%10
        return a**2+b**2+c**2

# Ensure the number is a 3-digit number
if num<100 or num>999:
    print("Please enter a valid 3-digit number")
else:
    print(sum_of_square_of_3_digit(num))   


# # 18. Write a program that will check whether the number is armstrong number or not.

# In[47]:


# Let's say we have a n-digit number N 

# An Armstrong number(also known as narcissistic number or pluperfect number) is a number that is equal to sum of its own digits
# each raised to the power of the number of digits.

# D1**n + D2**n + .................. + Dn**n = N 


# Example;
# 1**3 + 5**3 + 3**3 = 1+125+27 = 153


# In[22]:


# Armstrong number can't be -ve
# It can be +ve and 0

# Examples; 0, 1, 153, 370, 371, and 407,etc


# In[23]:


(4321%10)//1


# In[24]:


(4321%100)//10


# In[25]:


(4321%1000)//100


# In[26]:


(4321%10000)//1000


# In[27]:


# and so on................................


# In[50]:


# for this program while loop is used because we have to do iteration and 
# generally, while loop is used when we repeatedly execute a block of statements while a condition is true


# In[56]:


num=int(input("Enter a number : "))

order=len(str(num))

i=1
sum=0   # initialize sum 

while i<=order:
    digit=(num%(10**i))//(10**(i-1))
    sum+=digit**order
    i+=1
    
if num==sum:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")


# # 19. Write a program that will take user input of (4 digits number) and check whether the number is narcissist number or not.

# In[16]:


num=int(input("Enter a four-digit number: " ))

def narcissist_or_not(num):
    a=((num%10000)//1000)
    b=((num%1000)//100)
    c=((num%100)//10)
    d=((num%10)//1)
    sum=(a**4)+(b**4)+(c**4)+(d**4)
    if num==sum:
        return(f"{num} is a narcissist number")
    else:
        return(f"{num} is not a narcissist number")

if num<1000 or num>9999:
    print("Please enter a valid four-digit number")
else:
    print(narcissist_or_not(num))


# # 20. Write a program that will give you in hand salary after deduction of
# HRA(10%),DA(5%),PF(3%), and tax (if salary is between 5-10lakh - 10%),(11-20lakh - 20%),(20<_ -30%)
# Also print the in hand salary in Rs,K,lakh,Cr,etc......

# In[17]:


# in_hand_salary=(total_salary-HRA-DA-PF-tax)/12


# In[21]:


# 1lakh= 1,00,000


# In[22]:


# 1Crore=1,00,00,000


# In[26]:


total_salary=float(input("Enter your annual salary : "))

HRA=total_salary*(10/100)
DA=total_salary*(5/100)
PF=total_salary*(3/100)

if 500000<total_salary<1000000:
    tax=total_salary*(10/100)    
elif 1100000<total_salary<2000000:
    tax=total_salary*(20/100)    
elif 2000000<total_salary:
    tax=total_salary*(30/100)
else:
    tax=0
    
in_hand_salary=(total_salary-HRA-DA-PF-tax)/12

if in_hand_salary<=999:
    print(f"The in hand salary is Rs {in_hand_salary}")
elif 999<in_hand_salary<=99999:    
    print(f"The in hand salary is {in_hand_salary} K")
elif 99999<in_hand_salary<=9999999:    
    print(f"The in hand salary is {in_hand_salary} lakh")
else:
    print(f"The in hand salary is {in_hand_salary} Crores")
    
         
          


# # 21. Write a menu driver program - 
# 
# 1.(cm to ft)
# 
# 2.(km to miles)
# 
# 3.(usd to inr)
# 
# 4.exit

# In[27]:


# 1 feet = 30.48 centimetres
# 1 cm = 1/30.48 = 0.0328084 ft


# In[28]:


# 1 mile = 1.60934 kilometres
# 1 km = 1/1.60934 = 0.62137 mile


# In[31]:


# 1 USD(United States Dollar) = 83.4421 INR(Indian rupee)


# In[40]:


def cm_to_ft(cm):
    return cm*0.0328084

def km_to_miles(km):
    return km*0.62137

def USD_to_INR(usd):
    return usd*83.4421

def main():
    while True:
        print("\nMenu:")
        print("1. Convert cm to ft")
        print("2. Convert km to miles")
        print("3. Convert USD to INR")
        print("4. Exit")
        
        choice=input("Enter your choice (1/2/3/4): ")
        
        if choice=='1':
            cm=float(input("Enter length in centimeters: "))
            print(f"{cm}cm is equal to {cm_to_ft(cm)}ft")
            
        elif choice=='2':
            km=float(input("Enter distance in kilometers: "))
            print(f"{km}km is equal to {km_to_miles(km)}miles")
        
        elif choice=='3':
            usd=float(input("Enter amount in USD: "))
            print(f"{usd}USD is equal to {USD_to_INR(usd)}INR")
            
        elif choice=='4':
            print("Exiting the program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter a valid choice")
            
main()


# # 22. Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs.

# In[19]:


# dog(x) --------> 1 head , 4 legs
# chicken(y)-------> 1 head , 2 legs

# head--------> x+y
# leg----------> 4x+2y

# dog(x)------>(leg - 2*head)/2 
# chicken(y)--------> head-x


# In[29]:


heads=int(input("Enter no.of heads : "))
legs=int(input("Enter no.of legs : "))

def number_of_chickens_dogs(heads,legs):
    if heads>=1 and legs%2==0:
        dogs=(legs - (2*heads))/2
        chickens=heads-dogs
        if dogs<0 or chickens<0:
            return ("Invalid choice . Please enter correct number of heads and legs")
        else:
            return (f"The number of dogs : {dogs} and the number of chickens : {chickens}")
    else:
        return ("Invalid choice . Please enter correct number of heads and legs")
    

# Ensure the choice of heads and legs are valid
if heads<0 or legs<0:
    print("Invalid choice . Please enter correct number of heads and legs")
elif heads>legs:
    print("Invalid choice . Please enter correct number of heads and legs")
elif heads==0 or legs==0:
    print("No animals are present")
else:
    print(number_of_chickens_dogs(heads,legs)) 


# # 23. Write a program that wil swap numbers

# In[34]:


a=int(input("Enter number1 : "))
b=int(input("Enter number2 : "))

def swap(a,b):
    a
    b
    print(f"Before swapping the numbers are : a={a} and b={b}")
    x=a
    a=b
    b=x
    return (f" After swapping the numbers are : a={a} and b={b}")

swap(a,b)


# # 24. Write a program to find the sum of first n numbers , where n will be provided by the user. 
# Eg if the user provides n=10 the output should be 55

# In[35]:


1+2+3+4+5+6+7+8+9+10


# In[36]:


n=10
(n*(n+1))/2


# In[45]:


n=int(input("Enter a valid integer : "))

def sum_of_n_numbers(n):
    sum=(n*(n+1))/2
    return (f" The sum of first {n} numbers is : {sum}")

# Ensure  n is a positive integer
if n<0:
    print("Invalid value of n . Please enter a valid integer")
else: 
    print(sum_of_n_numbers(n))
    


# # 25. Write a program that can multiply 2 numbers provided by the user without using the * operator

# In[47]:


4*3


# In[56]:


4+4+4


# In[16]:


n1=int(input("Enter first number : "))
n2=int(input("Enter a second number : "))

result=0

for i in range(0,n1):
    result=result+n2    # result+=n2
    
print(result)


# In[38]:


n1=int(input("Enter first number : "))
n2=int(input("Enter a second number : "))

result=0


if n1<0 and n2<0:
    n1=abs(n1)
    n2=abs(n2)
    for i in range(0,n1):
        result=result+n2
    print(result)
    
elif n1<0 or n2<0:
    if n1<0:
        n1=abs(n1)
        n2
        for i in range(0,n1):
            result=result+n2
        print(-result)    
    else:
        n2=abs(n2)
        n1
        for i in range(0,n1):
            result=result+n2
        print(-result)   
        
else:
    for i in range(0,n1): 
        result=result+n2
    print(result)


# # 26. Write a program that can find the factorial of a given number provided by the user.

# In[84]:


import math
math.factorial(3)


# In[85]:


math.factorial(5)


# In[86]:


# factorial(3)= 3*2*1


# In[87]:


# factorial(n)= 1*2*......*n


# In[88]:


# factorial(n)= fact(n-1)*n


# In[98]:


math.factorial(4)*5


# In[99]:


math.factorial(0)


# In[1]:


math.factorial(-1) #  factorial() not defined for negative values


# In[2]:


num=int(input("Enter number : "))


def factorial_of_a_number(num):
    fact=1
    while num>=1:
        fact=fact*num
        num=num-1
    return fact
    
factorial_of_a_number(num)    


# In[24]:


num=int(input("Enter number : "))

def factorial_of_a_number(num):
    
    if num==0 or num==1:
        return 1
    elif num<0:
        return ("Not defined")
    else: 
        fact=1
        while num>1:
            fact=fact*num
            num=num-1
        return fact
    
print(f"Factorial of {num} is {factorial_of_a_number(num)}")  


# # 27. Write a program to print the first 25 odd numbers

# In[34]:


i=1
n=50

for i in range (0,n):
    if i%2!=0:
        print(i)
    


# # 28. Write a program to print whether a given number is prime number or not

# In[19]:


# A number which is divisible by 1 and itself (and is greater than 1) and it is not divisble by any other number is a prime number.
# example; 2,3,5,7,11,13,17,19,23,29,31,37,41...............................


# 0 is neither prime not composite
# -ve numbers are not prime 


# In[42]:


n=int(input("Enter a number: "))

def prime_or_not(n):
   
    if n%1==0 and n%n==0:
        return ("prime number")
    else:
        return ("not prime number")
    
print(f"{n} is a {prime_or_not(n)}")


# In[30]:


import random


# In[37]:


random.randint(i)


# In[47]:


L=[1,2,3,4,5,6,7,8,9]

n=2

for i in L:
    if n%i==0:
        i+=1
        print ("not")


# In[ ]:


count=0
i=1

#while count<=25:
    if i%2!=0:
        print(i)


# # Q.> Given a list of integers,
# Write a python function to move all the even numbers to the front of the list while maintaining their original order. The odd numbers should follow in their original oreder.
# 
# original_list=[1,2,3,4,5,6,7,8,9]
# 
# desired_output=[2, 4, 6, 8, 1, 3, 5, 7, 9]

# In[76]:


# logic

original_list=[1,2,3,4,5,6,7,8,9]

even=[]

for i in original_list:
    if i%2==0:
        print(i)
        even.append(i)
even


# In[79]:


# logic

original_list=[1,2,3,4,5,6,7,8,9]

even=[]
odd=[]

for i in original_list:
    if i%2==0:

        even.append(i)
    else:
        
        odd.append(i)

print(even)
print(odd)


# In[82]:


# solution

original_list=[1,2,3,4,5,6,7,8,9]

even=[]
odd=[]
def even_odd_sort(original_list):
    for i in original_list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)

    print(even)
    print(odd)
    desired_output=even+odd
    return desired_output

print(f"The desired output is {even_odd_sort(original_list)}")


# In[ ]:




