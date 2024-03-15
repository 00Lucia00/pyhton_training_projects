#!/usr/bin/env python
# coding: utf-8


#Lucias
#Skapa en klass Account. Den skall ha kontonummer och saldo. 
#Den bör ha en funktion för att ändra saldot med en summa, och en funktion för att hämta nuvarande saldot. 

class Account():
    

    def __init__(self, account_number,balance = 0):
        self.account_number = account_number
        self.balance = balance
        
                
    def get_balance(self): # hämtar ett specifikt kontos innehåll
            print(f'Account: {self.account_number}')
            print(f'current balance: {self.balance}')
        
    def deposit(self,amount): # läggtill pengar
            if amount > 0:
                self.balance += amount
                print("Amount Deposited:",amount, 'currentBalance:', self.balance)
                return self.balance
            return None
    def withdraw(self,amount): # ta bort pengar
        if self.balance >= amount:
            self.balance -= amount
            print("Your current balance:", self.balance)
            return self.balance
        else:
            print("You have insufficient funds  ")
            return None
            
 
    

