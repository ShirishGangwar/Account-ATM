
class Bank:
    def __init__(self,Bankname,Branch):
        self.Bankname=Bankname
        self.Branch=Branch
    def show(self):
        print("Bankname : ",self.Bankname)
        print("Branch : ",self.Branch)
    Bankname=input("enter your bank name : ")
    Branch=input("enter your branch : ")
    def __init__(self,username,aadhar,pan,address,accountNo,pin):
        self.username=username
        self.aadhar=aadhar
        self.pan=pan
        self.address=address
        self.balance=0.0
        self.accountNo=accountNo
        self.pin=pin
        print(f'Hello {self.username} cong! your account succesfully')
    def show1(self):
        print("username : ",self.username)
        print("aadhar : ",self.aadhar)
        print("pan : ",self.pan)
        print("address : ",self.address)
        print("accountNo : ",self.accountNo)
        print("pin : ",self.pin)

    def deposit(self,amount):
        input_accountno=input("enter your accountNo : ")
        input_pin=input("enter your pin : ")
        if input_accountno==self.accountNo and input_pin==self.pin:
            self.balance=self.balance+amount
            print(f'{amount} deposited succesfully')
        else:
            print("your data mismatch")
    def withdraw(self,amount):
        input_accountno = input("enter your accountNo : ")
        input_pin = input("enter your pin : ")
        if input_accountno == self.accountNo and input_pin == self.pin:
            if amount<self.balance:
                self.balance=self.balance-amount
                print(f'{amount} withdraw successfully')
            else:
                print("Insufficent Fund...")
        else:
            print("your data mismatch")
    def Ministatement(self):
        input_accountno = input("enter your accountNo : ")
        input_pin = input("enter your pin : ")
        if input_accountno == self.accountNo and input_pin == self.pin:
            print('your account balance is',self.balance)
        else:
            print("Your Data mismatch")


username=input("enter your name : ")
aadhar=input("enter your aadhar number : ")
pan=input("enter your pan : ")
address=input("enter your address : ")
accountNo=input("enter the accountNo : ")
pin=input("enter the pin : ")


b=Bank(username,aadhar,pan,address,accountNo,pin)
b.show()
b.show1()
while True:
    print("please select any option")
    print("1.Deposit\n2.Withdraw\n3.Ministatement\n4.Stop")
    option=int(input("choice your option : "))


    if option==1:
        amount=float(input("enter deposit amount : "))
        b.deposit(amount)
    elif option==2:
        amount=float(input("enter your withdraw amount : "))
        b.withdraw(amount)
    elif option==3:
        b.Ministatement()
    elif option==4:
        print(f'Thanks for using {b.Bankname}-ATM')
        break
