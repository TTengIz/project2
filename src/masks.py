def get_mask_card_number(cart_number: str) -> str:
    """ Функция, которая принимает на вход номер катры и возвращает ее маску.
    Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX, где X - это цифра номера."""
    if len(cart_number) != 16:
        raise ValueError('Ввели некорректный номер карты')
    return f"{cart_number[:4]} {cart_number[4:6]}** **** {cart_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """ Функция, которая принимает на вход номер счета и возвращает его маску.
    Номер счета замаскирован и отображается в формате **XXXX, где X - это
    цифрв номера. То есть видны только последние цифры номера, а перед ним две звездочки."""
    if len(account_number) != 20:
        raise ValueError('Ввели некорректный номер аккаунта')
    return f"**{account_number[-4:]}"
