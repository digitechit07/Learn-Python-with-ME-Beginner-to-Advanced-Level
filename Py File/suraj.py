
#       QUESTIONS AND ANSWERS   



#for i in range(1,5):
#    for j in range(1,5):
#        if j<2:
#            print(j,end=" ")
#        else:
#            print(i,end=" ")
#    print()  

#for i in range(1,6):
#    var=1
#    for j in range(i):
#        print(var,end=" ")
#        var*=2
#    print()


#def numbers():
#    for i in range(1,11):
#        print(i,end="   ")
#    print()
#numbers()
#
#def even():
#    for i in range(1,11):
#        if i%2==0:
#            print(i)
#    #print()
#even()

#def factorial():
#  var=1
#  a = int(input(" Enter :  "))
#  for i in range(1,a+1):
#    var=var*i
#  print(var)
#
#factorial()

#def armstrong():
#    n=(input("Enter:  "))
#    sum=0
#    for i in n:
#        int1=int(i)
#        sum+=int1**len(n)
#    if sum==int(n):
#        print("armstrong")
#    else:
#        print("not armstrong")
#armstrong()
#


#for i in range(10,14):
# for j in range(2,i):
#  if i%j==1:
#    print(i)
#    break
#
# 
#for letter in 'python':
# if letter =='h':
#  continue
# print(letter)

#clear



#armstrong number

#num=int(input("enter number : "))
#sum=0
#temp=num
#while temp>0:
#    digit = temp%10
#    sum+=digit**3
#    temp//=10
#if num==sum:
#    print(num,"armstrong number")
#else:
#    print(num,"not armstrong number")

#var = input("enter input:  ")
#sum=0
#for i in var:
# int1=int(i)
# sum=sum+int1**len(var)
#print(sum)
#
#if int(var)==sum:
# print("A")
#else:
# print("n")
#

#var = input("enter input:  ")
#sum=0
#i=0
#while i<len(var):
#    str1 = int(var[i])
#    sum = sum + str1**len(var)
#    i+=1
#print(sum)
#if sum==int(var):
#    print("yes")
#else:
#    print("no")

#gmail = input("Enter :  ")
#if "@" and ".com" in gmail:
#    print("valid")
#else:
#    print('''your mail should contain "@" and ".com" \nex : suraj78@gmail.com ''')

#number = int(input("Enter number :  "))
#number2=str(number)
#if len(number2) == 10:
#    print("ok")
#else:
#    print("Invalid")

#def validation():
#                    username = input("Enter username :  ")
#                    if username=="suraj78":
#                        password= input("Enter password:  ")
#                        if password=="SMK78910":
#                            print("Successfully Login 😍️")
#                            gmail = input("Enter gmail i\'d :  ")
#                            if "@" and ".com" in gmail:
#                                print("mail i\'d validated")
#                                number=int(input("Enter phone number:  "))
#                                if len(str(number))==10:
#                                    print("validated")
#                                    
#                                else:
#                                    print("please enter 10 digit number")
#                            else:
#                                print('''Your mail i\'d should contain "@" and ".com''')
#                        else:
#                            print("Wrong password😐️")
#                    else:
#                        print("Invalid username")
#validation()
                  
                     
#def sum(n1,n2):
#    print(n1+n2)
#sum(1,88)
#

#def pattern(r):
#    for i in range(1,r):
#        for j in range(i):
#            print("*",end=" ")
#        print()
#pattern(6)  

#def numbers(n1,n2):
#    return n1+n2
#print(numbers(2,7)-2)

#def factorial(num):
#    for i in range(1,num):
#        num*=i
#    return num
#print(factorial(5))

#def name():
#    inp = input("Enter :  ")
#    var=""
#    for i in inp:
#        var+=i
#        print(var)
#name()


#def sumeven(input):
#    sum=0
#    for i in range(1,input+1):
#        if i%2==0:
#            sum+=i**2
#    return sum   
#print(sumeven(5))
#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
#def details(name,surname,mname):
#    print(name,mname,surname)
#details(name="suraj",mname="manohar",surname="khandagale")

