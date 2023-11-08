class Account():
    def __init__(self, bank, username, password, balance):
        bank.append(self)
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

    def transfer(self, acc_list, oth_usr, amount, password):
        oth_acc = None
        for acc in acc_list:
            if acc.username == oth_usr:
                oth_acc = acc

        if password == self.password:
            if amount <= self.balance and amount > 0 and oth_acc != None:
                self.balance -= amount
                oth_acc.balance += amount
                print('Successfully Transfered To',oth_acc.username,'| Amount: $'+str(amount),'| New Account Balance: $'+str(self.balance))
            else:
                print('Invalid Transfer Attempted')

    def account_details(self):
        print('Username:',self.username)
        print('Password:',self.password)
        print('Balance:',self.balance)

Bank = []

acc_1 = Account(Bank,'Page','Password',25000)
acc_1.view_balance('Password')
acc_1.withdrawl(15000,'Password')
acc_1.deposit(5760,'Password')

acc_2 = Account(Bank,'Sonny','HMS7',2530000)
acc_2.view_balance('HMS7')
acc_2.transfer(Bank,'Page',500000,'HMS7')
acc_1.view_balance('Password')
