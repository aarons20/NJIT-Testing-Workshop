from virtualBankLimited import BankAccount
from Exceptions import (
    InternalDepositException,
    WithdrawalException,
    BalanceRetrievalException,
)
import pytest


def test_view_balance_success():
    """
    This is a generic test for the happy path
    It is testing view_balance with a good value (100)
    """
    # Arrange - set up the scenario
    bank_account = BankAccount(username="name", balance=100)
    # Act - do the action that we are testing
    actual_balance = bank_account.view_balance()
    # Assert - Assert that our expected outcome happened. could be assert something equals a value, assert something is true, assert an exception is raised
    assert actual_balance == 100


def test_view_balance_unsuccessful():
    """
    This is a generic test for the unhappy path (error)
    It is testing that view_balance with a bad value (-100) raises an exception
    """
    # Arrange - set up the scenario
    bank_account = BankAccount(username="name", balance=-100)
    # Assert - Assert that an exception is raised
    with pytest.raises(BalanceRetrievalException):
        # Act - do the action that we are testing
        bank_account.view_balance()


# TODO Write Withdraw tests Here
def test_deposit_success():
    """
    This is a generic test for the happy path
    It is testing deposit with a good value (100)
    """
    # Arrange - set up the scenario
    bank_account = BankAccount(username="name", balance=100)
    # Act - do the action that we are testing
    actual_balance = bank_account.deposit(100)
    # Assert - Assert that the outcome is as expected
    assert actual_balance == 200


def test_deposit_negative_amount():
    """
    This is a generic test for the unhappy path (error)
    It is testing that deposit with a bad value (-100) raises an exception
    """
    # Arrange - set up the scenario
    bank_account = BankAccount(username="name", balance=100)
    # Assert - Assert that an exception is raised
    with pytest.raises(InternalDepositException):
        # Act - do the action that we are testing
        bank_account.deposit(-100)


def test_deposit_zero_amount():
    """
    This is a generic test for the unhappy path (error)
    It is testing that deposit with a bad value (0) raises an exception
    """
    # Arrange - set up the scenario
    bank_account = BankAccount(username="name", balance=100)
    # Assert - Assert that an exception is raised
    with pytest.raises(InternalDepositException):
        # Act - do the action that we are testing
        bank_account.deposit(0)


def test_deposit_invalid_data_type():
    """
    This is a generic test for the unhappy path (error)
    It is testing that deposit with a bad value (string) raises an exception
    """
    # Arrange - set up the scenario
    bank_account = BankAccount(username="name", balance=100)
    # Assert - Assert that an exception is raised
    with pytest.raises(InternalDepositException):
        # Act - do the action that we are testing
        bank_account.deposit("one hundred")


def test_withdraw_success():
    # Arrange - set up the scenario
    bank_account = BankAccount(username="name", balance=100)
    # Act - do the action that we are testing
    actual_balance = bank_account.withdraw(50)
    # Assert - Assert that the outcome is as expected
    assert actual_balance == 50


def test_withdraw_negative_amount():
    # Arrange - set up the scenario
    bank_account = BankAccount(username="name", balance=100)
    # Assert - Assert that an exception is raised
    with pytest.raises(WithdrawalException):
        # Act - do the action that we are testing
        bank_account.withdraw(-100)


def test_withdraw_zero_amount():
    # Arrange - set up the scenario
    bank_account = BankAccount(username="name", balance=100)
    # Assert - Assert that an exception is raised
    with pytest.raises(WithdrawalException):
        # Act - do the action that we are testing
        bank_account.withdraw(0)


def test_withdraw_invalid_data_type():
    # Arrange - set up the scenario
    bank_account = BankAccount(username="name", balance=100)
    # Assert - Assert that an exception is raised
    with pytest.raises(WithdrawalException):
        # Act - do the action that we are testing
        bank_account.withdraw(True)
