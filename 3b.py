#(b)	Write a python program to design a class ‘Account’ that stores the current balance, interest rate and account number of a bank account. Your class should provide methods to withdraw deposit and add interest to the account. The user should only be allowed to withdraw money up to some overdraft limit. If an account goes overdrawn, there is fee charged.
class Account:
    def __init__(self):
        balance = 1000
        self.balance=balance
        intrest_rate = 2
        self.intrest = intrest_rate
        acc_no = 1111
        self.acc_no = acc_no
        self.overdraw = 100
    def deposit(self,amt):
        self.balance += amt
    def bal(self):
        print("Balance is ",self.balance)
    def intr(self):
        print("Intrest Rate is:\t",self.intrest)
    def withdraw(self,amt):
        if self.balance >= amt:
            if self.overdraw > amt:
                self.balance = self.balance - amt - 5
                print("Amount Withdrawn Current Balance is\t", self.balance)
            else:
                self.balance = self.balance -amt
                print("Amount Withdrawn Current Balance is", self.balance)
        else:
            print("Not Enough Balance")
obj=Account()
while True:
    ch = int(input("Enter 1 to Withdraw, Enter 2 to Show Intrest, 3 to Deposit, 4 to Balance"))
    if ch == 3:
        obj.deposit(int(input("Enter Amount")))
    elif ch==4:
        obj.bal()
    elif ch==2:
        obj.intr()
    elif ch==1:
        obj.withdraw(int(input("Enter Amount To Withdraw")))
    else:
        print("e")
