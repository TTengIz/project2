from typing import Iterable


def filter_by_state(dictionary_id: Iterable[list], state: str) -> list:
    ''' Функция которая принимает на вход список словарей и
    создает на выход новый список словарей с нужным ключем. '''
    new_dictionary = [] # Создаю новый список
    for dictionary in dictionary_id: # Перебираю значение ключей в списке словарей
        if dictionary['state'] == state: # Если такой имееется
            new_dictionary.append(dictionary) # Добавляю данный словарь в новый список словарей
    return new_dictionary # Возвращаю новый список


if __name__ == '__main__':
    dict_id = filter_by_state([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ])


print(filter_by_state(dict_id))
