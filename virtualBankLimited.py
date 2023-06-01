from Exceptions import BalanceRetrievealException, InternalDepositException, WithdrawlException


class BankAccount:
    """
    A class used to represent a bank account

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

    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def transaction_options(self):
        try:
            print('\n[1] View Balance')
            print('[2] Deposit')
            print('[3] Withdraw')
            print('[4] Exit')

            select = int(input('Select an option: '))
            if select == 1:
                bal = BankAccount.view_balance(self)
                print('\nCurrent Balance: $' + str(bal))
            elif select == 2:
                amount = float(input('Enter the deposit amount: '))
                BankAccount.deposit(self, amount)
                print('\nDeposit successful!')
            elif select == 3:
                amount = float(input('Enter the withdrawal amount: '))
                BankAccount.withdraw(self, amount)
                print('\nWithdrawal successful!')
            elif select == 4:
                BankAccount.leave(self)
            else:
                print('\nTransaction Error - 405')
                BankAccount.transaction_options(self)
            if 0 < select < 4:
                BankAccount.transaction_options(self)
        except:
            raise Exception('Transaction Error - 402')

    def leave(self):
        print('\nThank You')
        quit()

    def view_balance(self):
        try:
            return self.balance
        except:
            raise BalanceRetrievealException

    def deposit(self, amount):
        if amount > 0:
            new_balance = (float(self.balance)) + amount
            self.balance = new_balance
            return self.balance
        else:
            raise InternalDepositException

    def withdraw(self, amount):
        if amount <= float(self.balance):
            new_balance = (float(self.balance)) - amount
            self.balance = new_balance
            return self.balance
        else:
            raise WithdrawlException
