''' tests
'''
import pytest

from google_sign import google_sign
from google_tr_async.google_tr_async import GEN_TOKEN

# tkk = '406644.3293161072'


def test_sanity():
    ''' test sanity

        var b = 406644;
        var b1 = 3293161072;

        TKK = '436443.3778881810'

        tkk = '406644.3293161072'
        GEN_TOKEN('test') -> google_sign('test', tkk)
    '''
    tkk = '406644.3293161072'
    # assert google_sign('test', TKK) == '476257.126138'
    assert google_sign('test', tkk) == GEN_TOKEN('test')


def test_empty():
    ''' test empty '''
    tkk = '406644.3293161072'
    assert google_sign('', tkk) == GEN_TOKEN('')


def test_nonascii():
    ''' test_nonascii '''
    tkk = '406644.3293161072'
    assert google_sign('中文', tkk) == GEN_TOKEN('中文')


def test_umlaut():
    ''' test_umlaut '''
    tkk = '406644.3293161072'
    assert google_sign('äöü', tkk) == GEN_TOKEN('äöü')


@pytest.mark.skip(reason=' chr(0x10001) odd one out')
def test_chr0x10001():
    ''' test_chr0x10001 '''
    tkk = '406644.3293161072'
    assert google_sign(chr(0x10001), tkk) == GEN_TOKEN(chr(0x10001))
