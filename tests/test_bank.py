import pytest
from bank_operator_simulator import models
from bank_operator_simulator import exceptions as exc


# 1. add_client
def test_add_client_success(sample_bank, sample_client) -> None:
    """Проверка регистрации нового клиента"""
    sample_bank.add_client(sample_client)
    assert sample_client.passport in sample_bank.client_db

# 2. deposit_money

# 3. issue_loan