#def sum(num1,num2,num3=0):
#    return num1+num2+num3
#print(sum(1,2,4))

#def fun(lst):
#    for i in lst.items(                      ):
#        print(i)
#dict = {"a":"aa","b":"bb","c":"cc"}
#fun(dict)

#without using .items 
#dict = {"a":"aa","b":"bb","c":"cc"}
#for i in dict.keys():
#    print(i,dict[i])
    
   
# LAMBDA FUNCTION OR ANONYMOUS

#syntax:
#  lambda arguments : expression

#var= lambda num1,num2 : num1+num2
#print(var(2,3))


#var= lambda num1,num2,num3 : print("num1 is greater")if (num1>num2 and num1>num3)else print("num2 is greatest") if (num2>num1 and num2>num3) else print("num3 is greatest")
#(var(2222,34,7))

#   21 december 2022

# question_1 : write a p[ython program to remove duplicates from list
#input : 

#method_1
#lst = [1,2,3,4,5,2,3]
#lst2 = []
#for i in lst:
#   if i not in lst2:
#        lst2.append(i)
#print(lst2)


#method_2
#lst1 = [1,2,3,4,5,2,3]
#lst2 = []
#for i in range(len(lst1)):
#    if lst1[i] not in lst2:
#        lst2.append(lst1[i])
#print(lst2)

#Question_2 : write a program to check if list is empty or not

#method_1
#lst = []
#abc = bool(lst)
#if abc==False:
#    print("lst is empty")
#else:
#    print("lst is not empty")


#method_2(prefer these one)
#lst=[]
#if len(lst)==0:
#    print("empty")



    

# Question_3 : write a python program that takes two list and return true if they
#               have at least one common number.

#method_1
#lst1 = [1,2,3,4,5]
#lst2 = [6,7,8,9,1]
#
#def func():
#    for i in lst1:
#        for j in lst2:
#            if i==j:
#                return True
#print(func())

#lst1 = ["a",1,"b",3]
#lst2 = ["name","age"]
#dict1 = {}
#dict2 = {}
#lst3 = []
#for i in range(len(lst2)):
#    for j in range(len(lst1)):
#        if i==j:        
#            dict1.update({lst2[i]:lst1[j]})
#print(dict1)
#for i in range(len(lst2)):
#    for j in range(len(lst1)):
#        if i==j:        
#            dict2.update({lst2[i]:lst1[j+2]})
#print(dict2)
#lst3.append(dict1)
#lst3.append(dict2)
#print(lst3)







#lst1 = ["a",1,"b",3,"c",5]
#lst2 = ["name","age"]
#dict1 = {}
#dict2 = {}
#lst3 = []
#for i in range(len(lst2)):
#    for j in range(len(lst1)):
#        if i==j:        
#            dict1.update({lst2[i]:lst1[j]})
#            dict2.update({lst2[i]:lst1[j+2]})
#lst3.append(dict1)
#lst3.append(dict2)
#print(lst3)


#    23 december 2022                ******************************************


#abc = lambda x : x[::-1]
#print(abc("suraj"))


#aa = "rahullovedipali"
#bb = int(input("how many letters you want : "))
#for i in range(bb):
#    cc = input("Enter : ")
#    dd = aa.index(cc
#    print(aa[dd])


# lambda inside user define function

#def double(num):
#    return lambda x : num*x
#doubler = double(2)
#print(doubler(3))

#def func(num):
#    return lambda x : num**x
#aa = func(2)
#print(aa(3))


#var= lambda num1,num2,num3 : print("num1 is greater")if (num1>num2 and num1>num3)else print("num2 is greatest") if (num2>num1 and num2>num3) else print("num3 is greatest")
#(var(2222,34,7))


#              26th dec 2022        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#var = lambda x , y : x+y
#print(var(9,0))


#map() function 

#lst = [1,2,3,4,5] 
#def square(num):
#    return num**2
#var = map(square,lst)
#print(list(var))

