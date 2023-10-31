import json
from datetime import datetime


def read_json(path):
    file = open(path, 'r', encoding='utf-8')
    operations = json.load(file)
    return operations


def get_mask_card(account: str):
    account = account.replace(account[6:12], '******')
    numbers = [account[:4], account[4:8], account[8:12], account[12:16]]
    account = ' '.join(numbers)
    return account


def get_mask_account(bank_account: str):
    len_account = len(bank_account)
    bank_account_mask = bank_account.replace(bank_account[:len_account-4], '**')
    return bank_account_mask


def get_executed_operations(all_operations):
    """
    Функция отбора выполненных операций и сортировки полученного списка по дате совершения операций
    :param all_operations:Список операций
    :return: отсортированный по дате список проведенных операций
    """
    ex_operations = []
    for operation in all_operations:
        if not (not operation):
            if operation['state'] == 'EXECUTED':
                ex_operations.append(operation)
    ex_operations = sorted(
        ex_operations,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True
    )
    return ex_operations


def print_operations(ex_operations: list):
    """
    Функция вывода пяти последних выполненных операций
    :param ex_operations: список выполненных операций
    :return: пять последних выполненных операций
    """
    for ex_operation in ex_operations[:5]:
        date = datetime.strptime(f"{ex_operation['date']}", '%Y-%m-%dT%H:%M:%S.%f')
        print(f'{date.strftime("%d.%m.%Y")} {ex_operation["description"]}')

        if "from" in ex_operation:
            operation = ex_operation['from'].split()
            if operation[0] != "Счет":
                secret_number = get_mask_card(operation[-1])
                operation[-1] = secret_number
                _from = ' '.join(operation)
            else:
                secret_count = get_mask_account(operation[len(operation)-1])
                operation[len(operation) - 1] = secret_count
                _from = ' '.join(operation)
        else:
            _from = ''

        operation = ex_operation['to'].split()
        if operation[0] != "Счет":
            secret_number = get_mask_card(operation[-1])
            operation[-1] = secret_number
            _to = ' '.join(operation)
        else:
            secret_count = get_mask_account(operation[-1])
            operation[-1] = secret_count
            _to = ' '.join(operation)
        print(f'{_from} -> {_to}')
        print(f'{ex_operation["operationAmount"]["amount"]} {ex_operation["operationAmount"]["currency"]["name"]}'+"\n")
