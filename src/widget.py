from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number: str) -> str:
    ''' Функция, которая маскирует номер карты или номер счета в зависимости от типа.'''
    type_number_list = type_number.split()
    if 'Счет' in type_number_list:
        return f'Счет {get_mask_account(type_number_list[1])}'
    elif 'MasterCard' in type_number_list or 'Maestro' in type_number_list:
        return f'{type_number_list[0]} {get_mask_card_number(type_number_list[1])}'
    elif 'Visa' in type_number_list:
        number_card = []
        simbol_card = []
        for i in type_number_list:
            if i.isdigit():
                number_card.append(i)
            elif i.isalpha():
                simbol_card.append(i)
        total_number_card = ''.join(number_card)
    return f'{simbol_card[0]} {simbol_card[1]} {get_mask_card_number(total_number_card)}'


def get_date(date_imput: str) -> str:
    ''' Функция, которая меняет вормат даты. '''
    dt = datetime.fromisoformat(date_imput)
    formatted_date = dt.strftime('%d.%m.%Y')
    return formatted_date


date_imput = "2024-03-11T02:26:18.671407"
print(get_date(date_imput))
print(mask_account_card('Maestro 1596837868705199'))
print(mask_account_card('Счет 64686473678894779589'))
print(mask_account_card('MasterCard 7158300734726758'))
print(mask_account_card('Счет 35383033474447895560'))
print(mask_account_card('Visa Classic 6831982476737658'))
print(mask_account_card('Visa Platinum 8990922113665229'))
print(mask_account_card('Visa Gold 5999414228426353'))
print(mask_account_card('Счет 73654108430135874305'))
