from utils import main


def test_get_mask_card():
    assert main.get_mask_card('2842878893689012') == '2842 87** **** 9012'
    assert main.get_mask_card('9171987821259925') == '9171 98** **** 9925'
    assert main.get_mask_card('1813166339376336') == '1813 16** **** 6336'


def test_get_mask_account():
    assert main.get_mask_account('2842878893689012') == '**9012'
    assert main.get_mask_account('9171987821259925') == '**9925'
    assert main.get_mask_account('1813166339376336') == '**6336'


def test_get_executed_operations():
    test_all_operations = [
        {
          "id": 441945886,
          "state": "EXECUTED",
          "date": "2019-08-26T10:50:58.294041",
          "operationAmount": {
            "amount": "31957.58",
            "currency": {
              "name": "руб.",
              "code": "RUB"
            }
          },
          "description": "Перевод организации",
          "from": "Maestro 1596837868705199",
          "to": "Счет 64686473678894779589"
        },
      {
        "id": 41428829,
        "state": "CANCELED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
          "amount": "8221.37",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
      },
      {
        "id": 939719570,
        "state": "CANCELED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
          "amount": "9824.07",
          "currency": {
            "name": "USD",
            "code": "USD"
          }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
      },
      {
        "id": 587085106,
        "state": "CANCELED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
          "amount": "48223.05",
          "currency": {
            "name": "руб.",
            "code": "RUB"
          }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
      },
    ]
    test_ex_operations = [
        {
          "id": 441945886,
          "state": "EXECUTED",
          "date": "2019-08-26T10:50:58.294041",
          "operationAmount": {
            "amount": "31957.58",
            "currency": {
              "name": "руб.",
              "code": "RUB"
            }
          },
          "description": "Перевод организации",
          "from": "Maestro 1596837868705199",
          "to": "Счет 64686473678894779589"
        },
    ]
    assert main.get_executed_operations([{}]) == []
    assert main.get_executed_operations(test_all_operations) == test_ex_operations

def test_print_operations():
  test_ex_op = [
    {
      "id": 441945886,
      "state": "EXECUTED",
      "date": "2019-08-26T10:50:58.294041",
      "operationAmount": {
        "amount": "31957.58",
        "currency": {
          "name": "руб.",
          "code": "RUB"
        }
      },
      "description": "Перевод организации",
      "from": "Maestro 1596837868705199",
      "to": "Счет 64686473678894779589"
    },
    {
      "id": 441945886,
      "state": "EXECUTED",
      "date": "2019-08-26T10:50:58.294041",
      "operationAmount": {
        "amount": "31957.58",
        "currency": {
          "name": "руб.",
          "code": "RUB"
        }
      },
      "description": "Перевод организации",
      "from": "Maestro 1596837868705199",
      "to": "Счет 64686473678894779589"
    },
    {
      "id": 41428829,
      "state": "EXECUTED",
      "date": "2019-07-03T18:35:29.512364",
      "operationAmount": {
        "amount": "8221.37",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод организации",
      "from": "MasterCard 7158300734726758",
      "to": "Счет 35383033474447895560"
    },
    {
      "id": 939719570,
      "state": "EXECUTED",
      "date": "2018-06-30T02:08:58.425572",
      "operationAmount": {
        "amount": "9824.07",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод организации",
      "from": "Счет 75106830613657916952",
      "to": "Счет 11776614605963066702"
    },
    {
      "id": 587085106,
      "state": "EXECUTED",
      "date": "2018-03-23T10:45:06.972075",
      "operationAmount": {
        "amount": "48223.05",
        "currency": {
          "name": "руб.",
          "code": "RUB"
        }
      },
      "description": "Открытие вклада",
      "to": "Счет 41421565395219882431"
    },
  ]
  test_ex_op_len = [
    {
      "id": 441945886,
      "state": "EXECUTED",
      "date": "2019-08-26T10:50:58.294041",
      "operationAmount": {
        "amount": "31957.58",
        "currency": {
          "name": "руб.",
          "code": "RUB"
        }
      },
      "description": "Перевод организации",
      "from": "Maestro 1596837868705199",
      "to": "Счет 64686473678894779589"
    },
    {
      "id": 441945886,
      "state": "EXECUTED",
      "date": "2019-08-26T10:50:58.294041",
      "operationAmount": {
        "amount": "31957.58",
        "currency": {
          "name": "руб.",
          "code": "RUB"
        }
      },
      "description": "Перевод организации",
      "from": "Maestro 1596837868705199",
      "to": "Счет 64686473678894779589"
    },
    {
      "id": 41428829,
      "state": "EXECUTED",
      "date": "2019-07-03T18:35:29.512364",
      "operationAmount": {
        "amount": "8221.37",
        "currency": {
          "name": "USD",
          "code": "USD"
        }
      },
      "description": "Перевод организации",
      "from": "MasterCard 7158300734726758",
      "to": "Счет 35383033474447895560"
    },
  ]
  test_print = [
    {
      'date': '26.08.2019',
      "description": "Перевод организации",
      'from': 'Maestro 1596 83** **** 5199',
      'to': 'Счет **9589', 'amount': '31957.58',
      'currency': 'руб.'
    },
    {
      'date': '26.08.2019',
      "description": "Перевод организации",
      'from': 'Maestro 1596 83** **** 5199',
      'to': 'Счет **9589', 'amount': '31957.58', 'currency': 'руб.'
    },
    {
      'date': '03.07.2019',
      "description": "Перевод организации",
      'from': 'MasterCard 7158 30** **** 6758',
      'to': 'Счет **5560', 'amount': '8221.37',
      'currency': 'USD'
    },
    {
      'date': '30.06.2018',
      "description": "Перевод организации",
      'from': 'Счет **6952',
      'to': 'Счет **6702',
      'amount': '9824.07',
      'currency': 'USD'
    },
    {
      'date': '23.03.2018',
      "description": "Открытие вклада",
      'from': '', 'to': 'Счет **2431',
      'amount': '48223.05',
      'currency': 'руб.'
    }
  ]
  assert main.list_operations(test_ex_op_len) == 'количество выполненных операций меньше 5!'
  assert main.list_operations(test_ex_op) == test_print
