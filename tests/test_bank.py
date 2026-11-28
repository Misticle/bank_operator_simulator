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
    sample_bank.add_client(sample_client)
    sample_bank.deposit_money(sample_client.passport, Decimal('500'))
    assert sample_bank.client_db[sample_client.deposit] == deposit

def test_deposit_success(sample_bank, sample_client) -> None:
    sample_bank.add_client(sample_client)
    with pytest.raises(exc.InvalidAmountError):
        sample_bank.deposit_money(sample_client.passport, Decimal('0'))

def test_deposit_success(sample_bank, sample_client) -> None:
    sample_bank.add_client(sample_client)
    with pytest.raises(exc.InvalidAmountError):
        sample_bank.deposit_money(sample_client.passport, Decimal('-500'))

# 3. issue_loan



    # def deposit_money(self, passport: str, amount: Decimal) -> Decimal:
    #     """внесение средств на депозитный счет"""
    #     if amount <= 0:
    #         raise exc.InvalidAmountError(f'Amount {amount} must be positive')
    #     client = self.get_client(passport)
    #     client.deposit += amount
    #     self.reserves += amount
    #     return client.deposit

# InsufficientBankFundsError


# 4. погашение

# ClientOverpayWarning

# InsufficientClientFundsError


# -------------------------------------
# @pytest.mark.parametrize(
#     'a, b, expected',
#     [
#         (50, 200, (50, 200, 250)),
#         (50, -200, (50, -200, -150)),
#         (-50, 200, (-50, 200, 150)),
#         (-50, -200, (-50, -200, -250)),
#     ],
#     ids = ['+/+', '+/-', '-/+', '-/-']
# )
# def test_function_xyz(a, b, expected: tuple):
#     assert function_xyz(a, b) == expected
