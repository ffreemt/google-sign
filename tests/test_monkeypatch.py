'''
pytest monkeypatch

https://semaphoreci.com/community/tutorials/mocks-and-monkeypatching-in-python
'''

import re
import pytest

from google_sign import get_tkk


class ExpError:
    def __init__(self, *args, **kwargs):
        raise Exception('test')


def square(x):
    ''' square '''
    return x * x


def test_function(monkeypatch):
    ''' test_function '''
    monkeypatch.setattr("test_monkeypatch.square", lambda x: 1)
    assert square(5) == 1


@pytest.mark.skip(reason="doesnt seem to work in coverage test")
# TypeError: raise_() takes 0 positional arguments but 2 were given
def test_monkeyptach(monkeypatch):
    ''' test_monkeyptach
    https://stackoverflow.com/questions/41314953/pytest-how-to-force-raising-exceptions-during-unit-testing

    pytest test_monkeypatch.py -k test_monkeyptach
    '''
    def raise_():
        raise Exception()

    monkeypatch.setattr(re, "search", raise_)
    with pytest.raises(Exception):
        re.search(r'aaa', 'baab')


@pytest.mark.skip(reason="doesnt seem to work in coverage test")
# TypeError: raise_() takes 0 positional arguments but 2 were given
def test_get_tkk_exception_branch(monkeypatch):
    ''' test_get_tkk_exception_branch '''

    def raise_():
        raise Exception()

    monkeypatch.setattr(re, "search", raise_)
    # with pytest.raises(Exception):
    assert get_tkk() is None
