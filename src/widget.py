from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_number: str) -> str:
    ''' Функция, которая маскирует номер карты или номер счета в зависимости от типа.'''
    type_number_list = type_number.split()
    if len(type_number) == 0:
        raise ValueError('Некорректный формат номера счета')
    if 'Счет' in type_number_list:
        return f'Счет {get_mask_account(type_number_list[1])}'
    else:
        number = get_mask_card_number(type_number[-16:])
        updated_card_number = " ".join(type_number.split()[:-1]) + " " + number
        return updated_card_number


def get_date(date_input: str) -> str:
    ''' Функция, которая меняет вормат даты. '''
    return ".".join(date_input[:10].split("-")[::-1])
