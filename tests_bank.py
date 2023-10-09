from virtualBankLimited import BankAccount
from Exceptions import InternalDepositException, WithdrawalException, BalanceRetrievalException
import pytest
import coverage

def test_view_balance_success():
        bank_account = BankAccount(username= 'name', balance=100)
        assert bank_account.view_balance() == 100
