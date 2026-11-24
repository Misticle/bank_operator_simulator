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
        self.client_db: dict[str, Client] = {} #client database

    def add_client(self, new_client: Client):
        """Add a client to the bank."""
        if new_client.passport in self.client_db:
            raise ValueError(f'Passport {new_client.passport} already exists')
        self.client_db[new_client.passport] = new_client

    def get_client(self, client_number: int) -> Client:
        """Get a client from the bank database."""
        pass

    # def client_data_base(self) -> None:
    #     """Show client full database"""
    #     for pasport, info in self.clients:
    #         self.clients[pasport]['name'] = pasport
    #     return None


class Operator:
    """Operator class to represent an operator"""
    #new_client - will be created here?
    def __init__(self):
        pass


if __name__ == '__main__':
    bank = Bank()

    while True:
        name = input('Введите имя клиента: ')
        passport = input('Введите паспорт: ')

        # 1. Собрали объект
        client = Client(name=name, passport=passport)

        # 2. Отдали банку (банк положил его в свой словарь)
        try:
            bank.add_client(client)
            print('New client added - success')
        except ValueError as err:
            print(f'Warning: {err}. try again')

        # 3. Вывели всех клиентов, которые сейчас есть в банке:
        for passport, client_obj in bank.client_db.items():
            print(f"Клиент: {client_obj.name} (паспорт: {passport})")