#lst1 = [1,2,3]
#lst2 = [3,4,5]
#lst3 = [4,5,6]
#
#def sqr(num1,num2,num3):
#    return num1**2,num2**2,num3**2
#print(list(map(sqr,lst1,lst2,lst3)))

                                                                                                                                                                                                                                                                                                                                                                                 
#lst1 = [10,22,30]
#lst2 = [1,2,3]
#
#def div(num1,num2):
#    return (num1/num2)
#var = map(div,lst1,lst2)
#print(list(var))

#colors = ['red','blue','green']
#var = map(list,colors)
#print(list(var))

            # 26th dec 2022      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
   
#lst = ['a','b','c','d']
#def func(strg):
#    return strg.upper()
#
#var = map(func,lst)
#print(list(var)

               #FILTER

#lst = [1,2,3,4,5,6]
#def even(num):
#    return num%2==0
#var = filter(even,lst)
#print(tuple(var))

#Pint numbers from list which are greater than 5
#lst = [6,2,9,8,1,0,97]
#def greater(num):
#    return num>5
#var = filter(greater,lst)
#print(list(var))


#lst = ['a','b','e','p','i','w','o','y','u','a']
#def func(let):
#    if 'a' in let:
#        return True
#    elif 'e' in let:
#        return True
#    elif 'i' in let:
#        return True
#    elif 'o' in let:
#        return True
#    elif 'u' in let:
#        return True
#var = filter(func,lst)
#print(list(var))

#lst = ['a','b','e','p','i','w','o','y','u','a']
#def func(let):
#    if 'a'or'e'or'i'or'o'or'u' in let:
#        return True
#var = filter(func,lst)
#print(list(var))

                #28th december 2022         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-

#lst = [-1,9,8,-1,6,-12]
#def func(num):
#    return num<0
#var = filter(func,lst)
#print(list(var))

#lst = "hello 23:99 jhsdgfk "
#def func(num):
#    if num.isdigit():
#     return True
#var = filter(func,lst)
#print(list(var))

#lst = [1,2,-3,9,-8,-6,2]
#def func(num):
#    return num<0
#var = list(filter(func,lst))
#print(var)
#
#def func2(num2):
#    return -num2
#var2 = list(map(func2,var))
#print(var2)




#lst = [1,2,-3,9,-8,-6,2]
#var = list(filter(lambda x : x<0,lst))
#print(var)
#
#var2 = list(map(lambda y : -y,var))
#print(var2)

#lst = [1,2,-3,9,-8,-6,2]
#var = list(map(lambda y : -y,list(filter(lambda x : x<0,lst))))
#print(var)


#lst = [1,2,-3,9,-8,-6,2]
#nlst = [3,8,6]
#for i in nlst:
#    if -i in lst:
#        var = lst.index(-i)
#        lst[var]=i
#
#print(lst)


#                  29th dec 2022            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



#lst = [1,2,-6,3,4,5,-2,-4,-9,32]
from functools import reduce
  
#def sum(a,b):
#    return a+b
#print(reduce(sum,lst))

#print(reduce(lambda a,b: a+b,lst))

#var = list(filter(lambda x:x%2==0,lst))
#print(var)
#lst2 = [1,2,3,4,5]
#print(reduce(lambda x,y:x*y,lst2))

#print(reduce(lambda x,y:return x if x<y else return y,lst2))

#def great(a,b):
#    if a>b:
#        return a
#    else:
#        return b
#print(reduce(great,lst2))

#print(reduce(lambda a,b : b if a<b else a,lst2))


#lst = [1000,8500,9000,250,8001,1]
#print(list(filter(lambda x: x<8000,lst)))
#
#print(list(map(lambda y:y+2000,list(filter(lambda x: x<8000,lst)))))


#     Find factorial of number:         
#num = int(input("enter number:  "))
#lst = []
#for i in range(1,num+1):
#    lst.append(i)
#print(reduce(lambda x,y:x*y,lst))
#


