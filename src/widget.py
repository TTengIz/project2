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

# "2024-03-11T02:26:18.671407"
def get_date(date_imput: str) -> str:
    ''' Функция, которая меняет вормат даты. '''
    return ".".join(date_imput[:10].split("-")[::-1])
