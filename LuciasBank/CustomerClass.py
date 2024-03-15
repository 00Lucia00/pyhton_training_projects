#!/usr/bin/env python
# coding: utf-8

#Lucias

#Skapa en klass Customer. Den skall ha användarnamn, lösenord och en lista av Accounts. 
#En användare kan ha många konton. 
#Den bör ha en funktion för att kolla om ett inskickat lösenord stämmer, samt en del funktioner som Bank använder sig av. 
#Som add_account, som skall finnas i Bank, kanske skall finnas i Customer och användas. 

class Customer():
    
    def __init__(self,userName,password,accountList = None):
        self.userName = userName
        self.password = password
        if accountList == None:
            self.accountList = ['no acounts regesterd']
        else:
            acInfo = []
            for item in accountList:
                acInfo.append(item.split('/'))
            self.accountList = acInfo
        

    def get_customer(self):
        print('customer details:\n',self.userName,self.password,self.accountList)
        details = [self.userName,self.password,self.accountList]
        return details
    

    def change_customer_password(self,old_password, new_password): #detta är ifall kund vill ändra
        if old_password == self.password:
            self.password = new_password
            print("Password changed successfully")
            return self.password
        print("Somthing wrong, passwored not changed!")
        return False
    
    
    def get_accounts(self): # hämtar alla konton
        if self.accountList != None:
            #for account in self.accountList:
            print(self.accountList)
            return True
        print('no accounts exist!')    
        return False
      
        
    def add_account(self,account_number):
        newAcc = [account_number, 0] 
        if self.accountList == []:
            self.accountList.append(newAcc)
            print("You added your first Account")
            return newAcc[0]
        else:
            for c in self.accountList:
                if c[0] != account_number:
                    self.accountList.append(newAcc)
                    print("Account Added")
                    return newAcc[0]
                print("account already exists")
        return None
    
    def remove_account(self,account_number): # tar bort ett konto om personen är inloggad
        for a in range(len(self.accountList)):
            for b in range(len(self.accountList)):
                if self.accountList[a][b] == account_number:
                    self.accountList.pop(a)
                    print('Account has been removed!')  
                    return self.accountList
        print("Account not found!")
        return None

