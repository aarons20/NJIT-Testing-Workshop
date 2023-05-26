class bankAccount:
    """
    A class used to represent an bank account

    ...

    Attributes
    ----------
    username : str
        the username of the current person banking
    balance : float
        the amount of money in the bank
    
    Methods
    -------
    transactionOption()
        Asks for input on what the user wants to do,
        based on the option it runs the expected function.
        If anything other than exit, function loops.

    leave()
        Prints thank you and exits the transactionOptions loop.

    viewBalance()
        Prints the amount stored in the bank account
    
    deposit()
        Add funds to your bank account
    
    withdraw()
        Remove funds from your bank account
    """
    username = "username"
    balance = 100.00
    
    def transactionOption(self):
        try:
            print('\n[1] View Balance')
            print('[2] Deposit')
            print('[3] Withdraw')
            print('[4] Exit')

            select = int(input('Select an option: '))
            if select == 1:
                bal = bankAccount.viewBalance(self)
                print('\nCurrent Balance: $'+ str(bal))
            elif select == 2:
                bankAccount.deposit(self)
                print('\nDeposit successful!')
            elif select == 3:
                bankAccount.withdraw(self)
                print('\nWithdrawal successful!')
            elif select == 4:
                bankAccount.leave(self)                
            else:
                print('\nTransaction Error - 405')
                bankAccount.transactionOption(self)
            if select > 0 and select < 4:
                bankAccount.transactionOption(self)
        except:
            raise Exception('Transaction Error - 402')

    def leave(self):
        print('\nThank You')
        quit

    def viewBalance(self):
        try:
            return self.balance
        except:
            raise Exception('Balance Retreival Error - 901')

    def deposit(self):
        amount = float(input('Enter the deposit amount: '))
        if amount > 0:
            newbalance = str((float(self.balance)) + amount)
            self.balance = newbalance
            return self.balance
        else:
            raise Exception('Internal Deposit Error - 212')

    def withdraw(self):
        amount = float(input('Enter the withdrawal amount: '))
        if amount <= float(self.balance):
            newbalance = str((float(self.balance)) - amount)
            self.balance = newbalance
            return self.balance
        else:
            raise Exception('Withdrawal Error - 787')



bank = bankAccount()
bank.transactionOption()
