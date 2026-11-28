import pytest
from bank_operator_simulator import models


@pytest.fixture
def sample_bank() -> models.Bank:
    data = models.Bank()
    yield data


@pytest.fixture
def sample_client() -> models.Client:
    data = models.Client(
        client_number=1, name='Ivan', passport='0000 000000'
    )
    return data