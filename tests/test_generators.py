import pytest
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency_usd(transactions):
    currency_name = filter_by_currency(transactions, 'USD')
    assert next(currency_name) == {
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
        }


def test_filter_by_currency_rub(transactions):
    currency_name = filter_by_currency(transactions, 'RUB')
    assert next(currency_name) == {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        }
    assert next(currency_name) == {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }


@pytest.mark.parametrize('transactions', [
    123,
    '',
    {},
    ()
])
def test_filter_by_currency_wrong_type(transactions):
    with pytest.raises(TypeError):
        a = filter_by_currency(transactions)
        next(a)


def test_transaction_descriptions(transactions):
    result = transaction_descriptions(transactions)
    assert next(result) == 'Перевод организации'
    assert next(result) == 'Перевод со счета на счет'
    assert next(result) == 'Перевод со счета на счет'
    assert next(result) == 'Перевод с карты на карту'
    assert next(result) == 'Перевод организации'


def test_card_number_generator(start, stop):
    expected_result_1 = '0000 0000 0000 0001'
    expected_result_2 = '0000 0000 0000 0002'
    expected_result_3 = '0000 0000 0000 0003'
    expected_result_4 = '0000 0000 0000 0004'
    expected_result_5 = '0000 0000 0000 0005'
    card_number = card_number_generator(start, stop)
    assert next(card_number) == expected_result_1
    assert next(card_number) == expected_result_2
    assert next(card_number) == expected_result_3
    assert next(card_number) == expected_result_4
    assert next(card_number) == expected_result_5



@pytest.mark.parametrize('start, stop', [
    (10**16, 10**16+1),
    (10**20, 10**20+1)
])
def test_invalid_card_number_generator(start, stop):
    with pytest.raises(ValueError, match= "Номер карты не может быть длиннее 16 цифр"):
        a = card_number_generator(start, stop)
        next(a)
