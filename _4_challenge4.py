# challenge 4 - Implement a Banking Account

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance 
    
class SavingsAccount(Account):

    def __init__(self,interestRate,title,balance):
            self.interestRate = interestRate
            super().__init__(title, balance)
            
title = input("Enter the title :")
balance = input("Enter the balance :")
interest_Rate = input("Enter the interestRate :")

savingsAccount_obj = SavingsAccount(title,balance,interest_Rate)
print(savingsAccount_obj)

title = input("Enter the title :")
balance = input("Enter the balance :")
interest_Rate = input("Enter the interesRate :")

savingsAccount_obj = SavingsAccount(title,balance,interest_Rate)