''' tests
'''
from google_sign import google_sign, TKK


def test_sanity():
    ''' test sanity '''
    assert google_sign('test', TKK) == '476257.126138'


def test_empty():
    ''' test empty '''
    assert google_sign('', TKK) == '791388.703367'


def test_empty_0():
    ''' test empty0 '''
    assert google_sign('', '0') == '0.0'


def test_x_0():
    ''' test x 0 '''
    assert google_sign('x', '0') == '489829.489829'


def test_tkk01():
    ''' test_tkk01 '''
    assert google_sign('', '0.1') == '1.1'


def test_nonascii():
    ''' test_nonascii '''
    assert google_sign('中文', TKK) == '473815.102924'


def test_nonascii():
    ''' test_nonascii '''
    assert google_sign('中文', TKK) == '473815.102924'


def test_nonascii():
    ''' test_nonascii '''
    assert google_sign('中文', TKK) == '473815.102924'


def test_umlaut():
    ''' test_umlaut '''
    assert google_sign('äöü', TKK) == '570289.924522'


def test_chr0x10001():
    ''' test_chr0x10001 '''
    assert google_sign(chr(0x10001), TKK) == '729014.898925'


def test_tkk_none():
    ''' test_tkk_none, fetch tkk on the fly '''
    assert len(google_sign('test', tkk=None)) == 13
