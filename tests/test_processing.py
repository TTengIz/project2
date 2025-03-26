import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_canceled(dictionary_list, expected_canceled):
    assert filter_by_state(dictionary_list, 'CANCELED') == expected_canceled

def test_filter_by_state_executed(dictionary_list, expected_executed):
    assert filter_by_state(dictionary_list, 'EXECUTED') == expected_executed

@pytest.mark.parametrize('dictionary', [
    123,
    '',
    {},
    ()
])
def test_filer_by_state_wrong_type(dictionary):
    with pytest.raises(TypeError):
        filter_by_state(dictionary)


def test_sort_by_date(dictionary_list, new_list):
    assert sort_by_date(dictionary_list, True) == new_list

def test_sort_by_date(dictionary_list, new_list_reverse):
    assert sort_by_date(dictionary_list, False) == new_list_reverse

@pytest.mark.parametrize('dictionary', [
    123,
    '',
    {},
    ()
])
def test_sort_by_date_wrong_type(dictionary):
    with pytest.raises(TypeError):
        sort_by_date(dictionary)
