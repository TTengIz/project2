from typing import Iterable, List, Dict
from datetime import datetime
from src.widget import get_date


def filter_by_state(dictionary_list: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    ''' Функция которая принимает на вход список словарей и
    создает на выход новый список словарей с нужным ключем. '''
    new_dictionary = [] # Создаю новый список
    for dictionary in dictionary_list: # Перебираю значение ключей в списке словарей
        if dictionary['state'] == state: # Если такой имееется
            new_dictionary.append(dictionary) # Добавляю данный словарь в новый список словарей
    return new_dictionary # Возвращаю новый список


def sort_by_date(dictionary_list: List[Dict], increase: bool = True) -> List[Dict]:
    ''' Функция, которая принимает на вход список словарей, который сортирует по дате
    на убываение и возвращает новый отсортированный спиок. '''
    new_list = sorted(
        dictionary_list,
        reverse=increase,
        key=lambda x: datetime.strptime(x['date'],"%Y-%m-%dT%H:%M:%S.%f")
    )
    return new_list

if __name__ == '__main__':
    dict_id = filter_by_state([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ], 'CANCELED')


    print(dict_id)
    dict_time = sort_by_date([
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ], True)


    print(dict_time)
