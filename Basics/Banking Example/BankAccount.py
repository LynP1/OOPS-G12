class Bank():
    def __init__(self,name,def_list,address,phone):
        self.name = name
        self.list = def_list
        self.address = address
        self.phone = phone

class Account():
    def __init__(self, bank, username, password, balance):
        bank.list.append(self)
        self.username = username
        self.password = password
        self.balance  = balance

    def deposit(self, amount, password):
        if password == self.password:
            if amount > 0:
                self.balance += amount
                print('Successfully Deposited: $'+str(amount),'| New Account Balance: $'+str(self.balance))
            else:
                print('Invalid Deposit Amount')
        else:
            print('Incorrect Password')

    def withdrawl(self, amount, password):
        if password == self.password:
            if amount <= self.balance and amount > 0:
                self.balance -= amount
                print('Successfully Withdrawled: $'+str(amount),'| New Account Balance: $'+str(self.balance))
            else:
                print('Invalid Withdrawl Amount')
        else:
            print('Incorrect Password')

    def view_balance(self,password):
        if password == self.password:
            print('Account Balance: $'+str(self.balance))
        else:
            print('Incorrect Password')

    def transfer(self, bank, oth_usr, amount, password):
        oth_acc = None
        for acc in bank.list:
            if acc.username == oth_usr:
                oth_acc = acc

        if password == self.password:
            if amount <= self.balance and amount > 0 and oth_acc != None:
                self.balance -= amount
                oth_acc.balance += amount
                print('Successfully Transfered To',oth_acc.username,'in',bank.name,'| Amount: $'+str(amount),'| New Account Balance: $'+str(self.balance))
            else:
                print('Invalid Transfer Attempted')
        else:
            print('Incorrect Password')

    def account_details(self):
        print('Username:',self.username)
        print('Password:',self.password)
        print('Balance:',self.balance)