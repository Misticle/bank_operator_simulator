import pytest
from decimal import Decimal
from bank_operator_simulator import models
from bank_operator_simulator import exceptions as exc


# 1. add_client
def test_add_client_success(sample_bank, sample_client) -> None:
    """Проверка регистрации нового клиента"""
    sample_bank.add_client(sample_client)
    assert sample_client.passport in sample_bank.client_db

def test_client_already_exist(sample_bank, sample_client) -> None:
    """Проверка внесения уже существующего в базе клиента"""
    sample_bank.add_client(sample_client)
    with pytest.raises(exc.ClientAlreadyExistsError):
        sample_bank.add_client(sample_client)

def test_client_not_exist(sample_bank) -> None:
    """Проверка ошибки поиска несуществующего клиента"""
    with pytest.raises(exc.ClientNotFoundError):
        sample_bank.get_client('abcd efghijk')

# 2. deposit_money

def test_deposit_success(sample_bank, sample_client) -> None:
    test_deposit = Decimal('500')
    sample_bank.add_client(sample_client)
    sample_bank.deposit_money(sample_client.passport, test_deposit)
    assert sample_bank.client_db[sample_client.passport].deposit == test_deposit

@pytest.mark.parametrize(
    'wrong_amount',
    [Decimal('0'), Decimal('-500')],
    ids = ['zero', 'negative']
)
def test_invalid_amount_error(sample_bank, sample_client, wrong_amount: Decimal) -> None:
    sample_bank.add_client(sample_client)
    with pytest.raises(exc.InvalidAmountError):
        sample_bank.deposit_money(sample_client.passport, wrong_amount)

# 3. issue_loan

def test_issue_loan_success(sample_bank, sample_client) -> None:
    test_loan = Decimal('500')
    bank_reserve_delta = sample_bank.reserves - test_loan
    sample_bank.add_client(sample_client)
    sample_bank.issue_loan(sample_client.passport, test_loan)
    assert sample_bank.client_db[sample_client.passport].credit == test_loan
    assert sample_bank.client_db[sample_client.passport].deposit == test_loan
    assert sample_bank.reserves == bank_reserve_delta

def test_issue_loan_insufficient_funds(sample_bank, sample_client) -> None:
    test_loan = Decimal('500')
    sample_bank.add_client(sample_client)
    sample_bank.reserves = Decimal('0')
    with pytest.raises(exc.InsufficientBankFundsError):
        sample_bank.issue_loan(sample_client.passport, test_loan)

# 4. погашение

def test_repay_loan_success(sample_bank, sample_client) -> None:
    test_loan = Decimal('500')
    test_repay = test_loan
    zero_loan = test_loan - test_repay
    sample_bank.add_client(sample_client)
    sample_bank.issue_loan(sample_client.passport, test_loan)
    sample_bank.repay_loan(sample_client.passport, test_repay)
    assert sample_bank.client_db[sample_client.passport].credit == zero_loan

def test_repay_loan_insufficient_funds(sample_bank, sample_client) -> None:
    test_loan = Decimal('500')
    test_repay = test_loan
    sample_bank.add_client(sample_client)
    sample_bank.issue_loan(sample_client.passport, test_loan)
    sample_bank.client_db[sample_client.passport].deposit = Decimal('0')
    with pytest.raises(exc.InsufficientClientFundsError):
        sample_bank.repay_loan(sample_client.passport, test_repay)

def test_repay_loan_overpay(sample_bank, sample_client) -> None:
    test_loan = Decimal('500')
    test_repay = test_loan + Decimal('500')
    sample_bank.add_client(sample_client)
    sample_bank.issue_loan(sample_client.passport, test_loan)
    with pytest.raises(exc.ClientOverpayWarning):
        sample_bank.repay_loan(sample_client.passport, test_repay)


    # def repay_loan(self, passport: str, amount: Decimal) -> Client:
    #     """Погашение кредита"""
    #     if amount <= 0:
    #         raise exc.InvalidAmountError(f'Amount {amount} must be positive')
    #     client = self.get_client(passport)
    #     if self.client_db[passport].deposit < amount:
    #         raise exc.InsufficientClientFundsError(
    #             f'not enough money on {passport} client`s account'
    #         )
    #     if amount > client.credit:
    #         raise exc.ClientOverpayWarning(
    #             f'{passport} client is about to be charged more than needed'
    #         )
    #     client.credit -= amount
    #     client.deposit -= amount
    #     self.reserves += amount
    #     return client