#                   30 dec 2022             @@@@@@@@@@@@@@@@@@@@@@@@@@@@
#                   RECURSION
#def factorial(n):
#    if n ==0 or n==1:
#        return 1
#    else:
#        return n*factorial(n-1)
#print(factorial(5))

#def sum(num):
#    if num>0:
#        sum(num-1)
#        print(num)
#sum(5)

#a=0
#def add(num):
#    if num>0:
#        return (num+add(num-1))
#    else:
#        return 0    
#print(add(5))

#FACTORIAL
#def factorial(num):
#    if num==1:
#        return 1
#    else:
#        return num*factorial(num-1)
#print(factorial(4))
#print(factorial(5))

#FIBONACCI SERIES
         

#                   2nd january 2022            @@@@@@@@@@@@@@@@@@@@@@@@@@@@


#lst = [1,[2,3,{'a':[2,4,6,{'b':[9,8]}]}]]
#print(lst[1][2]['a'.keys][3]['b'][0])
#
#class Demo:
#    def __init__(self):
#        self.name = "suraj"
#        self.age = 22
#
#    def details(self):
#        print("name: ",self.name," Age: ",self.age)
#stud = Demo()
#print(stud.name)
#stud.details()


#                   3rd january 2022            @@@@@@@@@@@@@@@@@@@@@@@@@@@@


#class Person:
#    def __init__(self,name,surname):
#        self.name = name
#        self.surname = surname
#        print(self.name,self.surname)
#obj = Person(" "," ")

#               04 january 2023             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#def caps(txt):
#    return txt.upper()
#
#def demo(func):
#    var = func("hello")
#    print(var)
#demo(caps)


# returning a function from another function

#def addition(num1):
#    def add(num2):
#        print(num1+num2)
#    return add
#var = addition(2)
#var(1)


#def number(n1):
#    def power(n2):
#        print(n1**n2)
#    return power
#var = number(4)
#var(2)


#lst1 = [12,19,8,6,11,1,10,23]
#lst2 = [8,6,11,23,100]
#
#def func1(nums1):
#    def func2(nums2):
#        for i in nums2:
#            if i in nums1:
#                print(f"{i} of lst2 is present in lst1") 
#            else:
#                print(f"\n{i} of lst2 is not present in lst1") 
#    return func2
#var = func1(lst1)
#var(lst2)     



##                  09/10/2022          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#array = [5,4,3,1,2]
#n= len(array)
#for i in range(n):
#    for j in range(i+1,n):
#        if array[i]>array[j]:
#            array[i],array[j]=array[j],array[i]
#print(array)

#                   10-01-2022          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# dic=[]
# dict1 = {'d':1,'c':2,'b':1,'a':4}
# var = dict1.keys()
# print(var)
# var2 = str(var)
# print("Print;   ",var2)
# # for i in var2:
# #     dic.append(i)
# print(dic)
# # dict1 = {11:1,22:2,333:1,44:4}
# # var = dict1.keys()
# # var2 = list(var)
# # print(var2)
# # print(lst)


# def dec(x):
#     return x+1
# def inc(x):
#     return x-1
# def demo(func,x):
#     var = func(x)
#     print(var)
# demo(inc,3)
# demo(dec,4)

# def star(func):
#     def inner(*args):
#         print("*"*10)
#         func(*args)
#         print("*"*10)
#     return inner

# def percent(func):
#     def inner(*args):
#         print("%"*10)
#         func(*args)
#         print("%"*10)
#     return inner

# @percent
# @star
# def msg(txt):
#     print(txt)

# msg("HEllo")


#           13-01-2023                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2

# def sortdict(var):
#         lst = list(var.keys())
#         for j in range(len(lst)):
#             for i in range(len(lst)-1):
#                 if ord(lst[i])>ord(lst[i+1]):
#                     lst[i],lst[i+1]=lst[i+1],lst[i]
#         dict2 = {}
#         for i in lst:
#             dict2.update({i:var[i]})
#         print(dict2)

