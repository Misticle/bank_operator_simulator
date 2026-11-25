class BankError(Exception):
    """Базовое исключение банка."""


class ClientAlreadyExistsError(BankError):
    """Клиент уже существует в базе"""


class ClientNotFoundError(BankError):
    """Клиент не найден"""


class InvalidAmountError(BankError):
    """Не верное значение суммы"""


class InsufficientBankFundsError(BankError):
    """Недостаточно средств в резервах банка."""

