# today's example 
class RBI:
    balance = 100

class TDC(RBI):
    def deposit(self):
        amount = int(input("Enter amount you want to deposit:  "))
        RBI.balance += amount
        print(f"You added {amount} rupees. Your current balance is {RBI.balance}.")

    def withdraw(self):
        amount2 = int(input("enter the amount you want to withdraw:  "))
        RBI.balance -= amount2
        print(f"You added {amount2} rupees. Your current balance is {RBI.balance}.")

class Customer(TDC):
    pass

c1 = Customer()
c1.deposit()
c1.withdraw()


    #   yestreday's example 100% sure it is right 

class Burgerking:
    amount = 0
    def __init__(self):
        self.burger_price = 100
        self.fries_price = 50

    def burger(self):
        Burgerking.amount+=self.burger_price
        print("You ate burger")

    def fries(self):
        Burgerking.amount += self.fries_price
        print("You ate fries")

class Dominos:
    def __init__(self):
        self.pizza_price = 200
        self.bread_price = 40

    def pizza(self):
        Burgerking.amount += self.pizza_price
        print("You ate pizza")

    def bread(self):
        Burgerking.amount += self.bread_price
        print("You ate bread")

class Customer(Burgerking,Dominos):
    def __init__(self):
        Dominos.__init__(self)
        Burgerking.__init__(self)

    def bill(self):
        print("Your total bill is ",Burgerking.amount)

c1 = Customer()
c1.burger()
c1.pizza()
c1.fries()
c1.bread()
c1.bill()