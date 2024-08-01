# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления
# и снятия средств в список.


import decimal

# Настройка точности
decimal.getcontext().prec = 2

# Константы
MULTIPLICITY = 50
PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
COUNT_PER = 3
MIN_LIMIT = decimal.Decimal(30)
MAX_LIMIT = decimal.Decimal(600)
PERCENT_RICHNESS = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_AMOUNT = 5_000_000
CMD_DEPOSIT = '1'
CMD_WINDRAW = '2'
CMD_EXIT = '3'

# Глобальные переменные
balance = decimal.Decimal(0)
operations = 0
transaction_history = []


def apply_richness_tax(balance):
    """Вычисляет налог на богатство и обновляет баланс."""
    if balance > RICHNESS_AMOUNT:
        tax_amount = balance * PERCENT_RICHNESS
        balance -= tax_amount
        print(f'Вычтен налог на богатство в размере {tax_amount}')
    return balance


def deposit(amount):
    """Пополнение баланса."""
    global balance, operations
    balance += amount
    operations += 1
    transaction_history.append(f'Пополнение: {amount}')
    print(f'Текущий баланс: {balance}')


def withdraw(amount):
    """Снятие средств с учетом комиссии."""
    global balance, operations
    comission = amount * PERCENT
    comission = max(MIN_LIMIT, min(comission, MAX_LIMIT))

    if comission + amount > balance:
        print('На балансе недостаточно средств')
    else:
        balance -= (amount + comission)
        operations += 1
        transaction_history.append(f'Снятие: {amount}, Комиссия: {comission}')
        print(f'Сумма снятия: {amount}, Комиссия: {comission}, Общая сумма: {amount + comission}')


def apply_bonus():
    """Применяет бонус к балансу каждые COUNT_PER операций."""
    global balance, operations
    if operations % COUNT_PER == 0:
        bonus_sum = balance * PERCENT_BONUS
        balance += bonus_sum
        print(f'Сумма бонуса: {bonus_sum}')


def main():
    global balance
    while True:
        action = input(
            f'Пополнить - {CMD_DEPOSIT}\n'
            f'Снять - {CMD_WINDRAW}\n'
            f'Выход - {CMD_EXIT}\n'
            f'Введите действие: \n'
        )

        balance = apply_richness_tax(balance)

        if action == CMD_DEPOSIT:
            amount = int(input(f'Введите сумму пополнения кратную {MULTIPLICITY}: '))
            while amount % MULTIPLICITY != 0:
                amount = int(input(f'Введите сумму пополнения кратную {MULTIPLICITY}: '))
            deposit(amount)

        elif action == CMD_WINDRAW:
            amount = int(input('Введите сумму снятия: '))
            withdraw(amount)

        elif action == CMD_EXIT:
            break

        else:
            print('Введена неверная команда')

        apply_bonus()
        print(f'Текущий баланс: {balance}')

    print("История транзакций:")
    for transaction in transaction_history:
        print(transaction)


if __name__ == "__main__":
    main()