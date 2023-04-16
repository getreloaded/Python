from fuel import convert
from fuel import gauge

def test_convert():
    assert convert('22/7') == False
    assert convert('4/5') == '80%'
    assert convert('-1.4') == False
    assert convert('fraction') == False
    assert convert('0/2') == 'E'
    assert convert('99.5/100') == False
    assert convert('4/4') == 'F'