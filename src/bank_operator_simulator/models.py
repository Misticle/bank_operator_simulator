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

    def add_client(self, new_client: Client) -> None:
        """Add a client to the bank."""
        if new_client.passport in self.client_db:
            raise ValueError(f'Passport {new_client.passport} already exists')
        self.client_db[new_client.passport] = new_client
        return None

    def get_client(self, client_number: int) -> None:
        """Get a client from the bank database."""
        for key, value in self.client_db.items():
            if client_number == key:
                print(f'passport {client_number} -> {value}')
                break
            else:
                print(f'passport {client_number} has not been added')
        return None

    def client_data_base(self, position) -> None:
        """Show client full database"""
        position = self.client_db
        print('client_data_base: ')
        for pasport, info in position.items():
            print(info)
        return None


class Operator:
    """Operator class to represent an operator"""
    #new_client - will be created here?
    def __init__(self):
        pass


if __name__ == '__main__':
    bank = Bank()
    client_number = 0
    while True:
        name = input('Введите имя клиента: ')
        passport = input('Введите паспорт: ')

        # 1. Присвоили новый номер
        client_number += 1

        # 2. Собрали объект
        client = Client(name=name, passport=passport, client_number=client_number)

        # 3. Отдали банку (банк положил его в свой словарь)
        try:
            bank.add_client(client)
            print('New client added - success')
        except ValueError as err:
            print(f'Warning: {err}. try again')

        # 4. Вывели всех клиентов, которые сейчас есть в банке:
        # for passport, client_obj in bank.client_db.items():
        #     print(f"Клиент: {client_obj.name} (паспорт: {passport})")

        bank.client_data_base(bank.client_db)

        # 5. Поиск клиента по паспорту
        find_client = input('input the key passport: ')
        bank.get_client(find_client)