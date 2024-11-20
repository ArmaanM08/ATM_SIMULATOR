#importing Module
from random import randint

# defining functions
class ATM:
    def __init__(self):
        self.bal = randint(1000,1000000)
        pass

    def sgnin(self):
        self.success = True
        self.acnt = ["admin",1122]
        self.usr = input("Enter name as per aadhar: ")
        self.pwd = int(input("Enter Password as per card: "))
        if self.usr == self.acnt[0] and self.pwd == self.acnt[1]:
            print(f"=====HELLO {self.usr}=====")
        else:
            print("Try Next Time")
            self.success = False
    def wtdr(self):
        self.wamnt = int(input("Enter Ammount to be Withdrawn: "))
        if self.wamnt>self.bal:
            print("Not Enough Balance")
        else:
            print(f"Rs",{self.wamnt},"Withdrawn Successfully!!")
            self.bal -= self.wamnt
            
    def dpst(self):
        self.damnt = int(input("Enter Ammount to be Deposited: "))
        print(f"Rs",{self.damnt},"Deposited Successfully!!")
        self.bal += self.damnt
        
    def chng_pn(self):
        self.query = input("Did you forgot your pin: ")
        if self.query in "yesYesYES":
            print("Contact Help line: ",randint(9000000000,9999999999))
        else:
            self.chkr = int(input("Enter old password: "))
            if self.chkr == self.acnt[1]:
                self.chngr = int(input("Enter New Password: "))
                self.acnt[1] = self.chngr
                print("New Password set")
            else:
                print("Incorrect")
    def see_bal(self):
        print(self.bal)
            
            
#Main Code ++==============
print('''=================================================
||               ATM SYSTEM                    ||
=================================================''')


obj = ATM()
obj.sgnin()
loop = obj.success
while loop == True:
    optn = int(input('''Enter your option \n1. Withdraw amount \n2. Deposit amount \n3. Change Pin \n4. Check Balance \n5. Exit \n>>> '''))
    if optn == 5:
        print("Thankyou for visiting our ATM!!")
        loop = 0 
    else:
        if optn == 1:
            obj.wtdr()
        elif optn == 2:
            obj.dpst()
        elif optn == 3:
            obj.chng_pn()
        elif optn == 4:
            obj.see_bal()
        else:
            print("Pick a number as listed in the menu above.")
        
    
            

