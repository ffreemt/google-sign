''' tests
'''
from google_sign import google_sign

def test_sanity():
    ''' test sanity '''
    assert google_sign('test') == '476257.126138'

def test_empty():
    ''' test empty '''
    assert google_sign('') == '791388.703367'
