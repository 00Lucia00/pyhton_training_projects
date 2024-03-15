#!/usr/bin/env python
# coding: utf-8
#Lucias
import random as r

class Bank():
    
    currentCustomer = None # checks if any customer is loged in
    
    def __init__(self, name, customerList): # construktor 
        print(f"Hi this is {name} Bank") # validates objeckt initialazation
        self.customerList = customerList  #takes in name for your bank name and a customer list
        
        
    def login(self, name, password): 

        for c in self.customerList:
            if name == c[0]:
                if password == c[1]:
                    print(f"Welcome {name} what can we do for you")
                    self.currentCustomer = c
                    return self.currentCustomer
        print("Invalid password or username, please try again!")
        return None
    
    def logout(self):
        self.currentCustomer = None
        print("You have Logout!")
        return True
    
    def get_customers(self):
        print('Current customers: ')
        for c in self.customerList: #skriver ut anatal kunder i listan
            print(c[0])
        print('This bank has', len(self.customerList), 'customers')#detta visar antal kunder i listan
    
    def add_customer(self,name, password):
        for c in self.customerList:
            if name == c[0]:  
                print("There is already a userAccount with that name!")
                return False
        
        print("Welcome to our Bank " + name)
        self.customerList.append([name, password])
        return True

    def get_customer(self,name):
        for customer in self.customerList:
            if customer[0] == name:
                print(customer)
                return customer
        print("Customer not found!")
        return None
   
    def change_customer_password(self,name, new_password): # detta är ifall admin vill ändra
        for c in self.customerList:
            if c[0] == name:
                self.customerList[self.customerList.index(c)][1] = new_password
                print("Password changed successfully")
                return new_password
        print("Customer not found!")
        return False
    
    def remove_customer(self,name):
        for customer in self.customerList:
            if customer[0] == name:
                self.customerList.remove(customer)
                print("Customer removed!")
                return True
        print("Customer not found!")
        return False
    
    def add_account(self,account_number):
        for customer in self.customerList:
            if customer == self.currentCustomer:
                customer.append(f'{account_number}/0')
                print("Account updated")
                return self.customerList
        print("No active user")
        return False
   
    def get_accounts(self):
        if self.currentCustomer != None:
            return self.currentCustomer[2:]
        print('must login to see accounts')
        return None
    
    def get_account(self,account_number): # hämtar ett specifikt konto ur admin perspektiv
        for a in range(len(self.customerList)):
            for b in range(len(self.customerList[a])):
                find = self.customerList[a][b].find(account_number)
                if find != -1:
                    acInfo = self.customerList[a][b].split('/')
                    print(find,acInfo[0],"currentBalance",acInfo[1])
                    return acInfo
        print("Account not found!")
        return None
   
    def remove_account(self,account_number): # tar bort ett konto om personen är inloggad
        if self.currentCustomer != None:
            for a in range(len(self.currentCustomer)):
                find = self.currentCustomer[a].find(account_number)
                if find != -1:
                    acInfo = self.currentCustomer[a].split('/')
                    print(acInfo[0],'This account has been removed!')
                    self.currentCustomer.pop(a) #pop tar indexnr och remove tar variable   
                    return account_number # så detta konto kan tas bort i kund object, skickar vidare info
            print("Account not found! cheack if user that the account belongs to is loged in")
        print('please log in to remove account.') 
        return None
                                  
     #bugg // samma siffror i konton kan göra så konton mixas        
    def deposit(self, account_number, amount): #detta ändrar konto innehåll utifrån admin perpektiv
        for a in range(len(self.customerList)):
            for b in range(len(self.customerList[a])):
                find = self.customerList[a][b].find(account_number)
                if find != -1:
                    acInfo = self.customerList[a][b].split('/')
                    acInfo[1] = int(acInfo[1]) + amount
                    print(acInfo[0], 'New balance:',acInfo[1] )
                    self.customerList[a][b] = f'{acInfo[0]}/{acInfo[1]}'
                            #customer.pop(b)
                            #customer.insert(b, acInfo)  
                    return self.customerList
        print("Account not found!")
        return False
                
    
    def withdraw(self, account_number, amount):
        for a in range(len(self.customerList)):
            for b in range(len(self.customerList[a])):
                find = self.customerList[a][b].find(account_number)
                if find != -1:
                    acInfo = self.customerList[a][b].split('/')
                    acInfo[1] = int(acInfo[1]) - amount
                    print(acInfo[0], 'New balance:',acInfo[1] )
                    self.customerList[a][b] = f'{acInfo[0]}/{acInfo[1]}'
                            #customer.pop(b)
                            #customer.insert(b, acInfo)  
                    return self.customerList
        print("Account not found!")
        return False
    


# In[ ]:


    def GenerateAccountNr(self):
        return f'konto{r.randrange(11,99)}'


# In[ ]:



  





