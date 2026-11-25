class BankError(Exception):  # общий родитель всех ошибок банка.
    """Базовое исключение банка."""


class ClientAlreadyExistsError(BankError)  :# клиент уже есть в базе.
    """Клиент уже существует в базе"""


class ClientNotFoundError(BankError):  # клиент не найден.
    """Клиент не найден"""


class InvalidAmountError(BankError):  # сумма <= 0.
    """Не верное значение суммы"""


class InsufficientBankFundsError(BankError):  # у банка не хватает резервов для выдачи кредита!
    """Банк стал БОМЖОМ!"""

