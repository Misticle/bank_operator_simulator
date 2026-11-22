#bank simulator - BS
import date from datetime
import decimal from Decimal

class BS:
    def __init__(self):
        pass

class Operator(BS):
    def __init__(self):
        pass

class Client(BS):
    def __init__(self, name: str, passport: str, reg_date: date, deposit: decimal, credit: deciaml):
        self.name = name
        self.passport = passport
        self.reg_date = reg_date
        self.deposit = deposit
        self.credit = credit