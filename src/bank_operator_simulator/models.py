from datetime import date
from decimal import Decimal

from bank_operator_simulator import exceptions as exc
from bank_operator_simulator.security import require_admin


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
    """Bank model"""
    
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
            raise exc.ClientAlreadyExistsError(f'Passport {new_client.passport} already exists')
        self.client_db[new_client.passport] = new_client
        return None

    def get_client(self, passport: str) -> Client | None:
        """Get a client from the bank database."""
        if passport not in self.client_db:
            raise exc.ClientNotFoundError(f'Passport {passport} does not exist')
        return self.client_db.get(passport)

    @require_admin
    def client_data_base(self) -> None:
        """Show client full database"""
        print('client_data_base: ')
        for passport, info in self.client_db.items():
            print(info)
        return None

    @require_admin
    def deposit_money(self, passport: str, amount: Decimal) -> Decimal:
        """внесение средств на депозитный счет"""
        if amount <= 0:
            raise exc.InvalidAmountError(f'Amount {amount} must be positive')
        client = self.get_client(passport)
        client.deposit += amount
        self.reserves += amount
        return client.deposit

    @require_admin
    def issue_loan(self, passport: str, amount: Decimal) -> Client:
        """Выдача кредита"""
        if amount <= 0:
            raise exc.InvalidAmountError(f'Amount {amount} must be positive')
        client = self.get_client(passport)
        if amount > self.reserves:
            raise exc.InsufficientBankFundsError(f'Amount {amount} cannot be greater than reserves')
        self.reserves -= amount
        client.credit += amount
        client.deposit += amount
        return client

    @require_admin
    def repay_loan(self, passport: str, amount: Decimal) -> Client:
        """Погашение кредита"""
        if amount <= 0:
            raise exc.InvalidAmountError(f'Amount {amount} must be positive')
        client = self.get_client(passport)
        if amount > client.credit:
            raise exc.ClientOverpayWarning(
                f'{passport} client is about to be charged more than needed'
            )
        if self.client_db[passport].deposit < amount:
            raise exc.InsufficientClientFundsError(
                f'not enough money on {passport} client`s account'
            )
        client.credit -= amount
        client.deposit -= amount
        self.reserves += amount
        return client

    @require_admin
    def show_reserves(self) -> Decimal:
        """Показать текущие резервы банка (только для админа)."""
        return self.reserves


class Operator:
    """Operator class to represent an operator"""
    #new_client - will be created here?
    def __init__(self):
        pass
