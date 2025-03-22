import pytest

from src.masks import get_mask_card_number

from src.masks import get_mask_account


def test_mask_card_number(card_number):
    assert get_mask_card_number(card_number) == '7000 79** **** 6361'


@pytest.mark.parametrize('card',[
    ('700079228960636121'),
    ('7000792289606'),
    ('')
])
def test_invalid_card_number(card):
    with pytest.raises(ValueError):
        get_mask_card_number(card)


def test_get_mask_account():
    assert get_mask_account(card_account) == '**4305'


@pytest.mark.parametrize('account',[
    ('73654108430135874305123'),
    ('7365410843013587'),
    ('')
])
def test_invalid_account_number(account):
    with pytest.raises(ValueError):
        get_mask_account(account)
