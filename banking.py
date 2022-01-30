import os
import pickle
import pathlib

# account class
class Account:
    acc_number = 0
    holder_name = ''
    deposit = 0
    type = ''

    # here we creating new Account
    def createAccount(self):
        self.acc_number = int(input('Account number : '))
        self.holder_name = input('Holder Name : ')
        self.deposit = int(input('Deposit amount (>=500) : '))
        self.type = input('Account type : ')
        print('Account created......')

# end of account class

# for creating new account
def newAccount():
    account = Account()
    account.createAccount()
    writeAccount(account)

# Balance enquirey
def accountinfo(num):
    file = pathlib.Path('account.data')

    if file.exists():
        openFile = open('account.data', "rb")
        loadFile = pickle.load(openFile)
        openFile.close()

        for acc in loadFile:
            if (acc.acc_number == num):
                print('------------------------------------')
                print('Account Holder : {}'.format(acc.holder_name))
                print('Your account balance : {}'.format(acc.deposit))
                print('------------------------------------')
        else:
            print('No data for this account number😥')

# deposit amount
def depositAmount(num):
    file = pathlib.Path('account.data')

    if file.exists():
        openFile = open('account.data', "rb")
        dataList = pickle.load(openFile)
        openFile.close()
        os.remove('account.data')

        for acc in dataList:
            if(acc.acc_number == num):
                amountDeposit = int(input("Deposit amount : "))
                acc.deposit += amountDeposit
                print('Deposited successfully...')
    else:
        print('No data....')
    outFile = open('newAccount.data', "wb")
    pickle.dump(dataList, outFile)
    outFile.close()
    os.rename('newAccount.data', 'account.data')


# Account List
def accountList():
    file = pathlib.Path('account.data')

    if file.exists():
        openFile = open('account.data', "rb")
        accountList = pickle.load(openFile)
        openFile.close()
        print('-----------Account List------------')
        for accList in accountList:
            print('------------------------------------')
            print('Account Number : {}'.format(accList.acc_number))
            print('Holder Name : {}'.format(accList.holder_name))
            print('Net Balance : {}'.format(accList.deposit))
            print('Account Type : {}'.format(accList.type))
            print('-------------------------------------')
    else:
        print('No data...')

# basically this function is for creating text file
def writeAccount(account):
    file = pathlib.Path('account.data')

    if file.exists():
        openFile = open('account.data', "rb")
        oldList = pickle.load(openFile)
        oldList.append(account)
        openFile.close()
        os.remove('account.data')
    else:
        oldList = [account]
    openFile = open('newAccount.data', "wb")
    pickle.dump(oldList, openFile)
    openFile.close()
    os.rename('newAccount.data', 'account.data')

# starting of the code
def into():
    print('********Welcome*********')
    print('****Bank of Horseman****')
    print()


into()

ch = ''
num = 0
while(ch != '0'):
    print('0 : Exit')
    print('1 : New Account')
    print('2 : Deposit')
    print('3 : Withdrawl')
    print('4 : Balance Enquirey')
    print('5 : All Account List')

    print('Choose option above....')
    ch = input()

    if (ch == '1'):
        newAccount()
    elif (ch == '2'):
        num = int(input('enter account number : '))
        depositAmount(num)
    elif(ch == '4'):
        num = int(input('enter account number : '))
        accountinfo(num)
    elif(ch == '5'):
        accountList()
