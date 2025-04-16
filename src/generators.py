from typing import Dict, Iterator, List


def filter_by_currency(transactions: List[Dict], currency: str = 'USD') -> Iterator[List[Dict]]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции,
    и возвращает итератор, который поочередно выдает транзакции, где валюта соответствует заданной."""
    print(type(transactions))
    if not isinstance(transactions, list):
        raise TypeError('Некоректное значение')
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Iterator[str]:
    """Функция, которая принимает на вход список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        if transaction['description']:
            yield transaction['description']


def card_number_generator(start, stop) -> Iterator[str]:
    ''' Функция, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Функция может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999 '''
    numbers = range(start, stop+1)
    kard_mask = '0000000000000000'
    for kard in numbers:
        if len(str(kard)) >= 17:
            raise ValueError("Номер карты не может быть длиннее 16 цифр")
        kard_mask = kard_mask[: -len(str(kard))] + str(kard)
        yield f'{kard_mask[:4]} {kard_mask[4:8]} {kard_mask[8:12]} {kard_mask[12:]}'

