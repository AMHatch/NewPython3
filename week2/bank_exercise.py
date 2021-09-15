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