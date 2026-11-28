

if __name__ == '__main__':
    print_hi('PyCharm')

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
        except exc.ClientAlreadyExistsError as err:
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
        except exc.ClientNotFoundError as err:
            print(f'Warning: {err}. try again')
        else:
            print('Кладем деньги на депозитный счет----------------------------')

            try:
                deposit = Decimal(input())
                money_deposited = bank.deposit_money(search_result.passport, deposit)
                print(f'Deposit amount: {deposit}')
                print(f'Money deposited: {money_deposited}')
            except exc.InvalidAmountError as err:
                print(f'Warning: {err}. try again')
