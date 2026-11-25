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

    def get_client(self, passport: str) -> Client | None:
        """Get a client from the bank database."""
        if passport not in self.client_db:
            raise ValueError(f'Passport {passport} does not exist')
        return self.client_db.get(passport)

    def client_data_base(self) -> None:
        """Show client full database"""
        print('client_data_base: ')
        for passport, info in self.client_db.items():
            print(info)
        return None

    def deposit_money(self, passport: str, amount: Decimal) -> Decimal:
        # 1. Проверка, что amount > 0 (иначе raise ValueError).
        # 2. Поиск клиента через self.get_client(passport).
        # 3. Прибавление amount к депозиту клиента (client.deposit) и к резерву банка (self.reserves).
        if amount <= 0:
            raise ValueError(f'Amount {amount} must be positive')
        client = self.get_client(passport)
        client.deposit += amount
        self.reserves += amount
        return client.deposit


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

        print('1. Присвоили новый номер------------------------------------')
        client_number += 1

        print('2. Собрали объект-------------------------------------------')
        client = Client(name=name, passport=passport, client_number=client_number)

        print('3. Отдали банку (банк положил его в свой словарь)-----------')
        try:
            bank.add_client(client)
            print('New client added - success')
        except ValueError as err:
            print(f'Warning: {err}. try again')

        print('4. Вывели всех клиентов, которые сейчас есть в банке:-------')
        bank.client_data_base()

        print('5. Поиск клиента по паспорту--------------------------------')
        find_client = input('input the key passport: ')
        try:
            search_result = bank.get_client(find_client)
            print('New client found - success\n'
                  f'Search result:\n{search_result}'
            )
        except ValueError as err:
            print(f'Warning: {err}. try again')
        else:
            print('Кладем деньги на депозитный счет----------------------------')

            try:
                deposit = Decimal(input())
                money_deposited = bank.deposit_money(search_result.passport, deposit)
                print(f'Deposit amount: {deposit}')
                print(f'Money deposited: {money_deposited}')
            except ValueError as err:
                print(f'Warning: {err}. try again')