# dict1 = {'c':3,'d':4,'b':2,'a':1}
# sortdict(dict1)

# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def year2(cls,name,year):
#         return cls(name,2023-year)
     
    
# obj = Dog("runo",7)
# print(obj.name)
# print(obj.age)

# obj2 = Dog.year2("champ",2013)
# print(obj2.name)
# print(obj2.age)

# class Demo:
#     @staticmethod
#     def add(a,b):
#         print(a+b)
#         return a*b
# print(Demo.add(2,3))
    
#                       Inheritance                 16-01-2023      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# class Father:
#     def car(self):
#         print("mercedes")
#     def bike(self):
#         print("duke 390")

# class Child(Father):
#     pass

# obj = Child()
# obj.car()
# obj.bike()

# class Father:
#     def demo(self):
#         print("father class")
# class Child(Father):
#     def demo(self):
#         print("child class")
# c1 = Child()
# c1.demo()

#           subclassing             @@@@

# note : object is an instance of class

# class Father:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# class Child(Father):
#     def __init__(self,name,age):
#         # super().__init__(name,age)        # self parameter not required
#         Father.__init__(self,name,age)      # self parameter required
#         print(self.name)

# c1 = Child("sonu",21)
# c1.name

#                   17-01-2023                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@2

#    ***MULTIPLE INHERITANCE***
#        
# class Father:
#     def driving(self):
#         print("driving")
# class Mother:
#     def cooking(self):
#         print("cooking")
# class Child(Father,Mother):
#     def playing(self):
#         print("playing")
# c1 = Child()
# c1.driving()
# c1.cooking()
# c1.playing()

# class First:
#     def __init__(self,num1):
#         self.num1 = num1
# class Second:
#     def __init__(self,num2):
#         self.num2 = num2
# class Third(First,Second):
#     def __init__(self,num1,num2):
#         First.__init__(self,num1)
#         Second.__init__(self,num2)

#         num3 = self.num1+self.num2
#         print("addition:  ",num3)
# t1 = Third(10,20)

#                   18-01-2001                  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# class A:
#     def a(self):
#         print("A")
# class B:
#     def a(self):
#         print("B")
# class C(B,A):
#     def c(self):
#         print("c")

# obj = C()
# obj.a()

# today's example 
# class RBI:
#     balance = 100

# class TDC(RBI):
#     def deposit(self):
#         amount = int(input("Enter amount you want to deposit:  "))
#         RBI.balance += amount
#         print(f"You added {amount} rupees. Your current balance is {RBI.balance}.")

#     def withdraw(self):
#         amount2 = int(input("enter the amount you want to withdraw:  "))
#         RBI.balance -= amount2
#         print(f"You added {amount2} rupees. Your current balance is {RBI.balance}.")

# class Customer(TDC):
#     pass

# c1 = Customer()
# c1.deposit()
# c1.withdraw()


    #   yestreday's example 100% sure it is right 

#class Burgerking:
#    amount = 0
#    def __init__(self):
#        self.burger_price = 100
#        self.fries_price = 50
#
#    def burger(self):
#        Burgerking.amount+=self.burger_price
#        print("You ate burger")
#
#    def fries(self):
#        Burgerking.amount += self.fries_price
#        print("You ate fries")
#
#class Dominos:
#    def __init__(self):
#        self.pizza_price = 200
#        self.bread_price = 40
#
#    def pizza(self):
#        Burgerking.amount += self.pizza_price
#        print("You ate pizza")
#
#    def bread(self):
#        Burgerking.amount += self.bread_price
#        print("You ate bread")
#
#class Customer(Burgerking,Dominos):
#    def __init__(self):
#        Dominos.__init__(self)
#        Burgerking.__init__(self)
#
#    def bill(self):
#        print("Your total bill is ",Burgerking.amount)
#
#c1 = Customer()
#c1.burger()
# c1.pizza()
# c1.fries()
# c1.bread()
#c1.bill()



