import pickle
import os
import pathlib

class Account:
    def _init_(self):
        self.accNo = 0
        self.name = ''
        self.deposit = 0
        self.type = ''

    def createAccount(self):
        self.accNo = int(input("Enter the account no : "))
        self.name = input("Enter the account holder name : ")
        self.type = input("Enter the type of account [C/S] : ").upper()
        self.deposit = int(input("Enter The Initial amount(>=500 for Saving and >=1000 for current): "))
        print("\n\n\nAccount Created")

    def showAccount(self):
        print(f"Account Number : {self.accNo}")
        print(f"Account Holder Name : {self.name}")
        print(f"Type of Account : {self.type}")
        print(f"Balance : {self.deposit}")

    def modifyAccount(self):
        print(f"Account Number : {self.accNo}")
        self.name = input("Modify Account Holder Name : ")
        self.type = input("Modify Type of Account : ").upper()
        self.deposit = int(input("Modify Balance : "))

    def depositAmount(self, amount):
        self.deposit += amount

    def withdrawAmount(self, amount):
        self.deposit -= amount

    def report(self):
        print(f"{self.accNo:10} {self.name:20} {self.type:10} {self.deposit:10}")

    def getAccountNo(self):
        return self.accNo

    def getAccountHolderName(self):
        return self.name

    def getAccountType(self):
        return self.type

    def getDeposit(self):
        return self.deposit


def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)


def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            item.report()
        infile.close()
    else:
        print("No records to display")


def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist:
            if item.getAccountNo() == num:
                item.showAccount()
                found = True
    else:
        print("No records found")
    if not found:
        print("Account number not found")


def depositAndWithdraw(num, option):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        mylist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in mylist:
            if item.getAccountNo() == num:
                if option == 1:
                    amount = int(input("Enter the amount to deposit : "))
                    item.depositAmount(amount)
                    print("Your account is updated")
                elif option == 2:
                    amount = int(input("Enter the amount to withdraw : "))
                    if amount <= item.getDeposit():
                        item.withdrawAmount(amount)
                        print("Your account is updated")
                    else:
                        print("You cannot withdraw larger amount")
    else:
        print("No records found")
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        newlist = [item for item in oldlist if item.getAccountNo() != num]
        os.remove('accounts.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        infile.close()
        os.remove('accounts.data')
        for item in oldlist:
            if item.getAccountNo() == num:
                item.modifyAccount()
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')


def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open('accounts.data', 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove('accounts.data')
    else:
        oldlist = [account]
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')


def intro():
    print("\t\t\t\t**")
    print("\t\t\t\tBANK MANAGEMENT SYSTEM")
    print("\t\t\t\t**")
    print("\t\t\t\tBrought To You By : DataFlair\n\n")


# start of the program
ch = ''
num = 0
intro()
while ch != '8':
    print("\tMAIN MENU")
    print("\t1. NEW ACCOUNT")
    print("\t2. DEPOSIT AMOUNT")
    print("\t3. WITHDRAW AMOUNT")
    print("\t4. BALANCE ENQUIRY")
    print("\t5. ALL ACCOUNT HOLDER LIST")
    print("\t6. CLOSE AN ACCOUNT")
    print("\t7. MODIFY AN ACCOUNT")
    print("\t8. EXIT")
    print("\tSelect Your Option (1-8) ")
    ch = input()

    if ch == '1':
        writeAccount()
    elif ch == '2':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 1)
    elif ch == '3':
        num = int(input("\tEnter The account No. : "))
        depositAndWithdraw(num, 2)
    elif ch == '4':
        num = int(input("\tEnter The account No. : "))
        displaySp(num)
    elif ch == '5':
        displayAll()
    elif ch == '6':
        num = int(input("\tEnter The account No. : "))
        deleteAccount(num)
    elif ch == '7':
        num = int(input("\tEnter The account No. : "))
        modifyAccount(num)
    elif ch == '8':
        print("\tThanks for using bank management system")
        break
    else:
        print("Invalid choice")