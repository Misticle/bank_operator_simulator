#bank simulator - BS
from datetime import date
from decimal import Decimal


class Client:
    """Client model"""

    def __init__(
            self, client_number: int = 0, name: str = 'name',
            passport: str = '0000 000000', reg_date: date = date.today(),
            deposit: Decimal = Decimal('0'), credit: Decimal = Decimal('0')
    ) -> None:
        self.client_number = client_number
        self.name = name
        self.passport = passport
        self.reg_date = reg_date
        self.deposit = deposit
        self.credit = credit

    def __str__(self) -> str:
        return (
            f'клиент №: {self.client_number},\n'
            f'имя: {self.name},\n'
            f'паспорт №: {self.passport},\n'
            f'дата регистрации в системе: {self.reg_date},\n'
            f'баланс счета: {self.deposit} ₽,\n'
            f'сумма кредита: {self.credit} ₽'
        )


class Bank:
    def __init__(
            self, name: str = "Банк",
            reserves: Decimal = Decimal('5000000'),
    ) -> None:
        self.name = name
        self.reserves = reserves
        self.clients: dict = {}

    def add_client(self, client: Client):
        """Add a client to the bank."""
        pass


class Operator:
    """Operator class to represent an operator"""

    def __init__(self):
        pass


if __name__ == '__main__':
    # cli = Client()
    # cli = Client(
    #     1, 'alex', '1234 123456',
    #     date.today(), Decimal('100'), Decimal('100')
    # )
    cli = Client(1, 'alex', '1234 123456')

    print(cli)