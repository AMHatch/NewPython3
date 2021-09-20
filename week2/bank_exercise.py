class AccountHolder:
    def __init__(self, fName, accountType, status, balance):
        self.fName = fName
        self.accountType = accountType
        self.status = status
        self.balance = balance
        
class Bank:
    def __init__(self, name, address):
        self.name = name 
        self.address = address 
        self.accounts = []

    def new_account(self, fName, accountType, status, balance):

        newMember = AccountHolder(self, fName, accountType, status, balance):
        self.accounts.append(newMember)

    def show_all_memebers(self):
        for memberObj,index in accounts:
            print(f'{index + 1 }: {memberObj.fName}')

    def showAccount(self):
        memberID = int(input(f'select memeber to show details'))
        id = memberID - 1
        print(f'')




bankDC = Bank('Bank of Digital Crafts','42 Developer Lane')



bankDC.newAccount()
